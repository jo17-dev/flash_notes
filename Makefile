CXX = g++
CXXFLAGS = -std=c++17 -Wall -Iinclude -g
LDFLAGS = 

SRC_DIR = src
OBJ_DIR = build
BIN = nf_beta

SRCS := $(shell find $(SRC_DIR) -name '*.cpp')

OBJS := $(patsubst $(SRC_DIR)/%, $(OBJ_DIR)/%, $(SRCS:.cpp=.o))


all: $(BIN)

$(BIN): $(OBJS)
	$(CXX) $(CXXFLAGS) $^ -o $@ $(LDFLAGS)

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp
	@mkdir -p $(dir $@)   # Créer le dossier si nécessaire
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -rf $(OBJ_DIR) $(BIN)

run: all
	./$(BIN)

.PHONY: all clean run
