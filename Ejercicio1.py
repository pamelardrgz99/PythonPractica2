result = []

for num in range(1500, 2700):

    if num % 7 == 0 and num % 5 == 0:
        result.append(num)

# Mostrar los resultados
print(result)