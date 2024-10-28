import numpy as np 
import helpers.GraphMatrixDisplay as GraphMatrixDisplay 
import helpers.outputsSystem as outputsSystem
class RoadMatrix:
    def __init__(self , matrix):
        self.road_matrix= self.transformMatrixBinary(matrix)
    def transformMatrixBinary(self , matrix):
        matrix = np.array(matrix)
        return (matrix != 0).astype(int)
    def algorithmRoadMatrix(self):
        for row in range(len(self.road_matrix)):
            for column in range(len(self.road_matrix[row])):
                if row != column:
                    if(self.road_matrix[row][column]):
                        for column_fill in range(len(self.road_matrix[row])):
                            if not self.road_matrix[row][column_fill] and self.road_matrix[column][column_fill]:
                                self.road_matrix[row][column_fill] = self.road_matrix[column][column_fill]


    def availableRoutes(self, target):
            routes = []
            for column in range(len(self.road_matrix[target])):
                if target!=column:routes.append(column) 
            print(f"El Nodo {target} tiene caminos para: {routes}")

    def visualizeRoadMatrix(self):
        outputsSystem.sendMessage("Matriz de Caminos")
        GraphMatrixDisplay.displayRoadMatrix(self.road_matrix , len(self.road_matrix[0]))
    def existsRouteMap(self , nodeA , nodeB):
        return self.road_matrix[nodeA][nodeB]
    def getRoadMatrix(self) : return self.road_matrix