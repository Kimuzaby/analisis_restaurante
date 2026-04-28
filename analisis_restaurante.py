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
    resultado = {"comida_preferida": {}}

    for comida in restaurante["preferencias"]["comida"]:
        if comida in resultado["comida_preferida"]:
            resultado["comida_preferida"][comida] += 1
        else:
            resultado["comida_preferida"][comida] = 1

    return resultado


def reporte_2():
    resultado = {"frecuencia_consumo": {}}

    for frecuencia in restaurante["preferencias"]["frecuencia"]:
        if frecuencia in resultado["frecuencia_consumo"]:
            resultado["frecuencia_consumo"][frecuencia] += 1
        else:
            resultado["frecuencia_consumo"][frecuencia] = 1

    return resultado



def reporte_3():
    datos = restaurante["consumo"]["gasto"]
    total = 0

    for gasto in datos:
        total += gasto

    resultado = {
        "gasto": {
            "total": total,
            "cantidad": len(datos),
            "promedio": total / len(datos),
        }
    }
    return resultado


def reporte_4():
    datos = restaurante["experiencia"]["producto"]
    total = 0

    for valor in datos:
        total += valor

    resultado = {
        "satisfaccion_producto": {
            "promedio": total / len(datos)
        }
    }

    return resultado


def reporte_5():
    datos = restaurante["experiencia"]["servicio"]
    total = 0

    for valor in datos:
        total += valor

    resultado = {
        "satisfaccion_servicio": {
            "promedio": total / len(datos)
        }
    }

    return resultado

# Resultados
print("REPORTE 1:", reporte_1())
print("REPORTE 2:", reporte_2())
print("REPORTE 3:", reporte_3())
print("REPORTE 4:", reporte_4())
print("REPORTE 5:", reporte_5())

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
    print("\n--- Reporte 20: Perfil del Cliente Promedio ---")
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

    # Cálculos estadísticos
    comida_favorita = obtener_moda(restaurante["preferencias"]["comida"])
    frecuencia_tip = obtener_moda(restaurante["preferencias"]["frecuencia"])
    gasto_prom = calcular_promedio(restaurante["consumo"]["gasto"])
    sat_producto_prom = calcular_promedio(restaurante["experiencia"]["producto"])
    sat_servicio_prom = calcular_promedio(restaurante["experiencia"]["servicio"])
    tiempo_tipico = obtener_moda(restaurante["experiencia"]["tiempo"])
    precio_tipico = obtener_moda(restaurante["experiencia"]["precio"])
    recomienda_prom = calcular_promedio(restaurante["nps"]["recomendacion"])
    porcentaje_retorno = (sum(restaurante["nps"]["volveria"]) / total_clientes) * 100

    # Imprimir el perfil final
    print(f"Comida Preferida             : {comida_favorita}")
    print(f"Frecuencia de Consumo Típica : {frecuencia_tip}")
    print(f"Gasto Promedio               : ${gasto_prom:.2f}")
    print(f"Tiempo de Entrega Común      : {tiempo_tipico}")
    print(f"Percepción de Precio Típica  : {precio_tipico}")
    print(f"Promedio Satisfacción Prod.  : {sat_producto_prom:.2f} / 10")
    print(f"Promedio Satisfacción Serv.  : {sat_servicio_prom:.2f} / 10")
    print(f"Promedio Recomendación (NPS) : {recomienda_prom:.2f} / 10")
    print(f"Probabilidad de Retorno      : {porcentaje_retorno:.1f}% de clientes")
reporte_20()
