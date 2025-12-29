add_executable(decoratedocs
	../../src/scanner.cpp
	main.cpp
)

set_target_properties(decoratedocs PROPERTIES
	CXX_STANDARD 17
)

target_compile_definitions(decoratedocs PRIVATE SCANNER_USE_STD_STRING SCANNER_STANDALONE mysnprintf=snprintf)

target_include_directories(decoratedocs PRIVATE "${CMAKE_CURRENT_SOURCE_DIR}/../../src")
