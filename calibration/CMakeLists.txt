cmake_minimum_required(VERSION 3.10)

project(OpenCVCameraDemo)

find_package(OpenCV REQUIRED)


add_executable(app streamCapture.cpp)

target_link_libraries(app ${OpenCV_LIBS})
