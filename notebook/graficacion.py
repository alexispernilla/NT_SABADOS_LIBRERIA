import os

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import seaborn as sns


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA_GRAFICOS = os.path.join(ROOT_DIR, "data", "graficos")


def crear_ruta_si_no_existe(ruta_destino):
    os.makedirs(ruta_destino, exist_ok=True)


def datos_disponibles(datos_agrupados, titulo):
    if datos_agrupados.empty:
        print(f"No se genero {titulo}: no hay datos disponibles.")
        return False

    return True


def graficar_lineas(datos_agrupados, columna_eje_x, columna_eje_y,
                    titulo="Grafico de lineas", color_linea="#2196F3",
                    nombre_archivo="lineas.png", ruta_destino=RUTA_GRAFICOS):
    if not datos_disponibles(datos_agrupados, titulo):
        return

    crear_ruta_si_no_existe(ruta_destino)

    datos_ordenados = datos_agrupados.sort_values(by=columna_eje_x)
    figura, area_dibujo = plt.subplots(figsize=(10, 5))
    area_dibujo.plot(
        datos_ordenados[columna_eje_x],
        datos_ordenados[columna_eje_y],
        marker="o",
        color=color_linea,
        linewidth=2,
    )
    area_dibujo.set_title(titulo, fontsize=14)
    area_dibujo.set_xlabel(columna_eje_x, fontsize=12)
    area_dibujo.set_ylabel(columna_eje_y, fontsize=12)
    area_dibujo.grid(True, linestyle="--", alpha=0.6)
    plt.xticks(rotation=45)
    plt.tight_layout()

    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)
    plt.close(figura)
    print(f"Grafico de lineas guardado en: {ruta_completa}")


def graficar_barras(datos_agrupados, columna_categorias, columna_valores,
                    titulo="Grafico de barras", color_barras="#4CAF50",
                    nombre_archivo="barras.png", ruta_destino=RUTA_GRAFICOS):
    if not datos_disponibles(datos_agrupados, titulo):
        return

    crear_ruta_si_no_existe(ruta_destino)

    datos_ordenados = datos_agrupados.sort_values(by=columna_valores, ascending=False)
    figura, area_dibujo = plt.subplots(figsize=(10, 5))
    area_dibujo.bar(
        datos_ordenados[columna_categorias].astype(str),
        datos_ordenados[columna_valores],
        color=color_barras,
        edgecolor="black",
    )
    area_dibujo.set_title(titulo, fontsize=14)
    area_dibujo.set_xlabel(columna_categorias, fontsize=12)
    area_dibujo.set_ylabel(columna_valores, fontsize=12)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)
    plt.close(figura)
    print(f"Grafico de barras guardado en: {ruta_completa}")


def graficar_torta(datos_agrupados, columna_etiquetas, columna_valores,
                   titulo="Grafico de torta", lista_colores=None,
                   nombre_archivo="torta.png", ruta_destino=RUTA_GRAFICOS):
    if not datos_disponibles(datos_agrupados, titulo):
        return

    crear_ruta_si_no_existe(ruta_destino)

    if lista_colores is None:
        lista_colores = ["#FF9800", "#2196F3", "#4CAF50", "#E91E63", "#9C27B0", "#0891B2"]

    figura, area_dibujo = plt.subplots(figsize=(8, 8))
    cantidad_categorias = len(datos_agrupados)
    area_dibujo.pie(
        datos_agrupados[columna_valores],
        labels=datos_agrupados[columna_etiquetas],
        autopct="%1.1f%%",
        colors=lista_colores[:cantidad_categorias],
        startangle=90,
        wedgeprops={"edgecolor": "black", "linewidth": 0.5},
    )
    area_dibujo.set_title(titulo, fontsize=14)
    plt.tight_layout()

    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)
    plt.close(figura)
    print(f"Grafico de torta guardado en: {ruta_completa}")


