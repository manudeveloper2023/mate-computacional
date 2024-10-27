import numpy as np 
import helpers.GraphMatrixDisplay as GraphMatrixDisplay 
import helpers.outputsSystem as outputsSystem
import helpers.OSFunctions as OsFunctions
import time
class AdjacencyMatrix:
    def __init__(self , matrixSize):
        self.matrix = [[]]
        self.edges = []
        self.matrixSize = matrixSize
    def generateMatrix(self , type):
        if type == "random":
            self.generateMatrixRandom()
        elif type == "manual":
            self.generateMatrixManual()
        else:
            raise ValueError("Tipo de matriz no reconocido. Usa 'random' o 'manual'.")
    def generateMatrixRandom(self):
        self.matrix = np.zeros((self.matrixSize, self.matrixSize), dtype=int)
        for i in range(self.matrixSize):
            for j in range(i,self.matrixSize):
                if(np.random.randint(0, 2) or i==j):
                    weight = np.random.randint(1,21)
                    self.matrix[i][j] = self.matrix[j][i]  = weight
                    if (i!=j):
                        self.edges.append((i , j , weight))
        self.visualizeAdjacencyMatrix()
        outputsSystem.messageSuccess("Ha creado la matriz de adyacencia con exito!")
        time.sleep(2)
    def generateMatrixManual(self):
        self.matrix =  np.zeros((self.matrixSize,self.matrixSize), dtype=int)
        outputsSystem.sendMessage("Introduce los valores para la matriz de adyacencia:")
        for i in range(self.matrixSize):
            for j in range(i, self.matrixSize):
                    while True:
                        try:
                            self.visualizeAdjacencyMatrix()
                            weight = int(input(f"Introduce el peso para la arista ({i}, {j}): "))
                            if weight < 0:
                                outputsSystem.messageError("El peso debe ser un número entero no negativo.")
                                time.sleep(1)
                            
                            self.matrix[i][j] = self.matrix[j][i] = weight
                            if weight > 0 and i!=j:
                                self.edges.append((i, j, weight))
                            OsFunctions.clear_screen()
                            break
                        except ValueError as e:
                            outputsSystem.messageError("El peso debe ser un número entero no negativo.")
                            time.sleep(1)
        OsFunctions.clear_screen()
        self.visualizeAdjacencyMatrix()
        outputsSystem.messageSuccess("Ha creado la matriz de adyacencia con exito!")
        time.sleep(2)
        
    def getAdjacencyMatrix(self):return self.matrix
    def visualizeAdjacencyMatrix(self): 
        outputsSystem.sendMessage("Matriz de Adyacencia\n")
        GraphMatrixDisplay.displayAdjacencyMatrix(self.matrix , self.matrixSize)
    def getEdges(self):return self.edges
    def getMatrixSize(self): return self.matrixSize
