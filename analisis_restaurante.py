import csv

restaurante = encuestado = {
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
with open("encuestas_restaurantes.csv", "r") as encuestas:
    datos_restaurante = csv.DictReader(encuestas)


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
