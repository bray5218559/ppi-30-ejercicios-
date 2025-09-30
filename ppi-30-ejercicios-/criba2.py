def criba(n):
    primos = [True] * (n+1)
    primos[0] = primos[1] = False

    for i in range(2, int(n**0.5)+1):
        if primos[i]:
            print(f"\n → El número {i} es primo, ahora voy a eliminar sus múltiplos...")
            for j in range(2*i, n+1, i):
                if primos[j]:
                    print(f"   - Elimino {j} porque es múltiplo de {i}")
                primos[j] = False
        else:
            print(f" → El número {i} ya estaba eliminado, sigo con el siguiente.")

    return [x for x in range(n+1) if primos[x]]

def descomposicion_prima(n, primos):
    factores = []
    num = n
    for p in primos:
        while num % p == 0:
            factores.append(p)
            num //= p
        if num == 1:
            break
    return factores

num = int(input("Dame un número para verificar los números primos: "))
print("\nLos números primos desde 1 hasta", num, "son:")
primos = criba(num)
print(primos)

factores = descomposicion_prima(num, primos)

if len(factores) == 1 and factores[0] == num:
    print(f"\n El número {num} es primo y no tiene más factores que 1 y {num}.")
else:
    descomp = " * ".join(map(str, factores))
    print(f"\n Aplicando el Teorema Fundamental de la Aritmética:")
    print(f"   {num} = {descomp}")