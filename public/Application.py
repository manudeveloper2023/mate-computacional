import algorithms.AlgorithmDijtskra as AlgorithmDijtskra
import structures.NetworkGraph as NetworkGraph 
import algorithms.RoadMatrix as RoadMatrix
import algorithms.AdjacencyMatrix as AdjacencyMatrix
import helpers.OSFunctions as OSFunctions
import helpers.CompressedPathForDijkstra as compressedPathForDiklstra
import structures.MenuMatrix as menuMatrix 
import helpers.ShowTitle as showTitle
import structures.MenuDijkstra as menuDijkstra
import helpers.outputsSystem as outputsSystem
import time 
class Application:
    def __init__(self):
        showTitle.show_title()
        self.adjacencyMatrix = None
        self.algorithmDijkstra = None
        self.roadMatrix = None
        self.networkGraph = None
        self.menuMatrix = menuMatrix.MenuMatrix()
        self.menuDijkstra = menuDijkstra.MenuDijkstra()
        self.initializeMatrix()
    def initializeMatrix(self):
        OSFunctions.clear_screen()
        matrixSize = self.menuMatrix.getMatrixSize()
        self.adjacencyMatrix = AdjacencyMatrix.AdjacencyMatrix(matrixSize)
        OSFunctions.clear_screen()
        self.adjacencyMatrix.generateMatrix(self.menuMatrix.getTypeMatrix(matrixSize))
        OSFunctions.pause() 
        self.algorithmDijkstra = AlgorithmDijtskra.AlgorithmDijstkra(self.adjacencyMatrix.getEdges())
        self.roadMatrix = RoadMatrix.RoadMatrix(self.adjacencyMatrix.getAdjacencyMatrix())
        self.networkGraph = NetworkGraph.NetworkGraph(self.adjacencyMatrix.getEdges(), self.adjacencyMatrix.getMatrixSize())


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
                self.roadMatrix.availableRoutes()
                outputsSystem.sendMessage("Ingrese el nodo inicial del grafo: ")
                start_path = int(input()) 
                if not (0 <= start_path < self.adjacencyMatrix.getMatrixSize()):
                    outputsSystem.messageError(f"El nodo inicial {start_path} no existe en la matriz de adyacencia.")
                    time.sleep(1)
                    continue
                outputsSystem.sendMessage("Ingrese el nodo final del grafo: ")
                end_path = int(input())
                if not (0 <= end_path < self.adjacencyMatrix.getMatrixSize()):
                    outputsSystem.messageError(f"El nodo final {end_path} no existe en la matriz de adyacencia.")
                    time.sleep(1)
                    continue
                if start_path == end_path:
                    outputsSystem.messageError("Los nodos insertados son iguales")
                    time.sleep(1)
                    continue
                if not self.roadMatrix.existsRouteMap(start_path, end_path):
                    outputsSystem.messageError(f"No existe una ruta entre el nodo {start_path} y el nodo {end_path}.")
                    time.sleep(1)
                    continue
                outputsSystem.messageSuccess("Ha agregado los nodos exitosamente")
                OSFunctions.print_with_delay(f"Iniciando proceso de la animación de la busqueda de la ruta más corta desde {start_path} hasta {end_path}" , 0.01)
                time.sleep(1)
                OSFunctions.clear_screen()
                return start_path, end_path
            except ValueError:
               outputsSystem.messageError("Por favor, ingrese un número válido.")
               time.sleep(1)

    def showMenu(self):
        while True:
                OSFunctions.clear_screen()
                choice = self.menuDijkstra.showMainMenu()
                if choice == '1':
                    self.createAnimationDijstkra()
                elif choice == '2':
                    self.initializeMatrix()
                elif choice == '3':
                    break
                

    def init(self):
        self.showMenu()