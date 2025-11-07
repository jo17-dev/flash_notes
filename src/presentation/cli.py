from helpers.constantes import CLI_PARAMS
from model.file_access import FileManager
import sys

def display_help():
    print("----- allowed params -----")

    for item in CLI_PARAMS:
        if(item == ""):
            print("*  no params")
        else:
            print(f"*   {item}")
    print("---- Done by jo17-dev -----")
    print("---- Hope it helped -----")
    

def ajouter_note_cli(arg: list):
    if(len(arg) == 1):
        print("No note given")
    else:
        file_path = FileManager().add_note(" ".join(arg[1:]), is_editor_mode=False)
        print(f"saved at {file_path} ")
        sys.exit(0)

def ajouter_note_editeur(arg: list):
    file_path = FileManager().add_note(is_editor_mode=False)
    print(f"saved at {file_path} ")
    sys.exit(0)



def edit_note_editeur(arg: list):
    print("Option -ef : editer en mode fichier non pris en compte")
    print(arg)

def afficher_note_cli(arg: list):
    print("Option -s : afficher en mode cli les notes d'aujourdhui non pris en compte")
    print(arg)


def mauvais_params():
    print("Bad params")