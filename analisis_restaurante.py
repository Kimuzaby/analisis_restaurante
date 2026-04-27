import csv

restaurante = {
    "id": [],  # id son numeros, deberia ser usando con int()
    "preferencias": {"comida": [], "frecuencia": []},  # comida deberia ser una
    # lista de strings de comida
    # frecuencia deberia ser una lista de srrings de frecuence, ej: semanal, diario, etc
    "consumo": {"gasto": []},  # gasto deberia ser numeros float
    "experiencia": {
        "producto": [],  # producto deberia ser una lista de numeros
        "servicio": [],  # servicio deberia ser una lista de numeros
        "tiempo": [],  # tiempo deberia de ser una lista de strings, ej:"Rapido",
        # "Lento", "medio"
        "precio": [],  # precio deberia de ser una lista de strings, ej: "medio", "bajo"
    },
    "nps": {
        "recomendacion": [],  # recomendacion sera una lista de numeros
        "volveria": [],  # volveria deberia ser una lista de booleanos, ej: True, False
        "general": [],  # general deberia de ser una lista de numeros
    },
    #
}
with open("encuesta_restaurantes_10000.csv", "r") as encuestas:
    datos_restaurante = csv.DictReader(encuestas)
    # se llena el diccionario con el contenido de los datos del restaurante
    # lo valores van convertidos al formato esperado
    for valor in datos_restaurante:
        restaurante["id"].append(int(valor["id"]))
        restaurante["preferencias"]["comida"].append(valor["comida_preferida"])
        restaurante["preferencias"]["frecuencia"].append(valor["frecuencia_consumo"])
        restaurante["consumo"]["gasto"].append(float(valor["gasto_promedio"]))
        restaurante["experiencia"]["producto"].append(
            int(valor["satisfaccion_producto"])
        )
        restaurante["experiencia"]["servicio"].append(
            int(valor["satisfaccion_servicio"])
        )
        restaurante["experiencia"]["tiempo"].append(valor["tiempo_entrega"])
        restaurante["experiencia"]["precio"].append(valor["precio_percepcion"])
        restaurante["nps"]["recomendacion"].append(int(valor["recomendaria"]))
        restaurante["nps"]["volveria"].append(
            valor["volveria_comprar"].strip().lower() == "true"
        )
        restaurante["nps"]["general"].append(int(valor["calificacion_general"]))

"""
estructura esperada:
encuestado = { 
"id": 1, 
"preferencias": {
"comida": "Pizza", 
"frecuencia": "Semanal"
}, 
"consumo": {
"gasto": 50
},
"experiencia": { 
"producto": 8, 
"servicio": 7, 
"tiempo": "Rápido", 
"precio": "Medio" 
}, 
"nps": {
"recomendacion": 9,
"volveria": True,
"general": 8 
}
} 
"""


def reporte_1():
    pass


def reporte_2():
    pass


def reporte_3():
    pass


def reporte_4():
    pass


def reporte_5():
    pass


def reporte_6():
    pass


def reporte_7():
    pass


def reporte_8():
    pass


def reporte_9():
    pass


def reporte_10():
    pass


def reporte_11():
    pass


def reporte_12():
    pass


def reporte_13():
    pass


def reporte_14():
    pass


def reporte_15():
    pass

# Precio vs recomendación  
def reporte_16():
    print("\nReporte 16: Precio vs Recomendación")
    precios = restaurante["experiencia"]["precio"]
    recomendaciones = restaurante["nps"]["recomendacion"]

    # Agrupar las sumas y conteo de precios
    resumen = {}
    for precio, rec in zip(precios, recomendaciones):
        if precio not in resumen:
            resumen[precio] = {"suma": 0, "cantidad": 0}
        resumen[precio]["suma"] += rec
        resumen[precio]["cantidad"] += 1

    # Imprimir promedios
    for precio, datos in resumen.items():
        promedio = datos["suma"] / datos["cantidad"]
        print(f"Precio: {precio.capitalize():<10} | Promedio de Recomendación: {promedio:.2f} / 10")


# Tiempo de entrega vs satisfacción  
def reporte_17():
    print("\nReporte 17: Tiempo de Entrega vs Satisfacción General")
    tiempos = restaurante["experiencia"]["tiempo"]
    satisfaccion = restaurante["nps"]["general"]

    resumen = {}
    for tiempo, sat in zip(tiempos, satisfaccion):
        if tiempo not in resumen:
            resumen[tiempo] = {"suma": 0, "cantidad": 0}
        resumen[tiempo]["suma"] += sat
        resumen[tiempo]["cantidad"] += 1

    for tiempo, datos in resumen.items():
        promedio = datos["suma"] / datos["cantidad"]
        print(f"Tiempo de entrega: {tiempo.capitalize():<10} | Satisfacción General Promedio: {promedio:.2f} / 10")

# Ranking de comidas más consumidas  
def reporte_18():
    print("\nReporte 18: Ranking de Comidas Más Consumidas")
    comidas = restaurante["preferencias"]["comida"]

    # Contar cuántas veces se repite cada comida
    conteo = {}
    for comida in comidas:
        conteo[comida] = conteo.get(comida, 0) + 1

    # Ordenar el diccionario de mayor a menor según su cantidad
    ranking = sorted(conteo.items(), key=lambda x: x[1], reverse=True)

    for i, (comida, cantidad) in enumerate(ranking, 1):
        print(f"{i}. {comida:<15} | Consumida por: {cantidad} clientes")

# Promedio general por tipo de comida 
def reporte_19():
    print("\nReporte 19: Promedio General por Tipo de Comida")
    comidas = restaurante["preferencias"]["comida"]
    satisfaccion = restaurante["nps"]["general"]

    resumen = {}
    for comida, sat in zip(comidas, satisfaccion):
        if comida not in resumen:
            resumen[comida] = {"suma": 0, "cantidad": 0}
        resumen[comida]["suma"] += sat
        resumen[comida]["cantidad"] += 1

    promedios = []
    for comida, datos in resumen.items():
        promedio = datos["suma"] / datos["cantidad"]
        promedios.append((comida, promedio))

    # Ordenar por promedio más alto
    promedios.sort(key=lambda x: x[1], reverse=True)

    for comida, prom in promedios:
        print(f"Comida: {comida:<15} | Satisfacción General Promedio: {prom:.2f} / 10")

# Perfil del cliente promedio
def reporte_20():
    print("\nReporte 20: Perfil del Cliente Promedio")
    total_clientes = len(restaurante["id"])
    
    if total_clientes == 0:
        print("No hay datos cargados para analizar.")
        return

    # Funciones internas para no repetir código
    def calcular_promedio(lista):
        return sum(lista) / len(lista)

    def obtener_moda(lista):
        conteo = {}
        for item in lista:
            conteo[item] = conteo.get(item, 0) + 1
        # Obtener la llave con el valor más alto
        return max(conteo.items(), key=lambda x: x[1])[0]
