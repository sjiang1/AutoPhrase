CXX = g++
CXXFLAGS = -std=c++11 -Wall -g -O0 -msse2  -fopenmp  -I..

BIN = ./bin/segphrase_train ./bin/segphrase_segment
.PHONY: clean all

all: ./bin $(BIN)

./bin/segphrase_train: ./src/main.cpp ./src/utils/*.h ./src/frequent_pattern_mining/*.h ./src/data/*.h ./src/classification/*.h ./src/model_training/*.h ./src/clustering/*.h
./bin/segphrase_segment: ./src/segment.cpp ./src/utils/*.h ./src/frequent_pattern_mining/*.h ./src/data/*.h ./src/classification/*.h ./src/model_training/*.h ./src/clustering/*.h

./bin:
	mkdir -p bin

LDFLAGS= -pthread -lm -Wno-unused-result -Wno-sign-compare -Wno-unused-variable -Wno-parentheses -Wno-format
$(BIN) :
	$(CXX) $(CXXFLAGS) $(LDFLAGS) -o $@ $(filter %.cpp %.o %.c, $^)
$(OBJ) :
	$(CXX) -c $(CXXFLAGS) -o $@ $(firstword $(filter %.cpp %.c, $^) )

clean :
	rm -rf bin

