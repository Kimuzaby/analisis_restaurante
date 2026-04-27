"""Report 14: Analysis of satisfaction by spending category."""
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
#Reporte 14
def reporte_14():
    suma = {"consumo bajo": 0, "consumo medio": 0, "consumo alto": 0}
    conteo = {"consumo bajo": 0, "consumo medio": 0, "consumo alto": 0}
    for i in range(len(restaurante["consumo"]["gasto"])):
        gasto = restaurante["consumo"]["gasto"][i]
        satisfaccion = restaurante["experiencia"]["producto"][i]
       
        if gasto <= 20:
            suma["consumo bajo"] += satisfaccion
            conteo["consumo bajo"] += 1
        elif gasto <= 50:
            suma["consumo medio"] += satisfaccion
            conteo["consumo medio"] += 1
        else:
            suma["consumo alto"] += satisfaccion
            conteo["consumo alto"] += 1
    mayor_promedio = 0
    mejor_categoria = ""
    for categoria, valor in suma.items():
        if conteo[categoria] > 0:
            promedio = valor / conteo[categoria]
            if promedio > mayor_promedio:
                mayor_promedio = promedio
                mejor_categoria = categoria
    print(f"La categoría con mayor satisfacción es: {mejor_categoria} con un promedio de {mayor_promedio:.2f}")

reporte_14()
   