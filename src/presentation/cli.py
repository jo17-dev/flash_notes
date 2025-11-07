from helpers.constantes import CLI_PARAMS

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
    print("Option -a : Ajouter une note:: " +arg)

def ajouter_note_editeur(arg: list):
    print("Option -af : Ajouter note en mode fichier")
    print(arg)


def edit_note_editeur(arg: list):
    print("Option -ef : editer en mode fichier")
    print(arg)

def afficher_note_cli(arg: list):
    print("Option -s : afficher en mode cli les notes d'aujourdhui")
    print(arg)
