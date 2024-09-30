#Crear lista para almacenar nombre de los alumnos
alumnos = []

# Ingresar la cantidad de alumnos
cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))

for i in range(cantidad_alumnos):
    # Ingresar el nombre del alumno
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
    
    # Crear lista para almacenar las notas
    notas = []
    
    # Solicitar las 3 calificaciones
    for j in range(3):
        nota = int(input(f"Ingrese la nota {j + 1} de {nombre}: "))
        notas.append(nota)
    
    # Crear un diccionario con los datos del alumno
    alumno = {
        "Alumno": nombre,
        "Notas": notas
    }
    
    # Agregar el diccionario a la lista de alumnos
    alumnos.append(alumno)

# Mostrar en pantalla el listado completo de los alumnos
print("\nCalificaciones por alumno:")
for alumno in alumnos:
    print(f"Alumno: {alumno['Alumno']},\nNotas: {alumno['Notas']}\n")