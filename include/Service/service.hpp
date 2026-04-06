#ifndef SERVICE_H

#define SERVICE_H

#include <string>
#include <string_view>
namespace service {
  inline constexpr std::string_view VERSION = "2.0.0";
  inline constexpr std::string_view VERSION_NAME = "beta";
  inline constexpr std::string_view DATA_DIR = "";
  inline constexpr std::string_view CANT_ADD_EMPTY_NOTE =
    "Can't add a empty note. usage: nf -a <your note>";
  inline constexpr std::string_view BAD_CALL = "Bad call. type nf -h for help";
  inline constexpr std::string_view ERROR_OPENING_FILE =
    "Error while opening the target file";
  inline constexpr std::string_view USAGE =
      " -h -> display this help \n -a -> Add a note \n no param -> print "
      "todays file path to stdoutput";
  inline constexpr std::string_view SAVED_TO = "Saved to: ";
  inline constexpr std::string_view HOME_NOT_SET = "Home env variable not set.";
    
  void initializeConf(); // permet d'initialiser tout le chemin pour le jour d'aujourdhui (possiblement e passant pas un .yml ou.toml)
  std::string getTodayFilePath(); // recupere le cheminf complet vers le fichier d'aujourdhui
  bool addNewNote(char** note, int word_count, char* filePath); // ajoute la nouvelle note
  std::string displayUsage();
  void  displayText(std::string_view text, bool is_error=false);
} // namespace service

#endif
