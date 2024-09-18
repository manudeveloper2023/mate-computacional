import networkx as nx 

class NetworkEdge:
    def __init__(self, graph, position_edge, edge_width=1, default_color='lightgray'):
        self.edge_width = edge_width
        self.graph = graph
        self.position_edge = position_edge
        self.edge_colors = {edge: default_color for edge in self.graph.edges()}

    def drawEdges(self, ax, edge_colors=None):
        nx.draw_networkx_edges(self.graph, self.position_edge, ax=ax, width=self.edge_width, edge_color=edge_colors)
    def drawEdgesLabels(self , ax):
        edge_labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, self.position_edge, ax=ax, edge_labels=edge_labels)
    def updateEdgeColor(self, edge, color):
        if edge in self.edge_colors:
            self.edge_colors[edge] = color
        elif (edge[1], edge[0]) in self.edge_colors:  
            self.edge_colors[(edge[1], edge[0])] = color