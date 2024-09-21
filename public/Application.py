import algorithms.AlgorithmDijtskra as AlgorithmDijtskra
import structures.NetworkGraph as NetworkGraph 
import algorithms.RoadMatrix as RoadMatrix
import algorithms.AdjacencyMatrix as AdjacencyMatrix
import helpers.OSFunctions as OSFunctions
import helpers.CompressedPathForDijkstra as compressedPathForDiklstra
class Application:
    def __init__(self):
        self.adjacencyMatrix = None
        self.algorithmDijkstra = None
        self.roadMatrix = None
        self.networkGraph = None
        self.initializeMatrix()

    def initializeMatrix(self):
        OSFunctions.clear_screen()
        matrix_size = self.readSizeForMatrix()
        self.adjacencyMatrix = AdjacencyMatrix.AdjacencyMatrix(matrix_size)
        self.adjacencyMatrix.generateMatrix(self.showMenuMatrix())
        self.adjacencyMatrix.visualizeAdjacencyMatrix()
        OSFunctions.pause() 
        self.algorithmDijkstra = AlgorithmDijtskra.AlgorithmDijstkra(self.adjacencyMatrix.getEdges())
        self.roadMatrix = RoadMatrix.RoadMatrix(self.adjacencyMatrix.getAdjacencyMatrix())
        self.networkGraph = NetworkGraph.NetworkGraph(self.adjacencyMatrix.getEdges(), self.adjacencyMatrix.getMatrixSize())

    def showMenuMatrix(self):
        typeMatrix = ""
        while True:
            OSFunctions.clear_screen()
            try:    
                print("1. Ingresar Manualmente la Matriz")
                print("2. Generar Matriz Aleatoriamente")
                choice = int(input("Seleccione una opción: "))
                if choice == 1:
                    typeMatrix = "manual"
                    break
                elif choice == 2:
                    typeMatrix = "random"
                    break
                else:
                    print("Opción no válida. Por favor, intente de nuevo.")
                    OSFunctions.pause() 
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")
                OSFunctions.pause()  
        return typeMatrix

    def readSizeForMatrix(self):
        while True:
            try:
                OSFunctions.clear_screen()
                matrix_size = int(input("Ingresar el número de columnas y filas de la matriz A (8 <= n <= 16): "))
                if 8 <= matrix_size <= 16:
                    return matrix_size
                else:
                    print("Error: Ingrese un número dentro del rango 8 <= n <= 16.")
                    OSFunctions.pause()
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")
                OSFunctions.pause()  

    def createAnimationDijstkra(self):
        start_path, end_path = self.validateStartAndEndPathInDisjktra()
        path, path_length, states = self.algorithmDijkstra.algorithmDijkstra(start_path, end_path)
        compressed_path = compressedPathForDiklstra.compressedPathForDijsktra(path)
        self.networkGraph.drawDijsktraAnimate(path, compressed_path, states, path_length)

    def validateStartAndEndPathInDisjktra(self):
        while True:
            try:
                OSFunctions.clear_screen()
                self.roadMatrix.algorithmRoadMatrix()
                self.adjacencyMatrix.visualizeAdjacencyMatrix()
                self.roadMatrix.visualizeRoadMatrix()
                start_path = int(input("Ingrese el nodo inicial del grafo: ")) 
                if not (0 <= start_path < self.adjacencyMatrix.getMatrixSize()):
                    print(f"El nodo inicial {start_path} no existe en la matriz de adyacencia.")
                    OSFunctions.pause() 
                    continue
                end_path = int(input("Ingrese el nodo final del grafo: "))
                if not (0 <= end_path < self.adjacencyMatrix.getMatrixSize()):
                    print(f"El nodo final {end_path} no existe en la matriz de adyacencia.")
                    OSFunctions.pause()  
                    continue
                if start_path == end_path:
                    print("Los nodos insertados son iguales")
                    OSFunctions.pause()
                    continue
                if not self.roadMatrix.existsRouteMap(start_path, end_path):
                    print(f"No existe una ruta entre el nodo {start_path} y el nodo {end_path}.")
                    OSFunctions.pause() 
                    continue
                return start_path, end_path
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")
                OSFunctions.pause()  

    def showMenu(self):
        while True:
            try:
                OSFunctions.clear_screen()
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
                    OSFunctions.pause()  
                    break
                else:
                    print("Opción no válida. Por favor, intente de nuevo.")
                    OSFunctions.pause()  
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")
                OSFunctions.pause() 

    def init(self):
        self.showMenu()