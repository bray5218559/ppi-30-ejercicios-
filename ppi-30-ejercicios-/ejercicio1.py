
try:
    x = int(input("ingrese un numero:"))
    y = 10 / x

except ValueError:
    print("debes introducuir un numero valido.")
else:
    print(f"el numero es {x}")