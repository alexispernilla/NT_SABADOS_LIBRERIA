import os
import sys

import pandas as pd

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, "data")
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from notebook.limpieza_libros import limpiar_libros

def describir_libros(data_frame_limpio: pd.DataFrame) -> None:
    if data_frame_limpio.empty:
        print("No hay datos para describir (DataFrame vacio).")
        return

    print("***Descripcion del dataset de libros***")
    print(f"numero de filas del dataset: {data_frame_limpio.shape[0]}")
    print(f"numero de columnas del dataset: {data_frame_limpio.shape[1]}")
    print(f"lista de columnas disponibles: {list(data_frame_limpio.columns)}")
    print(f"tipos de datos de cada atributo:\n{data_frame_limpio.dtypes}")

    print("\n***estadisticas de campos numericos***")
    columnas_numericas = ["id", "anioPublicacion", "cantidadEjemplares"]
    print(data_frame_limpio[columnas_numericas].describe())

    print("\n***conteos de columnas de interes***")
    print("conteo por titulo:")
    print(data_frame_limpio["titulo"].value_counts())
    print("\nconteo por editorial:")
    print(data_frame_limpio["editorial"].value_counts())
    print("\nconteo por disponibilidad:")
    print(data_frame_limpio["disponible"].value_counts())

if __name__ == "__main__":
    pass
