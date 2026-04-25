import os
import sys

import pandas as pd


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, "data")
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from notebook.limpieza_libros import limpiar_libros
from utils.simulador_hu2libros import simular_libros


def describir_libros(data_frame_limpio: pd.DataFrame) -> None:
    print("***Descripcion del dataset de libros***")
    print(f"numero de filas del dataset: {data_frame_limpio.shape[0]}")
    print(f"numero de columnas del dataset: {data_frame_limpio.shape[1]}")
    print(f"lista de columnas disponibles: {list(data_frame_limpio.columns)}")
    print(f"tipos de datos de cada atributo:\n{data_frame_limpio.dtypes}")

    print("\n***estadisticas de campos numericos***")
    columnas_numericas = ["id", "paginas"]
    print(data_frame_limpio[columnas_numericas].describe())

    print("\n***conteos de columnas de interes***")
    print("conteo por titulo:")
    print(data_frame_limpio["titulo"].value_counts())
    print("\nconteo por codigo:")
    print(data_frame_limpio["codigo"].value_counts())
    print("\nconteo por autor:")
    print(data_frame_limpio["autor"].value_counts())

    print("\n***descripcion de fechas***")
    print(f"fecha de publicacion mas antigua: {data_frame_limpio['fecha_publicacion'].min()}")
    print(f"fecha de publicacion mas reciente: {data_frame_limpio['fecha_publicacion'].max()}")


def cargar_libros_limpios() -> pd.DataFrame:
    ruta_archivo = os.path.join(DATA_DIR, "simulacion_libros_limpia.csv")

    if os.path.exists(ruta_archivo):
        return pd.read_csv(ruta_archivo, parse_dates=["fecha_publicacion"])

    libros_sucios = pd.DataFrame(simular_libros(1000))
    return limpiar_libros(libros_sucios)


if __name__ == "__main__":
    libros_limpios = cargar_libros_limpios()
    describir_libros(libros_limpios)
