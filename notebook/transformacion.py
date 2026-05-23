import pandas as pd


def transformar_autores(data_frame_limpio):
    filtro1 = data_frame_limpio.query('nacionalidad.notna()')
    agrupacion1 = filtro1.groupby('nacionalidad')['id'].count().reset_index(name="conteo_autores")

    filtro2 = data_frame_limpio.query('nacionalidad == "britanico"')
    agrupacion2 = filtro2.groupby('apellido')['id'].count().reset_index(name="conteo_autores")

    filtro3 = data_frame_limpio.query('nacionalidad in ["argentino", "chileno", "colombiano", "peruano"]')
    agrupacion3 = filtro3.groupby('nacionalidad')['id'].count().reset_index(name="conteo_autores")

    agrupacion_resumen = {
        "agrupacion1": agrupacion1,
        "agrupacion2": agrupacion2,
        "agrupacion3": agrupacion3
    }

    return agrupacion_resumen


def transformar_libros(data_frame_limpio):
    filtro1 = data_frame_limpio.query('disponible == True')
    agrupacion1 = filtro1.groupby('editorial')['cantidadEjemplares'].sum().reset_index(name="total_ejemplares")

    filtro2 = data_frame_limpio.query('anioPublicacion >= 1990')
    agrupacion2 = filtro2.groupby('anioPublicacion')['id'].count().reset_index(name="conteo_libros")

    filtro3 = data_frame_limpio.query('autorNombre.notna()')
    agrupacion3 = filtro3.groupby('autorNombre')['id'].count().reset_index(name="conteo_libros")

    filtro4 = data_frame_limpio.query('disponible == True and editorial.notna()')
    agrupacion4 = filtro4.groupby('editorial')['cantidadEjemplares'].mean().reset_index(name="promedio_ejemplares")

    filtro5 = data_frame_limpio.query('categoriaNombre.notna()')
    agrupacion5 = filtro5.groupby('categoriaNombre')['id'].count().reset_index(name="conteo_libros")

    filtro6 = data_frame_limpio.query('categoriaNombre.notna() and editorial.notna()')
    agrupacion6 = filtro6.groupby(['categoriaNombre', 'editorial'])['id'].count().reset_index(name="conteo_libros")

    agrupacion_resumen = {
        "agrupacion1": agrupacion1,
        "agrupacion2": agrupacion2,
        "agrupacion3": agrupacion3,
        "agrupacion4": agrupacion4,
        "agrupacion5": agrupacion5,
        "agrupacion6": agrupacion6
    }

    return agrupacion_resumen
