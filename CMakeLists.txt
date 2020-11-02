cmake_minimum_required(VERSION 3.17)
project(static_mdyn)

set(CMAKE_CXX_STANDARD 14)

add_executable(static_mdyn main.cpp common.h dipole_interaction.cpp)

set(BOOST_ROOT "C:/Program Files/boost_1_62_0")
find_package(Boost)
include_directories(${Boost_INCLUDE_DIRS})