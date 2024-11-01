import helpers.OSFunctions as osFunctions
class MenuMatrixInterfaces:
    def __init__(self):
        self.dimensionsShow = False  
        self.menuShow = False  

    def showDimenssionsMatrixInput(self):
        if not self.dimensionsShow:
            lines = [
                "╔═══════════════════════════════════════════════════════════════════════╗",
                "║                    DIMENSIONES DE LA MATRIZ                           ║",
                "╠═══════════════════════════════════════════════════════════════════════╣",
                "║                                                                       ║",
                "║     ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐             ║",
                "║     │ 8 x 8   │   │ 10 x 10 │   │ 12 x 12 │   │ 16 x 16 │             ║",
                "║     └─────────┘   └─────────┘   └─────────┘   └─────────┘             ║",
                "║                                                                       ║",
                "║     Ingrese un numero n donde: 8 <= n <= 16                           ║",
                "║                                                                       ║",
                "║     La matriz sera de dimensiones n x n                               ║",
                "║                                                                       ║",
                "╠═══════════════════════════════════════════════════════════════════════╣",
                "║                          EJEMPLO DE MATRIZ 8x8                        ║",
                "║                 ┌─────────────────────────────────┐                   ║",
                "║                 │ [1][2][3][4][5][6][7][8]        │                   ║",
                "║                 │ [*][*][*][*][*][*][*][*]        │                   ║",
                "║                 │ [*][*][*][*][*][*][*][*]        │                   ║",
                "║                 │ [*][*][*][*][*][*][*][*]        │                   ║",
                "║                 │ [*][*][*][*][*][*][*][*]        │                   ║",
                "║                 │ [*][*][*][*][*][*][*][*]        │                   ║",
                "║                 │ [*][*][*][*][*][*][*][*]        │                   ║",
                "║                 │ [*][*][*][*][*][*][*][*]        │                   ║",
                "║                 └─────────────────────────────────┘                   ║",
                "╚═══════════════════════════════════════════════════════════════════════╝"
            ]
            for line in lines:
                osFunctions.print_with_delay(line , 0.001)
            self.dimensionsShow = True  
        else : 
                print("""
            ╔═══════════════════════════════════════════════════════════════════════╗
            ║                    DIMENSIONES DE LA MATRIZ                           ║
            ╠═══════════════════════════════════════════════════════════════════════╣
            ║                                                                       ║
            ║     ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐             ║
            ║     │ 8 x 8   │   │ 10 x 10 │   │ 12 x 12 │   │ 16 x 16 │             ║
            ║     └─────────┘   └─────────┘   └─────────┘   └─────────┘             ║
            ║                                                                       ║
            ║     Ingrese un numero n donde: 8 <= n <= 16                           ║
            ║                                                                       ║
            ║     La matriz sera de dimensiones n x n                               ║
            ║                                                                       ║
            ╠═══════════════════════════════════════════════════════════════════════╣
            ║                          EJEMPLO DE MATRIZ 8x8                        ║
            ║                 ┌─────────────────────────────────┐                   ║
            ║                 │ [1][2][3][4][5][6][7][8]        │                   ║
            ║                 │ [*][*][*][*][*][*][*][*]        │                   ║
            ║                 │ [*][*][*][*][*][*][*][*]        │                   ║
            ║                 │ [*][*][*][*][*][*][*][*]        │                   ║
            ║                 │ [*][*][*][*][*][*][*][*]        │                   ║
            ║                 │ [*][*][*][*][*][*][*][*]        │                   ║
            ║                 │ [*][*][*][*][*][*][*][*]        │                   ║
            ║                 │ [*][*][*][*][*][*][*][*]        │                   ║
            ║                 └─────────────────────────────────┘                   ║
            ╚═══════════════════════════════════════════════════════════════════════╝
            """)

    def showMainMenu(self, matrixSize):
        if not self.menuShow:
            lines = [
                f"            ╔═══════════════════════════════════════════════════════════════════════╗",
                f"            ║                        SELECCIONA UNA OPCIÓN                          ║",
                f"            ║                     Tamaño de matriz: {matrixSize}x{matrixSize}                           ║",
                f"            ╠═══════════════════════════════════════════════════════════════════════╣",
                f"            ║  1. Ingresar Matriz Manualmente    │  2. Generar Matriz Aleatoria     ║",
                f"            ║     ┌─────────────────┐            │     ┌─────────────────┐          ║",
                f"            ║     │  [1][2][3]      │            │     │  [*][?][*]      │          ║",
                f"            ║     │  [4][5][6]      │            │     │  [?][*][?]      │          ║",
                f"            ║     │  [7][8][9]      │            │     │  [*][?][*]      │          ║",
                f"            ║     └─────────────────┘            │     └─────────────────┘          ║",
                f"            ╚═══════════════════════════════════════════════════════════════════════╝"
            ]
            for line in lines:
                osFunctions.print_with_delay(line , 0.001)
            self.menuShow = True 
        else:
              print(f"""
                ╔═══════════════════════════════════════════════════════════════════════╗
                ║                        SELECCIONA UNA OPCIÓN                          ║
                ║                     Tamaño de matriz: {matrixSize}x{matrixSize}                           ║
                ╠═══════════════════════════════════════════════════════════════════════╣
                ║  1. Ingresar Matriz Manualmente   │  2. Generar Matriz Aleatoria      ║
                ║     ┌─────────────────┐           │     ┌─────────────────┐           ║
                ║     │  [1][2][3]      │           │     │  [*][?][*]      │           ║
                ║     │  [4][5][6]      │           │     │  [?][*][?]      │           ║
                ║     │  [7][8][9]      │           │     │  [*][?][*]      │           ║
                ║     └─────────────────┘           │     └─────────────────┘           ║
                ╚═══════════════════════════════════════════════════════════════════════╝
                """)