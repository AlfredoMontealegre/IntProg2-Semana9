import os
import time
import random

participante = []
while True:
    os.system("cls||clear")
    os.system("color b0")
    nombre = input("Ingrese el nombre del participante (o 'fin' para terminar): ")
    if nombre.lower() == 'fin':
        break
    participante.append(nombre.upper())
  
os.system("cls||clear")
print("Participante agregado...")
print(f"{participante}")
print(f"Participantes Totales = {len(participante)}")

cont = 10
while cont > 0:
    os.system("cls||clear")
    print(cont)
    time.sleep(1)
    cont -= 1

os.system("cls||clear")
os.system("color a2")
fin = len(participante) - 1
ganador = random.randint(0, fin)
print(f"Ganador: {participante[ganador]}")