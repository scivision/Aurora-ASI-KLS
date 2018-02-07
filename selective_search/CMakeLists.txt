cmake_minimum_required(VERSION 2.8)


# https://cmake.org/cmake/help/latest/module/FindPythonLibs.html
find_package(PythonInterp REQUIRED)
find_package(PythonLibs REQUIRED)

find_package(Boost REQUIRED COMPONENTS python numpy)

INCLUDE_DIRECTORIES(${Boost_INCLUDE_DIR} ${PYTHON_INCLUDE_DIRS})

add_library(segment SHARED segment_py.cpp)
target_link_libraries(segment ${Boost_LIBRARIES})
set_target_properties(segment PROPERTIES PREFIX "")