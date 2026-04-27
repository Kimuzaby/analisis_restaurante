import csv

# Diccionario princiapal 
restaurante = {
    "id": [],
    "preferencias": {"comida": [], "frecuencia": []},
    "consumo": {"gasto": []},
    "experiencia": {
        "producto": [],
        "servicio": [],
        "tiempo": [],
        "precio": [],
    },
    "nps": {
        "recomendacion": [],
        "volveria": [],
        "general": [],
    },
}

# CSV
with open("encuesta_restaurantes_10000.csv", "r", encoding="utf-8") as encuestas:
    datos_restaurante = csv.DictReader(encuestas)

    for valor in datos_restaurante:
        restaurante["id"].append(int(valor["id"]))
        restaurante["preferencias"]["comida"].append(valor["comida_preferida"])
        restaurante["preferencias"]["frecuencia"].append(valor["frecuencia_consumo"])
        restaurante["consumo"]["gasto"].append(float(valor["gasto_promedio"]))
        restaurante["experiencia"]["producto"].append(int(valor["satisfaccion_producto"]))
        restaurante["experiencia"]["servicio"].append(int(valor["satisfaccion_servicio"]))
        restaurante["experiencia"]["tiempo"].append(valor["tiempo_entrega"])
        restaurante["experiencia"]["precio"].append(valor["precio_percepcion"])
        restaurante["nps"]["recomendacion"].append(int(valor["recomendaria"]))
        restaurante["nps"]["volveria"].append(
            valor["volveria_comprar"].strip().lower() == "true"
        )
        restaurante["nps"]["general"].append(int(valor["calificacion_general"]))

# Reporte 1

def reporte_1():
    resultado = {"comida_preferida": {}}

    for comida in restaurante["preferencias"]["comida"]:
        if comida in resultado["comida_preferida"]:
            resultado["comida_preferida"][comida] += 1
        else:
            resultado["comida_preferida"][comida] = 1

    return resultado


# reporte 2

def reporte_2():
    resultado = {"frecuencia_consumo": {}}

    for frecuencia in restaurante["preferencias"]["frecuencia"]:
        if frecuencia in resultado["frecuencia_consumo"]:
            resultado["frecuencia_consumo"][frecuencia] += 1
        else:
            resultado["frecuencia_consumo"][frecuencia] = 1

    return resultado


# Reporte 3

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

# Reporte 4

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

# Reporte 5

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

