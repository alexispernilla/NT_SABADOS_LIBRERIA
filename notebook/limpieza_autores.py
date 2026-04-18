import pandas as pd


VALORES_VALIDOS_NOMBRE = {
    "gabriel garcía márquez",
    "laura restrepo",
    "fernando vallejo",
    "juan gabriel vásquez",
    "jorge franco",
    "william ospina",
    "álvaro mutis",
}
VALORES_VALIDOS_CODIGO = {"au001", "au002", "au003", "au004", "au005", "au006", "au007"}
VALORES_VALIDOS_NACIONALIDAD = {"colombiana"}
FECHA_POR_DEFECTO = pd.Timestamp("1900-01-01")


def limpiar_autores(data_frame_sucio: pd.DataFrame) -> pd.DataFrame:
    data_frame_limpio = data_frame_sucio.copy()

    columnas_texto = ["nombre", "codigo", "nacionalidad"]
    for columna in columnas_texto:
        data_frame_limpio[columna] = (
            data_frame_limpio[columna].astype("string").str.strip().str.lower()
        )

    data_frame_limpio["nombre"] = data_frame_limpio["nombre"].where(
        data_frame_limpio["nombre"].isin(VALORES_VALIDOS_NOMBRE), pd.NA
    )
    data_frame_limpio["codigo"] = data_frame_limpio["codigo"].where(
        data_frame_limpio["codigo"].isin(VALORES_VALIDOS_CODIGO), pd.NA
    )
    data_frame_limpio["nacionalidad"] = data_frame_limpio["nacionalidad"].where(
        data_frame_limpio["nacionalidad"].isin(VALORES_VALIDOS_NACIONALIDAD), pd.NA
    )

    data_frame_limpio["id"] = pd.to_numeric(data_frame_limpio["id"], errors="coerce")
    data_frame_limpio["libros_publicados"] = pd.to_numeric(
        data_frame_limpio["libros_publicados"], errors="coerce"
    )

    data_frame_limpio = data_frame_limpio[data_frame_limpio["id"] > 0]
    data_frame_limpio = data_frame_limpio[data_frame_limpio["libros_publicados"] >= 0]

    data_frame_limpio["fecha_nacimiento"] = pd.to_datetime(
        data_frame_limpio["fecha_nacimiento"], errors="coerce"
    )
    data_frame_limpio["fecha_nacimiento"] = data_frame_limpio["fecha_nacimiento"].fillna(
        FECHA_POR_DEFECTO
    )

    columnas_obligatorias = [
        "id",
        "nombre",
        "codigo",
        "nacionalidad",
        "libros_publicados",
    ]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)
    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio
