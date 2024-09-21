import networkx as nx
import matplotlib.pyplot as plt
import structures.NetworkNode as networkNode
import structures.NetworkEdge as networkEdge
import structures.AnimateGraphDijkstra as animateDijsktra
import helpers.OSFunctions as OSFunctions
import webbrowser
class NetworkGraph:
    def __init__(self, edges, size):
        self.graph = nx.Graph()
        self.size = size
        self.graph.add_weighted_edges_from(edges)
        self.position = nx.spring_layout(self.graph, k=3 , iterations=100)
        self.networkNode = self.choiceSizeNodes()
        self.networkEdge = networkEdge.NetworkEdge(graph=self.graph, position_edge=self.position, edge_width=1)
        self.fig, self.ax = plt.subplots(figsize=(15, 15))
        self.animateDijsktra = animateDijsktra.AnimateGraphDijkstra(networkEdge=self.networkEdge, networkNode=self.networkNode,
                                                    networkGraph=self)
    def drawGraph(self, node_colors=None, edge_colors=None):
        self.ax.clear()
        self.ax.axis('off')
        self.networkNode.drawNode(ax=self.ax, node_colors=node_colors)
        self.networkEdge.drawEdges(ax=self.ax, edge_colors=edge_colors)
        self.networkNode.drawNodeLabels(ax=self.ax)
        self.networkEdge.drawEdgesLabels(ax=self.ax)

    def choiceSizeNodes(self):
        if self.size > 12:
            return networkNode.NetworkNode(node_size=500, position_node=self.position, graph=self.graph, font_size=8)
        else:
            return networkNode.NetworkNode(node_size=1500, position_node=self.position, graph=self.graph, font_size=10)
        
    def drawDijsktraAnimate(self,path,   compressed_path, states , path_length):
        ani = self.animateDijsktra.animateDijkstra(path, compressed_path,  states , path_length ,  self.ax , self.fig )
        gif_path = OSFunctions.loadGif('output/dijkstra_animation.gif')
        webbrowser.open('file://' + gif_path)
        



    