import os
import sys

import pandas as pd

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, "data")
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from notebook.limpieza_autores import limpiar_autores
from notebook.limpieza_libros import limpiar_libros
from notebook.descripcion_hu1_autores import describir_autores
from notebook.descripcion_hu2_libros import describir_libros
from utils.simulador_hu1autor import simular_autores
from utils.simulador_hu2libros import simular_libros


def guardar_simulacion(nombre, datos, sufijo=""):
    os.makedirs(DATA_DIR, exist_ok=True)
    df = datos if isinstance(datos, pd.DataFrame) else pd.DataFrame(datos)
    nombre_archivo = f"simulacion_{nombre}{sufijo}"
    df.to_json(
        os.path.join(DATA_DIR, f"{nombre_archivo}.json"),
        orient="records",
        indent=4,
        date_format="iso",
        force_ascii=False,
    )
    df.to_csv(os.path.join(DATA_DIR, f"{nombre_archivo}.csv"), index=False)


def procesar_simulacion(
    nombre, funcion_simulador, funcion_limpieza, cantidad_registros, funcion_descripcion=None
):
    simulaciones = funcion_simulador(cantidad_registros)
    simulaciones_ordenadas = pd.DataFrame(simulaciones)
    simulaciones_limpias = funcion_limpieza(simulaciones_ordenadas)

    guardar_simulacion(nombre, simulaciones_ordenadas)
    guardar_simulacion(nombre, simulaciones_limpias, "_limpia")

    if funcion_descripcion is not None:
        funcion_descripcion(simulaciones_limpias)

    return len(simulaciones_ordenadas), len(simulaciones_limpias)


def main():
    total_autores, total_autores_limpios = procesar_simulacion(
        "autores", simular_autores, limpiar_autores, 1000, describir_autores
    )
    total_libros, total_libros_limpios = procesar_simulacion(
        "libros", simular_libros, limpiar_libros, 1000, describir_libros
    )

    print("Simulaciones generadas:")
    print(" - data/simulacion_autores.json")
    print(" - data/simulacion_autores.csv")
    print(" - data/simulacion_autores_limpia.json")
    print(" - data/simulacion_autores_limpia.csv")
    print(" - data/simulacion_libros.json")
    print(" - data/simulacion_libros.csv")
    print(" - data/simulacion_libros_limpia.json")
    print(" - data/simulacion_libros_limpia.csv")
    print()
    print(f"Autores: {total_autores_limpios} registros limpios de {total_autores}")
    print(f"Libros: {total_libros_limpios} registros limpios de {total_libros}")


if __name__ == "__main__":
    main()
