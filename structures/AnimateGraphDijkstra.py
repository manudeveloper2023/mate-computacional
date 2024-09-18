import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
class AnimateGraphDijkstra:
    def __init__(self , networkEdge , networkNode , networkGraph ,  graph)  :
        self.networkEdge = networkEdge 
        self.networkNode = networkNode
        self.networkGraph = networkGraph
        self.graph = graph 
    
    def animateDijkstra(self, path, states , ax , fig):
        path_edges = set(path)  
        path_nodes = set([node for edge in path for node in edge]) 
        extra_frames = 25

        def update(frame):
            self.choiceColorEdge(frame , states , path_edges , path_nodes)
            edge_colors = [self.networkEdge.edge_colors[edge] for edge in self.graph.edges()]
            node_colors = [self.networkNode.node_colors[node] for node in self.graph.nodes()]
            self.drawUpdateGraph(ax=ax , node_colors=node_colors , edge_colors= edge_colors , frame= frame ,states= states)
            self.refreshEdgesAndNodes()
        print("Camino final completado")
        ani = animation.FuncAnimation(
            fig,
            update,
            frames=len(states) + 1+extra_frames + 25,
            repeat=False,
            interval=200
        )
        ani.save('dijsktra_animation.gif', writer='pillow', fps=4)
        return ani
    
    def drawUpdateGraph(self , ax , node_colors , edge_colors , frame , states):
        ax.clear()
        self.networkGraph.drawGraph(node_colors= node_colors , edge_colors= edge_colors)
        ax.set_title(f"Paso {frame + 1}" if frame < len(states) else "Camino Final")

    def choiceColorEdge(self , frame , states , path_edges , path_nodes):
        if frame < len(states):
                for i in range(frame + 1):
                    edge = states[i]
                    self.networkEdge.updateEdgeColor(edge, 'red')
                    self.networkNode.updateNodeColor(edge[0], 'yellow')
                    print(f"Frame {i + 1}: Procesando arista {edge}")
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

    
    