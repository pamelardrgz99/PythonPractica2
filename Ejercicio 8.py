numero = int(input("Ingrese un número entero no negativo: "))
if numero < 0:
    print("No definido para números negativos.")
else:
    factorial = 1
    # Calcular el factorial
    for i in range(2, numero + 1):
        factorial *= i
    # Mostrar el resultado
    print(factorial)