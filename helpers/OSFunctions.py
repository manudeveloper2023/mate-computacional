import os 
import time

def clear_screen():
        if os.name == 'nt':  
            os.system('cls')
        else: 
            os.system('clear')
def pause():
        input("\nPresione Enter para continuar...")
def print_with_delay(text: str, delay: float = 0.03):
  
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
def loadGif(path):
    return os.path.abspath(path)