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

        #Reporte12
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

    print(f"La comida con mejor experiencia es: {mejor_comida} con un promedio de: {mayor_promedio:.2f}")
reporte_12()