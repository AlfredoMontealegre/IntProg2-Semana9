numeros = [10, 21, 32, 43, 54, 65, 76, 87, 98, 109]

suma_par = 0
for i in range(0, len(numeros), 2):
    suma_par += numeros[i]

# Mostrar resultado
print("Lista de números:")
print(numeros)
print(f"\nSuma de elementos en posiciones pares: {suma_par}")