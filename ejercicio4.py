import math

class FiguraGeometrica:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def calcularArea(self):
        raise NotImplementedError("Este método debe ser sobrescrito en la subclase")


class Circulo(FiguraGeometrica):
    def __init__(self, radio: float):
        super().__init__("Círculo")
        self.radio = radio

    def calcularArea(self):
        return math.pi * (self.radio ** 2)


class Rectangulo(FiguraGeometrica):
    def __init__(self, base: float, altura: float):
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura


class Triangulo(FiguraGeometrica):
    def __init__(self, base: float, altura: float):
        super().__init__("Triángulo")
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return (self.base * self.altura) / 2


# --- Prueba ---
c = Circulo(5)
r = Rectangulo(4, 6)
t = Triangulo(3, 7)

print(f"Área del círculo: {c.calcularArea():.2f}")
print(f"Área del rectángulo: {r.calcularArea():.2f}")
print(f"Área del triángulo: {t.calcularArea():.2f}")




