import os
import sys
import pandas as pd

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from notebook.consumo_hu1_autores import consumir_api_autores
from notebook.limpieza_autores import limpiar_autores
from notebook.consumo_hu2_libros import consumir_api_libros
from notebook.limpieza_libros import limpiar_libros
from notebook.transformacion import transformar_autores, transformar_libros

# Lógica para Autores
datos_autores = consumir_api_autores()
data_frame_autores = pd.DataFrame(datos_autores)
data_frame_limpio_autores = limpiar_autores(data_frame_autores)

# Lógica para Libros
datos_libros = consumir_api_libros()
data_frame_libros = pd.DataFrame(datos_libros)
data_frame_limpio_libros = limpiar_libros(data_frame_libros)

agrupaciones_autores = transformar_autores(data_frame_limpio_autores)
agrupaciones_libros = transformar_libros(data_frame_limpio_libros)


print(agrupaciones_autores)

print(agrupaciones_libros)