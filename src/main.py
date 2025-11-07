# fichier pour handle toutes les commandes
from sys import argv
from helpers.constantes import CLI_PARAMS as allowed_params
from presentation.cli import display_help, ajouter_note_cli, ajouter_note_editeur, edit_note_editeur, afficher_note_cli, mauvais_params

if(len(argv) == 1):
    # cas sans parametre
    afficher_note_cli(argv)
else:
    match argv[1]:
        case "-a":
            ajouter_note_cli()
        case "-af":
            ajouter_note_editeur(argv[1:])
        case "-ef":
            edit_note_editeur(argv[1:])
        case "-s":
            afficher_note_cli(argv[1:])
        case "-sd":
            afficher_note_cli(argv[1:])
        case "--help":
            display_help()
        case _:
            mauvais_params()