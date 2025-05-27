import random

numeros = [random.randint(1, 100) for _ in range(10)]

pares = []
impares = []

# Separar números pares e impares
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

# Mostrar resultados
print("Lista original:")
print(numeros)

print("\nNúmeros pares:")
print(pares)

print("\nNúmeros impares:")
print(impares)