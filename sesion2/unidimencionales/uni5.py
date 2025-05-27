numeros = [23, 67, 45, 89, 12, 54, 38, 90, 51, 47]

print("Lista de números:")
print(numeros)


contador = 0
for numero in numeros:
    if numero > 50:
        contador += 1

# Mostrar el resultado
print(f"\nCantidad de números mayores que 50: {contador}")