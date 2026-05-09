import pandas as pd

VALORES_VALIDOS_NACIONALIDAD = {"colombiana"}

def limpiar_autores(data_frame_sucio: pd.DataFrame) -> pd.DataFrame:
    if data_frame_sucio.empty:
        return pd.DataFrame(columns=["id", "nombre", "apellido", "nacionalidad"])

    data_frame_limpio = data_frame_sucio.copy()

    for col in ["id", "nombre", "apellido", "nacionalidad"]:
        if col not in data_frame_limpio.columns:
            data_frame_limpio[col] = pd.NA

    columnas_texto = ["nombre", "apellido", "nacionalidad"]
    for columna in columnas_texto:
        data_frame_limpio[columna] = (
            data_frame_limpio[columna].astype("string").str.strip().str.lower()
        )

    data_frame_limpio["nacionalidad"] = data_frame_limpio["nacionalidad"].where(
        data_frame_limpio["nacionalidad"].isin(VALORES_VALIDOS_NACIONALIDAD), pd.NA
    )

    data_frame_limpio["id"] = pd.to_numeric(data_frame_limpio["id"], errors="coerce")
    data_frame_limpio = data_frame_limpio.dropna(subset=["id"])
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id"] > 0]

    columnas_obligatorias = [
        "id",
        "nombre",
        "apellido",
    ]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)
    data_frame_limpio = data_frame_limpio.drop_duplicates(subset=["id"])

    return data_frame_limpio
