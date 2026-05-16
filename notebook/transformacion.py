import pandas as pd


def transformar_autores(data_frame_limpio):
    # transformacion 1: autores con nacionalidad registrada
    filtro1 = data_frame_limpio.query('nacionalidad.notna()')

    # Agrupar por nacionalidad y contar autores
    agrupacion1 = filtro1.groupby('nacionalidad')['id'].count().reset_index()

    # transformacion 2: autores britanicos por apellido
    filtro2 = data_frame_limpio.query('nacionalidad == "britanico"')

    # Agrupar por apellido y contar autores
    agrupacion2 = filtro2.groupby('apellido')['id'].count().reset_index()

    # transformacion 3: autores latinoamericanos por nacionalidad
    filtro3 = data_frame_limpio.query('nacionalidad in ["argentino", "chileno", "colombiano", "peruano"]')

    # Agrupar por nacionalidad y contar autores latinoamericanos
    agrupacion3 = filtro3.groupby('nacionalidad')['id'].count().reset_index()

    agrupacion_resumen = {
        "agrupacion1": agrupacion1,
        "agrupacion2": agrupacion2,
        "agrupacion3": agrupacion3
    }

    return agrupacion_resumen


def transformar_libros(data_frame_limpio):
    # transformacion 1: libros disponibles
    filtro1 = data_frame_limpio.query('disponible == True')

    # Agrupar por editorial y sumar la cantidad de ejemplares
    agrupacion1 = filtro1.groupby('editorial')['cantidadEjemplares'].sum().reset_index()

    # transformacion 2: libros publicados desde 1990
    filtro2 = data_frame_limpio.query('anioPublicacion >= 1990')

    # Agrupar por anio y contar libros
    agrupacion2 = filtro2.groupby('anioPublicacion')['id'].count().reset_index()

    # transformacion 3: libros con autor registrado
    filtro3 = data_frame_limpio.query('autorNombre.notna()')

    # Agrupar por autor y contar libros
    agrupacion3 = filtro3.groupby('autorNombre')['id'].count().reset_index()

    # transformacion 4: libros disponibles con editorial registrada
    filtro4 = data_frame_limpio.query('disponible == True and editorial.notna()')

    # Agrupar por editorial y calcular el promedio de ejemplares
    agrupacion4 = filtro4.groupby('editorial')['cantidadEjemplares'].mean().reset_index()

    # transformacion 5: libros con categoria registrada
    filtro5 = data_frame_limpio.query('categoriaNombre.notna()')

    # Agrupar por categoria y contar libros
    agrupacion5 = filtro5.groupby('categoriaNombre')['id'].count().reset_index()

    agrupacion_resumen = {
        "agrupacion1": agrupacion1,
        "agrupacion2": agrupacion2,
        "agrupacion3": agrupacion3,
        "agrupacion4": agrupacion4,
        "agrupacion5": agrupacion5
    }

    return agrupacion_resumen
