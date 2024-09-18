import networkx as nx
import heapq as heapriority_queue

class AlgorithmDijstkra:
    def __init__(self, edges):
        self.edges = edges
        self.graph = self.createGraphFromEdges(self.edges)
        self.position = nx.spring_layout(self.graph)
        
    def algorithmDijkstra(self, start, target):
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        previous_nodes = {node: None for node in self.graph}
        priority_queue = [(0, start)]
        states = []
        visited = set()

        while priority_queue:
            current_distance, current_node = heapriority_queue.heappop(priority_queue)

            if current_node in visited:
                continue

            visited.add(current_node)
            

            if current_node == target:
                break

            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight
                states.append((current_node , neighbor))
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapriority_queue.heappush(priority_queue, (distance, neighbor))

        path = []
        current = target
        while current is not None:
            path.append(current)
            current = previous_nodes[current]
        path.reverse()

        if path[0] != start:
            return None, float('inf'), states 

        return path, distances[target], states
    
    def createGraphFromEdges(self , edges):
        graph = {}
        for node_1, node_2, weight in edges:
            if node_1 not in graph:
                graph[node_1] = []
            if node_2 not in graph:
                graph[node_2] = []
            graph[node_1].append((node_2, weight))
            graph[node_2].append((node_1, weight))
        return graph