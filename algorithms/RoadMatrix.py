import numpy as np 
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
                            if not self.road_matrix[row][column_fill]:
                                self.road_matrix[row][column_fill] = self.road_matrix[column][column_fill]
        
    def existsRouteMap(self , nodeA , nodeB):
        return self.road_matrix[nodeA][nodeB]
    def getRoadMatrix(self) : return self.road_matrix