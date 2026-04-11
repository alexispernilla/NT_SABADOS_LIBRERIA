import os
import sys

import pandas as pd

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, "data")
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from utils.simulador_hu1autor import simular_autores
from utils.simulador_hu2libros import simular_libros


def guardar_simulacion(nombre, datos):
    os.makedirs(DATA_DIR, exist_ok=True)
    df = pd.DataFrame(datos)
    df.to_json(
        os.path.join(DATA_DIR, f"simulacion_{nombre}.json"),
        orient="records",
        indent=4,
    )
    df.to_csv(os.path.join(DATA_DIR, f"simulacion_{nombre}.csv"), index=False)


def main():
    autores_simulados = simular_autores(1000)
    libros_simulados = simular_libros(1000)

    guardar_simulacion("autores", autores_simulados)
    guardar_simulacion("libros", libros_simulados)

    print("Simulaciones generadas:")
    print(" - data/simulacion_autores.json")
    print(" - data/simulacion_autores.csv")
    print(" - data/simulacion_libros.json")
    print(" - data/simulacion_libros.csv")


if __name__ == "__main__":
    main()
