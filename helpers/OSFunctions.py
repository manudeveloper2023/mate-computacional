import os 
def clear_screen():
        if os.name == 'nt':  
            os.system('cls')
        else: 
            os.system('clear')
def pause():
        input("\nPresione Enter para continuar...")
def loadGif(path):
    return os.path.abspath(path)