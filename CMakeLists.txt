cmake_minimum_required(VERSION 3.6)
project(STL)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=c99")
set(SOURCE_FILES 20171214/lyrichu_20171214_02.cpp 20180102/lyrichu_20180102_01.cpp)
add_executable(STL ${SOURCE_FILES})



