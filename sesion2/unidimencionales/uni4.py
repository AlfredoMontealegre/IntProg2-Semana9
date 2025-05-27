# Lista de palabras
palabras = ["manzana", "banana", "pera", "uva", "naranja", "sandía", "melón"]

# Mostrar la lista
print("Lista de palabras:")
print(palabras)

buscada = input("\nIngresa una palabra para buscar en la lista: ").lower()

if buscada in palabras:
    print(f"La palabra '{buscada}' SÍ está en la lista.")
else:
    print(f"La palabra '{buscada}' NO está en la lista.")