def createGraphFromEdgesInDijstkra(edges):
        graph = {}
        for node_1, node_2, weight in edges:
            if node_1 not in graph:
                graph[node_1] = []
            if node_2 not in graph:
                graph[node_2] = []
            graph[node_1].append((node_2, weight))
            graph[node_2].append((node_1, weight))
        return graph