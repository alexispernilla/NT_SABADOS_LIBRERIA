import random
from datetime import datetime, timedelta


def ensuciar_libro(libro):
    probabilidad_error = random.random()

    if probabilidad_error < 0.15:
        libro["id"] = random.choice([None, 0, -1 * random.randint(1, 100)])
    elif probabilidad_error < 0.3:
        libro["titulo"] = random.choice(
            [
                "",
                f" {libro['titulo']} ",
                libro["titulo"].lower(),
            ]
        )
    elif probabilidad_error < 0.45:
        libro["codigo"] = random.choice(
            [
                libro["codigo"].lower(),
                libro["codigo"].replace("LB", "LIB-"),
                f" {libro['codigo']} ",
            ]
        )
    elif probabilidad_error < 0.6:
        libro["autor"] = random.choice([None, f" {libro['autor']} "])
    elif probabilidad_error < 0.75:
        libro["fecha_publicacion"] = None
    elif probabilidad_error < 0.9:
        libro["paginas"] = random.choice([None, 0, -1 * random.randint(1, 50), 5000])

    return libro


def simular_libros(numeroLibros):
    libros_base = [
        {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "codigo": "LB001"},
        {"titulo": "Delirio", "autor": "Laura Restrepo", "codigo": "LB002"},
        {"titulo": "La virgen de los sicarios", "autor": "Fernando Vallejo", "codigo": "LB003"},
        {"titulo": "Los informantes", "autor": "Juan Gabriel Vásquez", "codigo": "LB004"},
        {"titulo": "Rosario Tijeras", "autor": "Jorge Franco", "codigo": "LB005"},
        {"titulo": "El país de la canela", "autor": "William Ospina", "codigo": "LB006"},
        {"titulo": "La nieve del almirante", "autor": "Álvaro Mutis", "codigo": "LB007"}
    ]

    fechaInicial = datetime(1950, 1, 1)
    libros = []

    for i in range(numeroLibros):
        base = random.choice(libros_base)

        fechaSimulada = fechaInicial + timedelta(days=random.randint(0, 26000))

        libro = {
            "id": i + 1,
            "titulo": base["titulo"],
            "codigo": base["codigo"],
            "autor": base["autor"],
            "paginas": random.randint(100, 800),
            "fecha_publicacion": fechaSimulada.strftime("%Y-%m-%d")
        }

        libro = ensuciar_libro(libro)
        libros.append(libro)

    return libros
