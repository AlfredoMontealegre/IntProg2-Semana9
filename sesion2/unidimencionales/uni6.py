numeros = []

print("Ingresa 10 números:")

# Pedir 10 números al usuario
for i in range(10):
    numero = int(input(f"Ingrese el número #{i + 1}: "))
    numeros.append(numero)

# Mostrar la lista original
print("\nLista original:")
print(numeros)

lista_invertida = numeros[::-1]

print("\nLista en orden inverso:")
print(lista_invertida)