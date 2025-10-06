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

num = int(input("Dame un número para verificar los números primos: "))

print("\n los números primos desde 1 hasta", num, "son:")
print(criba(num))
