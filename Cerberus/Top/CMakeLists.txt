####
# F Prime CMakeLists.txt:
#
# SOURCES: list of source files (to be compiled)
# AUTOCODER_INPUTS: list of files to be passed to the autocoders
# DEPENDS: list of libraries that this module depends on
#
# More information in the F´ CMake API documentation:
# https://fprime.jpl.nasa.gov/latest/docs/reference/api/cmake/API/
#
####

set(SPECIFIC_INSTANCES "${CMAKE_CURRENT_LIST_DIR}/instances-native.fpp")
if ("${FPRIME_PLATFORM}" STREQUAL Zephyr)
    set(SPECIFIC_INSTANCES "${CMAKE_CURRENT_LIST_DIR}/instances-zephyr.fpp")
endif()
register_fprime_module(
    AUTOCODER_INPUTS
        "${CMAKE_CURRENT_LIST_DIR}/instances.fpp"
        "${SPECIFIC_INSTANCES}"
        "${CMAKE_CURRENT_LIST_DIR}/topology.fpp"
    SOURCES
        "${CMAKE_CURRENT_LIST_DIR}/CerberusTopology.cpp"
)
