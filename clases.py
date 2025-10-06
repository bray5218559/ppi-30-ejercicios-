# guardar_texto.py
# Programa simple para escribir texto y guardarlo en un archivo .txt

def escribir_texto():
    print("Escribe tu texto (termina con una línea que diga .fin):")
    lineas = []
    while True:
        linea = input()
        if linea.strip() == ".fin":
            break
        lineas.append(linea)
    return "\n".join(lineas)


def guardar_texto(texto):
    nombre = input("Nombre del archivo (sin extensión): ").strip()
    if not nombre:
        nombre = "mi_texto"
    nombre_archivo = nombre + ".txt"

    try:
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write(texto)
        print(f"\n✅ Archivo guardado como '{nombre_archivo}'")
    except Exception as e:
        print(f"❌ Error al guardar el archivo: {e}")


def main():
    texto = escribir_texto()

    if not texto.strip():
        print("No escribiste nada. Saliendo sin guardar.")
        return

    respuesta = input("¿Deseas guardar el texto? (s/n): ").strip().lower()
    if respuesta == "s":
        guardar_texto(texto)
    else:
        print("No se guardó el texto.")


if __name__ == "__main__":
    main()

