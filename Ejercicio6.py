# Crear la lista de numero
serie = []

a=0
b=1

# Generar la serie de Fibonacci hasta 50
while a <= 50:
    serie.append(a)
    c = a
    a = b
    b = c + b 


# Mostrar resultado
print("Serie de Fibonacci:", serie)