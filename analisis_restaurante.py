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
separador_de_reportes = "------------------------------------------------------------------------------------------------------------"

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


# pasa por todas las filas de la columna experiencia tiempo, por cada coincidencia, se en
# 1 el contador del diccionario y se muestra el porcentaje
def reporte_6():
    print(separador_de_reportes)
    print("Reporte 6: distribucion del tiempo de entrega de pedidos")
    print(separador_de_reportes)
    tiempos_entrega = {"Rápido": 0, "Aceptable": 0, "Lento": 0}
    for conteo in restaurante["experiencia"]["tiempo"]:
        if conteo in tiempos_entrega:
            tiempos_entrega[conteo] += 1
    pedidos_rapido = tiempos_entrega["Rápido"]
    pedidos_aceptable = tiempos_entrega["Aceptable"]
    pedidos_lento = tiempos_entrega["Lento"]
    total_pedidos = pedidos_aceptable + pedidos_rapido + pedidos_lento
    porcentaje_pedidos_rapidos = (pedidos_rapido / total_pedidos) * 100
    porcentaje_pedidos_aceptables = (pedidos_aceptable / total_pedidos) * 100
    porcentaje_pedidos_lentos = (pedidos_lento / total_pedidos) * 100

    print(f"""
    total pedidos rapidos: {pedidos_rapido},
    total pedidos aceptables: {pedidos_aceptable},
    total pedidos lentos: {pedidos_lento}
    """)
    print(f"""
    porcentaje pedidos rapidos: {porcentaje_pedidos_rapidos}%,
    porcentaje pedidos aceptables: {porcentaje_pedidos_aceptables}%,
    porcentaje pedidos lentos: {porcentaje_pedidos_lentos}%
    """)
    print(separador_de_reportes)


reporte_6()


# por cada coincidencia con la percepcion de precios se aumenta el contador, se calcula
# el porcentaje
def reporte_7():
    print("Reporte 7: distribucion de percepcion de precios")
    print(separador_de_reportes)
    percepcion_precios = {"Alto": 0, "Medio": 0, "Bajo": 0}
    experiencia_precio = restaurante["experiencia"]["precio"]
    for conteo in experiencia_precio:
        if conteo in percepcion_precios:
            percepcion_precios[conteo] += 1
    percepcion_precios_alto = percepcion_precios["Alto"]
    percepcion_precios_medio = percepcion_precios["Medio"]
    percepcion_precios_bajo = percepcion_precios["Bajo"]
    total_percepciones = (
        percepcion_precios_alto + percepcion_precios_medio + percepcion_precios_bajo
    )
    porcentaje_precio_alto = (percepcion_precios_alto / total_percepciones) * 100
    porcentaje_precio_medio = (percepcion_precios_medio / total_percepciones) * 100
    porcentaje_precio_bajo = (percepcion_precios_bajo / total_percepciones) * 100
    print(f"""
    personas que persiven precios altos: {percepcion_precios_alto}, 
    personas que persiven precios medios: {percepcion_precios_medio},
    personas que persiven precios bajos: {percepcion_precios_bajo}
    """)
    print(f"""
    porcentaje de personas que persiven precios altos: {porcentaje_precio_alto}%,
    porcentaje de personas que persiven precios medios: {porcentaje_precio_medio}%,
    porcentaje de personas que persiven precios bajos: {porcentaje_precio_bajo}%
    """)
    print(separador_de_reportes)


reporte_7()


# suma todas las recomendaciones y las divide entre su longitud, a 2 decimales
def reporte_8():
    print("Reporte 8: promedio de satisfaccion general")
    print(separador_de_reportes)
    recomendacion = restaurante["nps"]["recomendacion"]
    # print(recomendacion)
    print(f"""
    promedio de satisfaccion general: {sum(recomendacion) / len(recomendacion):.2f}
    """)
    print(separador_de_reportes)


reporte_8()


# por cada coincidencia en los valores true y false se aumenta el contador y se muestran
# las estadisticas de total y porcentajes
def reporte_9():
    print("Reporte 9: porcentaje de clientes que volverian")
    print(separador_de_reportes)
    clientes_volverian = restaurante["nps"]["volveria"]
    volverian = {"si": 0, "no": 0}
    for valor in clientes_volverian:
        if valor == True:
            volverian["si"] += 1
        if valor == False:
            volverian["no"] += 1

    clientes_que_volverian = volverian["si"]
    clientes_que_no_volverian = volverian["no"]
    total = clientes_que_no_volverian + clientes_que_volverian
    porcentaje_volverian = (clientes_que_volverian / total) * 100
    porcentaje_no_volverian = (clientes_que_no_volverian / total) * 100
    print(f""" 
    cantidad de clientes que volverian: {clientes_que_volverian}
    cantidad de clientes que no volverian: {clientes_que_no_volverian}
    porcentaje de clientes que regresarian: {porcentaje_volverian:.2f}%
    porcentaje de clientes que no regresarian: {porcentaje_no_volverian:.2f}
    """)
    print(separador_de_reportes)


reporte_9()


# por cada recomendacion en el NPS se aumenta el contador, se aplica la formula:
# NPS = %promotores - %detractores
def reporte_10():
    print("Reporte 10:")
    print(separador_de_reportes)

    recomendacion = restaurante["nps"]["recomendacion"]
    total = len(recomendacion)

    conteo = {"promotores": 0, "pasivos": 0, "detractores": 0}

    for recomendados in recomendacion:
        if recomendados >= 9:
            conteo["promotores"] += 1
        elif recomendados >= 7:
            conteo["pasivos"] += 1
        else:
            conteo["detractores"] += 1

    porcentajes = {
        "promotores": (conteo["promotores"] / total) * 100,
        "pasivos": (conteo["pasivos"] / total) * 100,
        "detractores": (conteo["detractores"] / total) * 100,
    }

    nps = porcentajes["promotores"] - porcentajes["detractores"]

    print(f"""
    promedio de NPS: {nps}
    """)
    print(separador_de_reportes)


reporte_10()


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
