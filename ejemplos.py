

try:
    arch= open("hola.txt", "r")
    data = arch.read()
    print(data)
except IOError:
    print("Error al leer el archivo")
finally:
    arch.close()