# Bucle While

import math 


# input

numero= int(input("Digite el numero: "))

# processing 

while numero<0:
    print("Error -> Deberia ser un numero positivo")
    numero= int(input("Digite el numero:  "))

print(f"\n  Su raiz cuadrada es {(math.sqrt(numero)):.2f}")
