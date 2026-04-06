#include <iostream>
#include <string>
#include <cstring>
#include <ctime>
#include <fstream>
#include <filesystem>
#include "../../include/Service/service.hpp"
#include <cstdlib>

namespace fs = std::filesystem;

using namespace std;
namespace service {
  void initializeConf() {}

  string getTodayFilePath() {
    const char* home = std::getenv("HOME");
    if (!home) {
      displayText(HOME_NOT_SET, true);
      exit(1);
    }
    string full_dir_path = string(home) + "/.flashnote";
    string_view DATA_DIR(full_dir_path);
    time_t timestamp = time(NULL);
    struct tm datetime = *localtime(&timestamp);
    fs::path todayFilePath = string(DATA_DIR) +
        "/year" + to_string(datetime.tm_year + 1900) + "/month" +
        ((datetime.tm_mon + 1) >= 10 ? to_string(datetime.tm_mon + 1)
                                     : "0" + to_string(datetime.tm_mon + 1)) +
        "/day" +
        (datetime.tm_mday >= 10 ? to_string(datetime.tm_mday)
                                : "0" + to_string(datetime.tm_mday)) +
        ".flashnote.md";

    // creation du dossier parent
    fs::create_directories(todayFilePath.parent_path());

    // creation du fichier
    std::ofstream(todayFilePath, ios::app).close();
    
    return string(todayFilePath);
  }

  bool addNewNote(char **note, int word_count ,char* filePath) {
    time_t timestamp = time(NULL);
    struct tm dt = *localtime(&timestamp);
    char date[50];
    strftime(date, 50, "%a, %B %e %Y - %H:%M", &dt);
    string header =
      "id=" + to_string(timestamp) + ";v=" + string(VERSION) + ";timestamp=" + date + "\n\n";

    string footer = "\n\n---\n\n";

    ofstream TargetFile(filePath, ios::app);
    
    if (!TargetFile) {
      displayText(ERROR_OPENING_FILE, true);
      return false;
    }
    
    TargetFile << header;
    for (int i = 0; i < word_count; i++) {
      TargetFile << *(note+i) << " ";
    }
    TargetFile << footer;
    TargetFile.close();
    string message = string(SAVED_TO) + filePath;
    displayText(message.c_str());
    return true;
  }

  string displayUsage() {
    return string(USAGE);
  }

  void displayText(string_view text, bool is_error) {
    cerr << (is_error ? "\033[0;31m" : "\033[34m" ) << text << "\033[0m" <<endl;
  }
} // namespace service
