import networkx as nx 

class NetworkNode :
    def __init__(self , node_size , position_node , graph , font_size):
        self.graph = graph 
        self.position_node = position_node
        self.node_size = node_size
        self.font_size = font_size
        self.node_colors = {edge: 'red' for edge in self.graph.nodes()}
    def drawNode(self, ax, node_colors=None):
        nx.draw_networkx_nodes(self.graph, self.position_node, ax=ax, node_size=self.node_size, node_color=node_colors)
    def drawNodeLabels(self, ax):
        nx.draw_networkx_labels(self.graph, self.position_node, ax=ax, font_size=self.font_size)
    def updateNodeColor(self, node, color):
        if node in self.node_colors:
            self.node_colors[node] = color
        

    