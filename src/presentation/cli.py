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
    