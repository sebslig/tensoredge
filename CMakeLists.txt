cmake_minimum_required(VERSION 3.10)
project(tensoredge)

set(CMAKE_CXX_STANDARD 17)

add_library(tensoredge_core src/engine.hpp)

add_executable(tensoredge_cli src/main.cpp)
target_link_libraries(tensoredge_cli tensoredge_core)
