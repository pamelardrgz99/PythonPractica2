# Crear lista para los numeros
primos = []

for num in range(2, 100):
    # Inicializar un contador de divisores
    div = 0
    # Verificar si el número es divisible por algún número menor que él
    for i in range(1, num + 1):
        if num % i == 0:
            div += 1
    # Si tiene dos divisores es numero primo
    if div == 2:
        primos.append(num)

# Calcular la suma de los números primos
suma_primos = sum(primos)

# Mostrar el resultado
print(suma_primos)