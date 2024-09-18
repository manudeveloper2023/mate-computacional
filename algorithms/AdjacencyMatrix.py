import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt

class AdjacencyMatrix:
    def __init__(self , matrixSize):
        self.matrix = [[]]
        self.edges = []
        self.matrixSize = matrixSize
    def generateMatrix(self):
        self.matrix = np.random.randint(0,2, size=(self.matrixSize,self.matrixSize))
        for i in range(self.matrixSize):
            for j in range(i,self.matrixSize):
                if(self.matrix[i][j] or i==j):
                    weight = np.random.randint(1,21)
                    self.matrix[i][j] = self.matrix[j][i]  = weight
                    if (i!=j):
                        self.edges.append((i , j , weight))
    def getAdjacencyMatrix(self):return self.matrix
    def visualizeAdjacencyMatrix(self):
        max_width = max(len(str(num)) for row in self.matrix for num in row)
        print("    " + " ".join(f"{i:^{max_width}}" for i in range(self.matrixSize)))
        print("  +" + "-" * (self.matrixSize * (max_width + 1) + 1))
        for i, row in enumerate(self.matrix):
            print(f"{i:2d}|", end=" ")
            for num in row:
                if num == 0:
                    print(f"\033[90m{num:^{max_width}}\033[0m", end=" ")  
                else:
                    print(f"{num:^{max_width}}", end=" ")  
            print("|")
        print("  +" + "-" * (self.matrixSize * (max_width + 1) + 1))
    def getAdjacencyMatrixForNetworkx(self):
        matrixForNetworkx= self.matrix
        np.fill_diagonal(matrixForNetworkx, 0)
        return matrixForNetworkx
    def getEdges(self):return self.edges
    def getMatrixSize(self): return self.matrixSize
