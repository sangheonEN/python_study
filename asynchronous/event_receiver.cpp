#include <iostream>
#include <boost/asio.hpp>

using boost::asio::ip::tcp;

int main() {
    try {
        boost::asio::io_context io_context;

        // TCP 서버 소켓 생성, 포트 12345에서 리슨
        tcp::acceptor acceptor(io_context, tcp::endpoint(tcp::v4(), 12345));
        std::cout << "Server is listening on port 12345..." << std::endl;

        while (true) {
            tcp::socket socket(io_context);
            acceptor.accept(socket);  // 클라이언트 연결 수락
            std::cout << "Client connected." << std::endl;

            // 클라이언트로부터 데이터 수신
            char data[1024];
            size_t length = socket.read_some(boost::asio::buffer(data));
            std::string received_data(data, length);
            std::cout << "Received event parameter: " << received_data << std::endl;

            // 소켓 닫기
            socket.close();
        }

    } catch (std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}
