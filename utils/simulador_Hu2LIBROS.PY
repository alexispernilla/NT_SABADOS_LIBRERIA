import random
from datetime import datetime, timedelta

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
            "id": i + 1,  # ✅ ID único
            "titulo": base["titulo"],
            "codigo": base["codigo"],
            "autor": base["autor"],
            "paginas": random.randint(100, 800),
            "fecha_publicacion": fechaSimulada.strftime("%Y-%m-%d")
        }

        libros.append(libro)

    return libros


# Ejemplo
libros_simulados = simular_libros(5)
for libro in libros_simulados:
    print(libro)
    