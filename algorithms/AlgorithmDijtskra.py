import networkx as nx
import heapq as heapriority_queue
import helpers.CreateGraphForDijstkra as createGraphForDijstkra
class AlgorithmDijstkra:
    def __init__(self, edges):
        self.graph = createGraphForDijstkra.createGraphFromEdgesInDijstkra(edges)
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
    
    