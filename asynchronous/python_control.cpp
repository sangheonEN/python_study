#include <iostream>
#include <boost/asio.hpp>
#include <boost/asio/ip/tcp.hpp>
#include <cstdlib> // system() 함수 사용을 위해 추가
#include <string>
#include <thread>
#include <atomic>

// Boost.Asio의 네임스페이스 사용
using boost::asio::ip::tcp;

// Python 프로세스를 관리하기 위한 전역 변수
std::atomic<bool> python_process_running(false);

// Python 스크립트의 절대 경로 지정
const std::string python_script_path = "D:\\git_hub\\python_study\\asynchronous\\event_send.py";

// Anaconda 가상환경 활성화 및 Python 스크립트 실행 명령 생성
std::string get_start_command() {
    std::string activate_env = "call C:\\Users\\USER\\anaconda3\\Scripts\\activate.bat base && ";
    std::string python_command = "python " + python_script_path;
    return activate_env + python_command;
}

void start_python_process() {
    if (!python_process_running) {
        std::cout << "Starting Python process in Anaconda base environment..." << std::endl;
        python_process_running = true;
        // Python 스크립트 실행 (백그라운드에서)
        std::thread([]() {
            std::string command = "start cmd /c \"" + get_start_command() + "\"";  // Windows에서 새로운 CMD 창에서 실행
            system(command.c_str());
            python_process_running = false;
        }).detach();
    } else {
        std::cout << "Python process is already running." << std::endl;
    }
}

void stop_python_process() {
    if (python_process_running) {
        std::cout << "Stopping Python process..." << std::endl;
        // Python 프로세스 종료
        system("taskkill /IM python.exe /F");  // 모든 Python 프로세스 종료
        python_process_running = false;
    } else {
        std::cout << "Python process is not running." << std::endl;
    }
}

int main() {
    try {
        boost::asio::io_context io_context;

        // TCP 서버 소켓 생성, 포트 12345에서 리슨
        tcp::acceptor acceptor(io_context, tcp::endpoint(tcp::v4(), 12345));
        std::cout << "Server is listening on port 12345..." << std::endl;

        while (true) {
            tcp::socket socket(io_context); // Boost.Asio의 TCP 소켓 사용
            acceptor.accept(socket);  // 클라이언트 연결 수락
            std::cout << "Client connected." << std::endl;

            // 클라이언트로부터 데이터 수신
            char data[1024];
            boost::system::error_code error;  // 오류 코드를 받을 변수
            size_t length = socket.read_some(boost::asio::buffer(data), error); // 수정된 코드: 오류 코드 포함

            if (error) {
                std::cerr << "Error while reading: " << error.message() << std::endl;
                continue;
            }

            std::string received_data(data, length);
            std::cout << "Received command: " << received_data << std::endl;

            // 명령어 처리
            if (received_data == "start") {
                start_python_process();
            } else if (received_data == "stop") {
                stop_python_process();
            }

            // 소켓 닫기
            socket.close();
        }

    } catch (std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}
