import random
from datetime import datetime, timedelta


def ensuciar_autor(autor):
    probabilidad_error = random.random()

    if probabilidad_error < 0.15:
        autor["id"] = random.choice([None, 0, -1 * random.randint(1, 100)])
    elif probabilidad_error < 0.3:
        autor["nombre"] = random.choice(
            [
                "",
                f" {autor['nombre']} ",
                autor["nombre"].lower(),
            ]
        )
    elif probabilidad_error < 0.45:
        autor["codigo"] = random.choice(
            [
                autor["codigo"].lower(),
                autor["codigo"].replace("AU", "AUT-"),
                f" {autor['codigo']} ",
            ]
        )
    elif probabilidad_error < 0.6:
        autor["fecha_nacimiento"] = None
    elif probabilidad_error < 0.75:
        autor["libros_publicados"] = random.choice([None, -1 * random.randint(1, 10)])

    return autor


def simular_autores(numeroAutores):
    listaAutores = [
        "Gabriel García Márquez",
        "Laura Restrepo",
        "Fernando Vallejo",
        "Juan Gabriel Vásquez",
        "Jorge Franco",
        "William Ospina",
        "Álvaro Mutis"
    ]

    codigosAutores = ["AU001", "AU002", "AU003", "AU004", "AU005", "AU006", "AU007"]

    fechaInicial = datetime(1930, 1, 1)
    autores = []

    for _ in range(numeroAutores):
        fechaSimulada = fechaInicial + timedelta(days=random.randint(0, 30000))

        autor = {
            "id": random.randint(1, 5000),
            "nombre": random.choice(listaAutores),
            "codigo": random.choice(codigosAutores),
            "nacionalidad": "Colombiana",
            "libros_publicados": random.randint(1, 50),
            "fecha_nacimiento": fechaSimulada.strftime("%Y-%m-%d")
        }

        autor = ensuciar_autor(autor)
        autores.append(autor)

    return autores
