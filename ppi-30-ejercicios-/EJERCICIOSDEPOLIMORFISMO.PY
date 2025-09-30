class Paleta:
    def __init__(self, sabor: str, precio: float):
        self.sabor = sabor
        self.precio = precio

    def mostrarInfo(self):
        print(f"Paleta de {self.sabor}, precio: ${self.precio}")
        

class PaletaAgua(Paleta):
    def __init__(self, sabor: str, precio: float, baseAgua: bool = True):
        super().__init__(sabor, precio)
        self.baseAgua = baseAgua

    def mostrarInfo(self):  # Polimorfismo
        print(f"Paleta de agua sabor {self.sabor}, precio: ${self.precio}")


class PaletaCrema(Paleta):
    def __init__(self, sabor: str, precio: float, baseLeche: bool = True):
        super().__init__(sabor, precio)
        self.baseLeche = baseLeche

    def mostrarInfo(self):  # Polimorfismo
        print(f"Paleta de crema sabor {self.sabor}, precio: ${self.precio}")


# --- Polimorfismo ---
paletas = [
    PaletaAgua("Fresa", 15.0),
    PaletaCrema("Chocolate", 20.0)
]

for p in paletas:
    p.mostrarInfo()
