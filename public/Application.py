import algorithms.AlgorithmDijtskra as AlgorithmDijtskra
import structures.NetworkGraph as NetworkGraph 
import algorithms.RoadMatrix as RoadMatrix
import algorithms.AdjacencyMatrix as AdjacencyMatrix

class Application:
    def __init__(self):
        self.adjacencyMatrix = None
        self.algorithmDijkstra = None
        self.roadMatrix = None
        self.networkGraph = None
        self.initializeMatrix()
        
    def initializeMatrix(self):
        matrix_size = self.readSizeForMatrix()
        self.adjacencyMatrix = AdjacencyMatrix.AdjacencyMatrix(matrix_size)
        self.adjacencyMatrix.generateMatrix()
        self.algorithmDijkstra = AlgorithmDijtskra.AlgorithmDijstkra(self.adjacencyMatrix.getEdges())
        self.roadMatrix = RoadMatrix.RoadMatrix(self.adjacencyMatrix.getAdjacencyMatrix())
        self.networkGraph = NetworkGraph.NetworkGraph(self.adjacencyMatrix.getEdges(), self.adjacencyMatrix.getMatrixSize())
    def readSizeForMatrix(self):
        matrix_size = int(input("Ingresar el número de columnas y filas de la matriz A (8 <= n <= 16): "))
        while matrix_size < 8 or matrix_size > 16:
            matrix_size = int(input("Ingresar un número válido: "))
        return matrix_size

    def createAnimationDijstkra(self):
        start_path, end_path = self.validateStartAndEndPathInDisjktra()
        path, path_length, states = self.algorithmDijkstra.algorithmDijkstra(start_path, end_path)
        print(path)
        compressed_path = [(path[i], path[i+1]) for i in range(len(path)-1)]
        self.networkGraph.drawDijsktraAnimate(compressed_path, states)

    def validateStartAndEndPathInDisjktra(self):
        while True:
            self.roadMatrix.algorithmRoadMatrix()
            print(self.adjacencyMatrix.visualizeAdjacencyMatrix())
            print(self.roadMatrix.getRoadMatrix())
            start_path = int(input("Ingrese el nodo inicial del grafo: ")) 
            end_path = int(input("Ingrese el nodo final del grafo: "))
            if not (0 <= start_path < self.adjacencyMatrix.getMatrixSize()):
                print(f"El nodo inicial {start_path} no existe en la matriz de adyacencia.")
                continue
            if not (0 <= end_path < self.adjacencyMatrix.getMatrixSize()):
                print(f"El nodo final {end_path} no existe en la matriz de adyacencia.")
                continue
            if not self.roadMatrix.existsRouteMap(start_path, end_path):
                print(f"No existe una ruta entre el nodo {start_path} y el nodo {end_path}.")
                continue
            return start_path, end_path

    def showMenu(self):
        while True:
            print("\nMenu:")
            print("1. Crear animación de Dijkstra")
            print("2. Ingresar nueva matriz")
            print("3. Salir")
            choice = input("Seleccione una opción: ")
            
            if choice == '1':
                self.createAnimationDijstkra()
            elif choice == '2':
                self.initializeMatrix()
            elif choice == '3':
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
    def init(self):
        self.showMenu()