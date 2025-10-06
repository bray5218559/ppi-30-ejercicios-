
# Clase base
class Paleta:
    def __init__(self, sabor, precio):
        self.sabor = sabor
        self.precio = precio

# Subclase Paleta de Agua
class PaletaAgua(Paleta):
    def __init__(self, sabor, precio, baseAgua=True):
        super().__init__(sabor, precio)
        self.baseAgua = baseAgua

# Subclase Paleta de Crema
class PaletaCrema(Paleta):
    def __init__(self, sabor, precio):
        super().__init__(sabor, precio)

# Ejemplo
p1 = PaletaAgua("Limón", 15)
p2 = PaletaCrema("Chocolate", 20)

print(f"Paleta de {p1.sabor}, base de agua: {p1.baseAgua}, precio: ${p1.precio}")
print(f"Paleta de {p2.sabor}, precio: ${p2.precio}")


