import os
import sys

import pandas as pd

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from notebook.consumo_hu1_autores import consumir_api_autores
from notebook.consumo_hu2_libros import consumir_api_libros
from notebook.graficacion import graficar_agrupaciones_autores, graficar_agrupaciones_libros
from notebook.limpieza_autores import limpiar_autores
from notebook.limpieza_libros import limpiar_libros
from notebook.transformacion import transformar_autores, transformar_libros


def main():
    datos_autores = consumir_api_autores()
    data_frame_autores = pd.DataFrame(datos_autores)
    data_frame_limpio_autores = limpiar_autores(data_frame_autores)

    datos_libros = consumir_api_libros()
    data_frame_libros = pd.DataFrame(datos_libros)
    data_frame_limpio_libros = limpiar_libros(data_frame_libros)

    agrupaciones_autores = transformar_autores(data_frame_limpio_autores)
    agrupaciones_libros = transformar_libros(data_frame_limpio_libros)

    print("\n=== AGRUPACIONES DE AUTORES ===")
    print("\n1. Cantidad de autores por nacionalidad")
    print(agrupaciones_autores["agrupacion1"])

    print("\n2. Autores britanicos agrupados por apellido")
    print(agrupaciones_autores["agrupacion2"])

    print("\n3. Cantidad de autores latinoamericanos por nacionalidad")
    print(agrupaciones_autores["agrupacion3"])

    print("\n=== AGRUPACIONES DE LIBROS ===")
    print("\n1. Cantidad de ejemplares disponibles por editorial")
    print(agrupaciones_libros["agrupacion1"])

    print("\n2. Cantidad de libros publicados desde 1990 por anio")
    print(agrupaciones_libros["agrupacion2"])

    print("\n3. Cantidad de libros por autor")
    print(agrupaciones_libros["agrupacion3"])

    print("\n4. Promedio de ejemplares disponibles por editorial")
    print(agrupaciones_libros["agrupacion4"])

    print("\n5. Cantidad de libros por categoria")
    print(agrupaciones_libros["agrupacion5"])

    print("\n6. Cantidad de libros por categoria y editorial")
    print(agrupaciones_libros["agrupacion6"])

    print("\n=== GENERACION DE GRAFICOS ===")
    graficar_agrupaciones_autores(agrupaciones_autores)
    graficar_agrupaciones_libros(agrupaciones_libros)


if __name__ == "__main__":
    main()
