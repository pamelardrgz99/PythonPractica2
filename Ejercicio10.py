# Crear lista de los meses
meses = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo",
    "Junio", "Julio", "Agosto", "Septiembre",
    "Octubre", "Noviembre", "Diciembre"
]

# Ingresar el input de la fecha
fecha = input("Ingrese una fecha (MM/DD/AAAA o Mes día, año): ")

# Asignar variables para el día, mes y año
dia = 0
mes = 0
anio = 0


if '/' in fecha:
    partes = fecha.split('/')
    mes = int(partes[0]) 
    dia = int(partes[1])  
    anio = int(partes[2])  
elif ',' in fecha:
    partes = fecha.split(' ')
    mes_nombre = partes[0] 
    dia = int(partes[1].replace(',', '')) 
    anio = int(partes[2])  
    
# Encontrar el número del mes correspondiente al nombre del mes
    if mes_nombre in meses:
        mes = meses.index(mes_nombre) + 1  
# Mostrar Resultado
print("Output:", f"{anio}-{mes:02}-{dia:02}" )