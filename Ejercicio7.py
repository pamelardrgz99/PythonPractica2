#Crear lista de numeros
numeros_perfectos = []

for num in range(1, 1000):
    suma_divisores = 0 
    # Encontrar divisores propios
    for i in range(1, num):
        if num % i == 0:
            suma_divisores += i 
    # La suma de divisores propios tiene que ser igual al numero para que sea perfecto
    if suma_divisores == num:
        numeros_perfectos.append(num)
# Mostrar resultados
print( numeros_perfectos)