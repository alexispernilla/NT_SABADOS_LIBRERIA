import pandas as pd


VALORES_VALIDOS_TITULO = {
    "cien años de soledad",
    "delirio",
    "la virgen de los sicarios",
    "los informantes",
    "rosario tijeras",
    "el país de la canela",
    "la nieve del almirante",
}
VALORES_VALIDOS_AUTOR = {
    "gabriel garcía márquez",
    "laura restrepo",
    "fernando vallejo",
    "juan gabriel vásquez",
    "jorge franco",
    "william ospina",
    "álvaro mutis",
}
VALORES_VALIDOS_CODIGO = {"lb001", "lb002", "lb003", "lb004", "lb005", "lb006", "lb007"}
FECHA_POR_DEFECTO = pd.Timestamp("2000-01-01")


def limpiar_libros(data_frame_sucio: pd.DataFrame) -> pd.DataFrame:
    data_frame_limpio = data_frame_sucio.copy()

    columnas_texto = ["titulo", "codigo", "autor"]
    for columna in columnas_texto:
        data_frame_limpio[columna] = (
            data_frame_limpio[columna].astype("string").str.strip().str.lower()
        )

    data_frame_limpio["titulo"] = data_frame_limpio["titulo"].where(
        data_frame_limpio["titulo"].isin(VALORES_VALIDOS_TITULO), pd.NA
    )
    data_frame_limpio["codigo"] = data_frame_limpio["codigo"].where(
        data_frame_limpio["codigo"].isin(VALORES_VALIDOS_CODIGO), pd.NA
    )
    data_frame_limpio["autor"] = data_frame_limpio["autor"].where(
        data_frame_limpio["autor"].isin(VALORES_VALIDOS_AUTOR), pd.NA
    )

    data_frame_limpio["id"] = pd.to_numeric(data_frame_limpio["id"], errors="coerce")
    data_frame_limpio["paginas"] = pd.to_numeric(data_frame_limpio["paginas"], errors="coerce")

    data_frame_limpio = data_frame_limpio[data_frame_limpio["id"] > 0]
    data_frame_limpio = data_frame_limpio[data_frame_limpio["paginas"].between(1, 2000)]

    data_frame_limpio["fecha_publicacion"] = pd.to_datetime(
        data_frame_limpio["fecha_publicacion"], errors="coerce"
    )
    data_frame_limpio["fecha_publicacion"] = data_frame_limpio[
        "fecha_publicacion"
    ].fillna(FECHA_POR_DEFECTO)

    columnas_obligatorias = ["id", "titulo", "codigo", "autor", "paginas"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)
    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio
