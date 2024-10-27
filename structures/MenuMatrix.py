import helpers.OSFunctions as osFunctions
import interfaces.MenuMatrixInterfaces as menuMatrixInterfaces
import helpers.outputsSystem as outputsSystem
import time 
import  keyboard
class MenuMatrix : 
    
    def __init__(self):
        osFunctions.clear_screen()
        self.menuMatrixInterfaces = menuMatrixInterfaces.MenuMatrixInterfaces()
        osFunctions.clear_screen()
    
    def getMatrixSize(self):
        while True:
            try:
                self.menuMatrixInterfaces.showDimenssionsMatrixInput()
                outputsSystem.sendMessage("Ingresar el número de columnas y filas de la matriz A (8 <= n <= 16):")
                matrixSize= int(input())
                if 8 <= matrixSize <= 16:
                    outputsSystem.messageSuccess("Ha ingresado el número de la matriz correctamente")
                    time.sleep(1)
                    return matrixSize
                outputsSystem.messageError("El número debe estar entre 8 y 16. Intente nuevamente.")
                time.sleep(1)
                osFunctions.clear_screen()
            except ValueError:
                outputsSystem.messageError("Por favor ingrese un número válido.")
                time.sleep(1)
                osFunctions.clear_screen()
        
    def getTypeMatrix(self , matrixSize) :
        while(True):
            self.menuMatrixInterfaces.showMainMenu(matrixSize)
            outputsSystem.sendMessage("Presione 1 o 2 del teclado para seleccionar una de las opciones")
            if keyboard.read_event().event_type == keyboard.KEY_DOWN:
                if keyboard.is_pressed('1'):
                    osFunctions.print_with_delay("\n🔍 Ingresando matriz manualmente...\n")
                    osFunctions.clear_screen()
                    return 'manual'
                elif keyboard.is_pressed('2'):
                    osFunctions.print_with_delay("\n🎲 Generando matriz aleatoria...\n")
                    osFunctions.clear_screen()
                    return 'random'
                else :
                    outputsSystem.messageError("\nPor favor presione una opción válida.")
                    time.sleep(2)
            osFunctions.clear_screen()

