# Ingresar cadena de texto
texto = input("Input: ")
#Mapear las vocales mayusculas y minusculas
vocales = "aeiouAEIOU"
# Crear una nueva cadena omitiendo las vocales
cadena_sin_vocales = ""

for caracter in texto:
  if caracter not in vocales:
        cadena_sin_vocales += caracter

# Resultado
print("Output:", cadena_sin_vocales)