def graficar_mapa_calor(datos_agrupados, columna_filas, columna_columnas, columna_valores,
                        titulo="Mapa de calor", paleta_color="YlOrRd",
                        nombre_archivo="mapa_calor.png", ruta_destino=RUTA_GRAFICOS):
    if not datos_disponibles(datos_agrupados, titulo):
        return

    crear_ruta_si_no_existe(ruta_destino)

    tabla_pivote = datos_agrupados.pivot_table(
        index=columna_filas,
        columns=columna_columnas,
        values=columna_valores,
        aggfunc="sum",
        fill_value=0,
    )

    figura, area_dibujo = plt.subplots(figsize=(10, 6))
    sns.heatmap(
        tabla_pivote,
        annot=True,
        fmt=".0f",
        cmap=paleta_color,
        ax=area_dibujo,
        linewidths=0.5,
        linecolor="gray",
    )
    area_dibujo.set_title(titulo, fontsize=14)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)
    plt.close(figura)
    print(f"Mapa de calor guardado en: {ruta_completa}")


def graficar_agrupaciones_autores(agrupaciones_autores):
    graficar_barras(
        agrupaciones_autores["agrupacion1"],
        columna_categorias="nacionalidad",
        columna_valores="conteo_autores",
        titulo="Cantidad de autores por nacionalidad",
        color_barras="#2196F3",
        nombre_archivo="autores_por_nacionalidad.png",
    )
    graficar_barras(
        agrupaciones_autores["agrupacion2"],
        columna_categorias="apellido",
        columna_valores="conteo_autores",
        titulo="Autores britanicos por apellido",
        color_barras="#4CAF50",
        nombre_archivo="autores_britanicos_por_apellido.png",
    )
    graficar_torta(
        agrupaciones_autores["agrupacion3"],
        columna_etiquetas="nacionalidad",
        columna_valores="conteo_autores",
        titulo="Autores latinoamericanos por nacionalidad",
        nombre_archivo="autores_latinoamericanos.png",
    )


def graficar_agrupaciones_libros(agrupaciones_libros):
    graficar_barras(
        agrupaciones_libros["agrupacion1"],
        columna_categorias="editorial",
        columna_valores="total_ejemplares",
        titulo="Ejemplares disponibles por editorial",
        color_barras="#0891B2",
        nombre_archivo="ejemplares_por_editorial.png",
    )
    graficar_lineas(
        agrupaciones_libros["agrupacion2"],
        columna_eje_x="anioPublicacion",
        columna_eje_y="conteo_libros",
        titulo="Libros publicados desde 1990 por anio",
        color_linea="#E91E63",
        nombre_archivo="libros_por_anio.png",
    )
    graficar_barras(
        agrupaciones_libros["agrupacion3"],
        columna_categorias="autorNombre",
        columna_valores="conteo_libros",
        titulo="Cantidad de libros por autor",
        color_barras="#FF9800",
        nombre_archivo="libros_por_autor.png",
    )
    graficar_barras(
        agrupaciones_libros["agrupacion4"],
        columna_categorias="editorial",
        columna_valores="promedio_ejemplares",
        titulo="Promedio de ejemplares disponibles por editorial",
        color_barras="#9C27B0",
        nombre_archivo="promedio_ejemplares_por_editorial.png",
    )
    graficar_torta(
        agrupaciones_libros["agrupacion5"],
        columna_etiquetas="categoriaNombre",
        columna_valores="conteo_libros",
        titulo="Cantidad de libros por categoria",
        nombre_archivo="libros_por_categoria.png",
    )
    graficar_mapa_calor(
        agrupaciones_libros["agrupacion6"],
        columna_filas="categoriaNombre",
        columna_columnas="editorial",
        columna_valores="conteo_libros",
        titulo="Cantidad de libros por categoria y editorial",
        nombre_archivo="mapa_calor_categoria_editorial.png",
    )
