import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tqdm import tqdm
import os
class AnimateGraphDijkstra:
    def __init__(self , networkEdge , networkNode , networkGraph ,  graph)  :
        self.networkEdge = networkEdge 
        self.networkNode = networkNode
        self.networkGraph = networkGraph
        self.graph = graph 
    
    def animateDijkstra(self, path , compressed_path, states ,path_length ,  ax , fig):
        fps_animation = 6 if len(states) > 60 else 4
        path_edges = set(compressed_path)  
        path_nodes = set([node for edge in compressed_path for node in edge]) 
        extra_frames = 10
        total_frames = len(states) + 1 + extra_frames
        pbar = tqdm(total=total_frames, desc="Procesando animación")
        def update(frame):
            pbar.update(1)
            self.choiceColorEdge(frame , states , path_edges , path_nodes)
            edge_colors = [self.networkEdge.edge_colors[edge] for edge in self.graph.edges()]
            node_colors = [self.networkNode.node_colors[node] for node in self.graph.nodes()]
            self.drawUpdateGraph(ax=ax , node_colors=node_colors , edge_colors= edge_colors)
            self.drawEdgeInGraph(ax , frame , states , path , path_length)
            self.refreshEdgesAndNodes()
        ani = animation.FuncAnimation(
            fig,
            update,
            frames=total_frames, 
            repeat=False,
            interval=200
        )
        self.createAnimation(ani , fps_animation)
        pbar.close()
        return ani
    def createAnimation(self , ani , fps_animation):
        if not os.path.exists('output'):
            os.makedirs('output')
        ani.save('output/dijkstra_animation.gif', writer='pillow', fps=fps_animation)
    def drawUpdateGraph(self , ax , node_colors , edge_colors):
        ax.clear()
        self.networkGraph.drawGraph(node_colors= node_colors , edge_colors= edge_colors)
    def drawEdgeInGraph(self , ax , frame , states ,path , path_length):
         ax.set_title(f"Paso {frame + 1} => Arista : {states[frame]}" if frame < len(states) else f"Camino Final =>{'->'.join(map(str, path))} : Peso : {path_length}")

    def choiceColorEdge(self , frame , states , path_edges , path_nodes):
        if frame < len(states):
                for i in range(frame + 1):
                    edge = states[i]
                    self.networkEdge.updateEdgeColor(edge, 'red')
                    self.networkNode.updateNodeColor(edge[0], 'yellow')
        else:
                
                for edge in path_edges:
                    self.networkEdge.updateEdgeColor(edge, "green")
                for node in path_nodes:
                    self.networkNode.updateNodeColor(node, "green")
                
    def refreshEdgesAndNodes(self):
        for edge in self.graph.edges():
                self.networkEdge.updateEdgeColor(edge, 'black')
        for node in self.graph.nodes():
            self.networkNode.updateNodeColor(node, 'lightgray')

    
    