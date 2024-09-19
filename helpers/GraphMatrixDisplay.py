def displayRoadMatrix(matrix, matrixSize):
    cell_width = 3  
    total_width = matrixSize * cell_width + 3 
    print("    ", end="")  
    for i in range(matrixSize):
        print(f"{i:2d}", end=" ") 
    print()
    print("  +" + "-" * (total_width - 2)) 
    for i, row in enumerate(matrix):
        print(f"{i:2d}|", end=" ")
        for num in row:
            print(f"{num:2d}", end=" ")  
        print("|")
    print("  +" + "-" * (total_width - 2)) 
def displayAdjacencyMatrix(matrix, matrixSize):
    max_width = max(len(str(num)) for row in matrix for num in row)
    print("    " + " ".join(f"{i:^{max_width}}" for i in range(matrixSize)))
    print("  +" + "-" * (matrixSize * (max_width + 1) + 1))
    for i, row in enumerate(matrix):
        print(f"{i:2d}|", end=" ")
        for num in row:
            if num == 0:
                print(f"\033[90m{num:^{max_width}}\033[0m", end=" ")  
            else:
                print(f"{num:^{max_width}}", end=" ")  
        print("|")
    print("  +" + "-" * (matrixSize * (max_width + 1) + 1))     
