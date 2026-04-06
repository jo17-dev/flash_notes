#include <iostream>
#include "../include/Service/service.hpp"
#include <bits/stdc++.h>
using namespace std;
using namespace service;


int main(int argc, char *argv[]) {
  if (argc-1 == 0) { // no arg --> display usage
    cout << getTodayFilePath() << endl;
    return 0;
  }

  if (strcmp(argv[1], "--help") == 0 || strcmp(argv[1], "-h") == 0) { // --help || -h --> help
    cout << displayUsage() << endl;
  } else if (strcmp(argv[1], "-v") == 0 || strcmp(argv[1], "--version") == 0) {
    displayText("nf - flashnote version "+string(VERSION) + " " + string(VERSION_NAME));
  }else if (strcmp(argv[1], "-a") == 0) { // -a --> add
    if (argc - 2 == 0) {
      displayText(CANT_ADD_EMPTY_NOTE, true);
      return 1;
    }
    addNewNote(argv + 2, argc - 2, getTodayFilePath().data());
    return 0;
  } else { // bad arg
    displayText(BAD_CALL, true);
    return 1;
  }
}
