cmake_minimum_required(VERSION 3.8)
set(CMAKE_C_COMPILER gcc)
set(CMAKE_CXX_COMPILER g++)

project(AutoPhrase)

set(CMAKE_BUILD_TYPE Debug)
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -Wall")

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

find_package(OpenMP REQUIRED)
if (OPENMP_FOUND)
    set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
    set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
endif()

set(SOURCE_FILES_train
        src/classification/feature_extraction.h
        src/classification/label_generation.h
        src/classification/predict_quality.h
        src/classification/random_forest.h
        src/clustering/clustering.h
        src/data/documents.h
        src/data/dump.h
        src/frequent_pattern_mining/frequent_pattern_mining.h
        src/model_training/segmentation.h
        src/utils/commandline_flags.h
        src/utils/parameters.h
        src/utils/random.h
        src/utils/utils.h
        src/main.cpp
        src/utils/filtered_phrases.h)

set(SOURCE_FILES_segment
        src/classification/feature_extraction.h
        src/classification/label_generation.h
        src/classification/predict_quality.h
        src/classification/random_forest.h
        src/clustering/clustering.h
        src/data/documents.h
        src/data/dump.h
        src/frequent_pattern_mining/frequent_pattern_mining.h
        src/model_training/segmentation.h
        src/utils/commandline_flags.h
        src/utils/parameters.h
        src/utils/random.h
        src/utils/utils.h
        src/segment.cpp
        src/utils/filtered_phrases.h)

add_executable(segphrase_train ${SOURCE_FILES_train})
add_executable(segphrase_segment ${SOURCE_FILES_segment})