import helpers.OSFunctions as osFunctions
import interfaces.MenuDijkstraInterfaces as menuDijkstraInterfaces 
import helpers.outputsSystem as outputsSystem
import time 
import  keyboard


class MenuDijkstra :
    def __init__(self)  :
        self.menuDijkstraInterfaces = menuDijkstraInterfaces.MenuDijkstraInterfaces()
    def showMainMenu(self):
        while(True):
            self.menuDijkstraInterfaces.showMainMenu()
            outputsSystem.sendMessage("Presione una de las opciones con el teclado para seleccionarlas")
            if keyboard.read_event().event_type == keyboard.KEY_DOWN:
                    if keyboard.is_pressed('1'):
                        osFunctions.print_with_delay("\n🔍 Iniciando proceso inicial de la creacion de la animación de Dijkstra...\n")
                        return '1'
                    elif keyboard.is_pressed('2'):
                        osFunctions.print_with_delay("\n🎲 Creando interfaz para la creacion de una nueva matriz \n")
                        return '2'
                    elif keyboard.is_pressed('3') :
                        osFunctions.clear_screen()
                        osFunctions.print_with_delay("\nEsta saliendo del sistema . . . \n")
                        self.menuDijkstraInterfaces.exitInterface()
                        return '3'
                    else :
                        outputsSystem.messageError("\nPor favor presione una opción válida.")
                        time.sleep(2)
            osFunctions.clear_screen()
