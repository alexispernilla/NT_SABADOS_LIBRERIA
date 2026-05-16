import pandas as pd 

def transformar_autores(data_frame_limpio):
    # Transformacion 1: Cantidad de Autores por Nacionalidad
    # Filtramos para asegurarnos de no contar registros sin nacionalidad
    filtro1 = data_frame_limpio.query('nacionalidad != ""')
    agrupacion1 = filtro1.groupby('nacionalidad')['id'].count().reset_index()
    agrupacion1 = agrupacion1.rename(columns={'id': 'cantidad_autores'})
    agrupacion1 = agrupacion1.sort_values(by='cantidad_autores', ascending=False)

    # Transformacion 2: Conteo de Autores por Apellido (Top 10)
    # Filtramos los autores cuyo apellido no esté vacío
    filtro2 = data_frame_limpio.query('apellido != ""')
    agrupacion2 = filtro2.groupby('apellido')['id'].count().reset_index()
    agrupacion2 = agrupacion2.rename(columns={'id': 'cantidad_autores'})
    agrupacion2 = agrupacion2.sort_values(by='cantidad_autores', ascending=False).head(10)

    agrupacion_resumen = {
        "autores_por_nacionalidad": agrupacion1,
        "top_apellidos_autores": agrupacion2
    }

    return agrupacion_resumen

def transformar_libros(data_frame_limpio):
    # Transformacion 3: Total de Ejemplares Disponibles por Editorial
    # Filtramos únicamente los libros que están disponibles
    filtro3 = data_frame_limpio.query('disponible == True')
    agrupacion3 = filtro3.groupby('editorial')['cantidadEjemplares'].sum().reset_index()
    agrupacion3 = agrupacion3.rename(columns={'cantidadEjemplares': 'total_ejemplares'})
    agrupacion3 = agrupacion3.sort_values(by='total_ejemplares', ascending=False)

    # Transformacion 4: Tendencia de Publicación por Año (A partir del año 1900)
    # Filtramos libros publicados en 1900 o después para evitar valores atípicos históricos
    filtro4 = data_frame_limpio.query('anioPublicacion >= 1900')
    agrupacion4 = filtro4.groupby('anioPublicacion')['id'].count().reset_index()
    agrupacion4 = agrupacion4.rename(columns={'id': 'cantidad_libros_publicados'})
    agrupacion4 = agrupacion4.sort_values(by='anioPublicacion', ascending=True)

    # Transformacion 5: Promedio de Ejemplares por Editorial en Libros Recientes (Desde 2000)
    # Filtramos para enfocarnos en publicaciones contemporáneas y con ejemplares existentes
    filtro5 = data_frame_limpio.query('anioPublicacion >= 2000 and cantidadEjemplares > 0')
    agrupacion5 = filtro5.groupby('editorial')['cantidadEjemplares'].mean().reset_index()
    agrupacion5 = agrupacion5.rename(columns={'cantidadEjemplares': 'promedio_ejemplares'})
    agrupacion5 = agrupacion5.round(2).sort_values(by='promedio_ejemplares', ascending=False)

    agrupacion_resumen = {
        "ejemplares_disponibles_por_editorial": agrupacion3,
        "libros_publicados_por_anio": agrupacion4,
        "promedio_ejemplares_editorial_recientes": agrupacion5
    }

    return agrupacion_resumen