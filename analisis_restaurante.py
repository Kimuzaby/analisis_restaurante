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
    promotores = 0
    pasivos = 0 
    detractores = 0

    for i in restaurante["nps"]["recomendacion"]:
        if i >= 9:
            promotores += 1
        elif i >= 7:
            pasivos += 1
        else:
            detractores += 1

    total = promotores + pasivos + detractores
    porcentaje_promotores = round((promotores / total) * 100, 2)
    porcentaje_pasivos = round((pasivos / total) * 100, 2)
    porcentaje_detractores = round((detractores / total) * 100, 2)
    
    print(f"Promotores: {promotores} ({porcentaje_promotores}%)")
    print(f"Pasivos: {pasivos} ({porcentaje_pasivos}%)")
    print(f"Detractores: {detractores} ({porcentaje_detractores}%)")

reporte_11()


def reporte_12():
    suma = {}
    conteo = {}

    for i in range(len(restaurante["preferencias"]["comida"])):
        comida = restaurante["preferencias"]["comida"][i]
        satisfaccion = restaurante["experiencia"]["producto"][i]

        if comida in suma:
            suma[comida] += satisfaccion
            conteo[comida] += 1
        else:
            suma[comida] = satisfaccion
            conteo[comida] = 1

    mayor_promedio = 0
    mejor_comida = ""

    for comida in suma:
        promedio = suma[comida] / conteo[comida]
        if promedio > mayor_promedio:
            mayor_promedio = promedio
            mejor_comida = comida

    print(f"La comida con mejor experiencia es: {mejor_comida} ({mayor_promedio:.2f})")

reporte_12()


def reporte_13():
    suma = {}
    conteo = {}

    for i in range(len(restaurante["preferencias"]["comida"])):
        comida = restaurante["preferencias"]["comida"][i]
        satisfaccion = restaurante["experiencia"]["producto"][i]

        if comida in suma:
            suma[comida] += satisfaccion
            conteo[comida] += 1
        else:
            suma[comida] = satisfaccion
            conteo[comida] = 1

    menor_promedio = 100
    peor_comida = ""

    for comida in suma:
        promedio = suma[comida] / conteo[comida]
        if promedio < menor_promedio:
            menor_promedio = promedio
            peor_comida = comida

    print(f"La comida con peor experiencia es: {peor_comida} ({menor_promedio:.2f})")

reporte_13()


def reporte_14():
    suma = {"bajo": 0, "medio": 0, "alto": 0}
    conteo = {"bajo": 0, "medio": 0, "alto": 0}

    for i in range(len(restaurante["consumo"]["gasto"])):
        gasto = restaurante["consumo"]["gasto"][i]
        satisfaccion = restaurante["experiencia"]["producto"][i]

        if gasto <= 20:
            suma["bajo"] += satisfaccion
            conteo["bajo"] += 1
        elif gasto <= 50:
            suma["medio"] += satisfaccion
            conteo["medio"] += 1
        else:
            suma["alto"] += satisfaccion
            conteo["alto"] += 1

    print("Promedio de satisfacción por nivel de gasto")

    for categoria in suma:
        if conteo[categoria] > 0:
            promedio = suma[categoria] / conteo[categoria]
            print(f"{categoria}: {promedio:.2f}")

reporte_14()


def reporte_15():
    suma = {}
    conteo = {}

    for i in range(len(restaurante["preferencias"]["frecuencia"])):
        frecuencia = restaurante["preferencias"]["frecuencia"][i]
        satisfaccion = restaurante["experiencia"]["producto"][i]

        if frecuencia in suma:
            suma[frecuencia] += satisfaccion
            conteo[frecuencia] += 1
        else:
            suma[frecuencia] = satisfaccion
            conteo[frecuencia] = 1

    print("Promedio de satisfacción por frecuencia")

    for categoria in sorted(suma):
        if conteo[categoria] > 0:
            promedio = suma[categoria] / conteo[categoria]
            print(f"{categoria}: {promedio:.2f}")

reporte_15()


def reporte_16():
    pass


def reporte_17():
    pass


def reporte_18():
    pass


def reporte_19():
    pass


def reporte_20():
    pass
