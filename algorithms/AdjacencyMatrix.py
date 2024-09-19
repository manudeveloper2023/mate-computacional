import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt
import helpers.GraphMatrixDisplay as GraphMatrixDisplay 
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
        self.matrix = np.random.randint(0,2, size=(self.matrixSize,self.matrixSize))
        for i in range(self.matrixSize):
            for j in range(i,self.matrixSize):
                if(self.matrix[i][j] or i==j):
                    weight = np.random.randint(1,21)
                    self.matrix[i][j] = self.matrix[j][i]  = weight
                    if (i!=j):
                        self.edges.append((i , j , weight))
    def generateMatrixManual(self):
        self.matrix =  np.zeros((self.matrixSize,self.matrixSize), dtype=int)
        print("Introduce los valores para la matriz de adyacencia:")
        for i in range(self.matrixSize):
            for j in range(i, self.matrixSize):
                    while True:
                        try:
                            weight = int(input(f"Introduce el peso para la arista ({i}, {j}): "))
                            if weight < 0:
                                raise ValueError("El peso debe ser un número entero no negativo.")
                            
                            self.matrix[i][j] = self.matrix[j][i] = weight
                            if weight > 0 and i!=j:
                                self.edges.append((i, j, weight))
                            
                            break
                        except ValueError as e:
                            print(f"Entrada no válida. {e}")
        
    def getAdjacencyMatrix(self):return self.matrix
    def visualizeAdjacencyMatrix(self):
        print("Matriz de Adyacencia")
        GraphMatrixDisplay.displayAdjacencyMatrix(self.matrix , self.matrixSize)

    def getAdjacencyMatrixForNetworkx(self):
        matrixForNetworkx= self.matrix
        np.fill_diagonal(matrixForNetworkx, 0)
        return matrixForNetworkx
    def getEdges(self):return self.edges
    def getMatrixSize(self): return self.matrixSize
