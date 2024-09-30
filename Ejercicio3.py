#Crear lista de numeros
numeros = []

while True:
    # Preguntar si desea ingresar un número
    ingreso_numero = input("¿Desea ingresar un número? (SI/NO): ")
    if ingreso_numero == 'NO':
        break
    elif ingreso_numero == 'SI':
        # Solicitar al usuario que ingrese un número
        numero = int(input("Ingrese el número: "))
        # Agregar a la lista
        numeros.append(numero)
    else:
        print("Por favor, responda con 'SI' o 'NO'.")

# Empezando a contar numeros e impares
pares = 0
impares = 0

for numero in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

# Mostrar resultados
print(f"Números ingresados: {numeros}")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")