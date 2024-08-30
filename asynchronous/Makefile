# Makefile for Boost.Asio project

# 컴파일러 설정
CXX = g++
CXXFLAGS = -std=c++17 -I D:/cpp_lib/TransmissionControlProtocol/boost_1_86_0

# 라이브러리 설정
LDFLAGS = -L D:/cpp_lib/TransmissionControlProtocol/boost_1_86_0/stage/lib -lws2_32

# 대상 파일 설정
TARGET = python_control
SOURCES = python_control.cpp
# TARGET = event_receiver
# SOURCES = event_receiver.cpp

# 빌드 명령
all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(SOURCES) $(LDFLAGS)

# 정리 명령
clean:
	rm -f $(TARGET)
