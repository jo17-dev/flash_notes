# fichier pour handle toutes les commandes
from sys import argv
from helpers.constantes import CLI_PARAMS as allowed_params
from presentation.cli import display_help

if(argv[1] not in allowed_params):
    print("Bad params")
    display_help()

