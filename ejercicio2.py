import os
os.system ("cls")

class Libro:
    def __init__(self, titulo, autor, precio):
        # Constructor que inicializa los atributos
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def mostrar_informaciones(self):
        # Método que muestra los datos del libro
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Precio: ${self.precio:.2f}")


# Ejemplo de uso:
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 350)
libro1.mostrar_informaciones()