CXX = g++
CXXFLAGS = -std=c++17 -Wall -Iinclude -g
LDFLAGS = 

SRC_DIR = src
OBJ_DIR = build
BIN = nf

SRCS := $(shell find $(SRC_DIR) -name '*.cpp')

OBJS := $(patsubst $(SRC_DIR)/%, $(OBJ_DIR)/%, $(SRCS:.cpp=.o))

PREFIX ?= /usr/local

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

install: $(BIN)
	install -d $(PREFIX)/bin
	install -m 755 $(BIN) $(PREFIX)/bin/$(BIN)

uninstall:
	rm -f $(PREFIX)/bin/$(BIN)

.PHONY: all clean run
