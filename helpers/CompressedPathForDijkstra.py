def compressedPathForDijsktra(path) : 
    return [(path[i], path[i+1]) for i in range(len(path)-1)]