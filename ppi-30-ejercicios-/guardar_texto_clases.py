# guardar_texto_simple.py
# Programa MUY simple con clases para escribir y guardar texto

class Editor:
    def __init__(self):
        self.texto = ""

    def escribir(self):
        print("Escribe tu texto (termina con .fin):")
        lineas = []
        while True:
            linea = input()
            if linea.strip() == ".fin":
                break
            lineas.append(linea)
        self.texto = "\n".join(lineas)

    def guardar(self):
        nombre = input("Nombre del archivo: ").strip()
        if not nombre:
            nombre = "texto"
        with open(nombre + ".txt", "w", encoding="utf-8") as f:
            f.write(self.texto)
        print(f"✅ Guardado como {nombre}.txt")


editor = Editor()
editor.escribir()
if editor.texto.strip():
    editor.guardar()
else:
    print("No escribiste nada.")


