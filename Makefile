CXX = g++
CXXFLAGS = -std=c++17 -Wall -Iinclude   # inclure le dossier des headers
LDFLAGS = 

SRC_DIR = src
OBJ_DIR = build
BIN = nf_beta

# Récupérer tous les fichiers .cpp dans src
SRCS := $(wildcard $(SRC_DIR)/*.cpp)

# Générer les fichiers objets correspondants dans build/
OBJS := $(patsubst $(SRC_DIR)/%.cpp,$(OBJ_DIR)/%.o,$(SRCS))

# ==========================
# Règles
# ==========================
all: $(BIN)

# Construire l’exécutable à partir des objets
$(BIN): $(OBJS)
	$(CXX) $(CXXFLAGS) $^ -o $@ $(LDFLAGS)

# Construire les fichiers objets à partir des fichiers sources
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp | $(OBJ_DIR)
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Créer le dossier build si nécessaire
$(OBJ_DIR):
	mkdir -p $(OBJ_DIR)

# Nettoyer les fichiers compilés
clean:
	rm -rf $(OBJ_DIR) $(BIN)

run: $(BIN)
	./$(BIN)

.PHONY: all clean
