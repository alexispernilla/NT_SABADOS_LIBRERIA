import os
import sys

import pandas as pd


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, "data")
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from notebook.limpieza_autores import limpiar_autores
from utils.simulador_hu1autor import simular_autores


def describir_autores(data_frame_limpio: pd.DataFrame) -> None:
    print("***Descripcion del dataset de autores***")
    print(f"numero de filas del dataset: {data_frame_limpio.shape[0]}")
    print(f"numero de columnas del dataset: {data_frame_limpio.shape[1]}")
    print(f"lista de columnas disponibles: {list(data_frame_limpio.columns)}")
    print(f"tipos de datos de cada atributo:\n{data_frame_limpio.dtypes}")

    print("\n***estadisticas de campos numericos***")
    columnas_numericas = ["id", "libros_publicados"]
    print(data_frame_limpio[columnas_numericas].describe())

    print("\n***conteos de columnas de interes***")
    print("conteo por nombre:")
    print(data_frame_limpio["nombre"].value_counts())
    print("\nconteo por codigo:")
    print(data_frame_limpio["codigo"].value_counts())
    print("\nconteo por nacionalidad:")
    print(data_frame_limpio["nacionalidad"].value_counts())

    print("\n***descripcion de fechas***")
    print(f"fecha de nacimiento mas antigua: {data_frame_limpio['fecha_nacimiento'].min()}")
    print(f"fecha de nacimiento mas reciente: {data_frame_limpio['fecha_nacimiento'].max()}")


def cargar_autores_limpios() -> pd.DataFrame:
    ruta_archivo = os.path.join(DATA_DIR, "simulacion_autores_limpia.csv")

    if os.path.exists(ruta_archivo):
        return pd.read_csv(ruta_archivo, parse_dates=["fecha_nacimiento"])

    autores_sucios = pd.DataFrame(simular_autores(1000))
    return limpiar_autores(autores_sucios)


if __name__ == "__main__":
    autores_limpios = cargar_autores_limpios()
    describir_autores(autores_limpios)
