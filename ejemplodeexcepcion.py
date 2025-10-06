

def excepciones_creativas():
    # 1.1 ZeroDivisionError - Cantidad de comida por animal
    try:
        print("1.1 ZeroDivisionError - Calcular comida por animal")
        total_comida = 50  # kilos de comida
        cantidad_animales = 0  # no hay animales en la jaula
        comida_por_animal = total_comida / cantidad_animales
    except ZeroDivisionError:
        print("Error: No se puede dividir la comida si no hay animales en la jaula\n")
    
    # 1.2 IndexError - Asignar asiento a estudiante
    try:
        print("1.2 IndexError - Asignar asiento en clase")
        asientos = ["A1", "A2", "A3"]
        estudiante = asientos[5]  # se pide un asiento que no existe
    except IndexError:
        print("Error: El asiento que se pidió no existe en la clase\n")
    
    # 1.3 FileNotFoundError - Leer lista de inventario
    try:
        print("1.3 FileNotFoundError - Leer lista de inventario del zoológico")
        with open("inventario_animales.txt", "r") as f:
            datos = f.read()
    except FileNotFoundError:
        print("Error: El archivo de inventario no se encuentra\n")


# Ejecutar función
excepciones_creativas()




