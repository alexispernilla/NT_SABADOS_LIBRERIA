import random
from datetime import datetime, timedelta


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

        autores.append(autor)

    return autores
