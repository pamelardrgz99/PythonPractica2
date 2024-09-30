# Crear la lista de numero
serie = []

a=0
b=1

# Generar la serie de Fibonacci hasta 50
while a <= 50:
    serie.append(a)
    a, b = b, a + b  

# Mostrar resultado
print("Serie de Fibonacci", serie)