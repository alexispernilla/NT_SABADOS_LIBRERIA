import pandas as pd


COLUMNAS_LIBROS = [
    "id",
    "titulo",
    "isbn",
    "editorial",
    "anioPublicacion",
    "cantidadEjemplares",
    "disponible",
    "autorNombre",
    "categoriaNombre",
]


def obtener_nombre_autor(autor):
    if not isinstance(autor, dict):
        return pd.NA

    nombre = str(autor.get("nombre", "")).strip()
    apellido = str(autor.get("apellido", "")).strip()
    nombre_completo = f"{nombre} {apellido}".strip().lower()

    return nombre_completo if nombre_completo else pd.NA


def obtener_nombre_categoria(categoria):
    if not isinstance(categoria, dict):
        return pd.NA

    nombre = str(categoria.get("nombre", "")).strip().lower()

    return nombre if nombre else pd.NA


def limpiar_libros(data_frame_sucio: pd.DataFrame) -> pd.DataFrame:
    if data_frame_sucio.empty:
        return pd.DataFrame(columns=COLUMNAS_LIBROS)

    data_frame_limpio = data_frame_sucio.copy()

    cols_esperadas = ["id", "titulo", "isbn", "editorial", "anioPublicacion", "cantidadEjemplares", "disponible"]
    for col in cols_esperadas:
        if col not in data_frame_limpio.columns:
            data_frame_limpio[col] = pd.NA

    for col in ["autor", "categoria"]:
        if col not in data_frame_limpio.columns:
            data_frame_limpio[col] = pd.NA

    columnas_texto = ["titulo", "isbn", "editorial"]
    for columna in columnas_texto:
        data_frame_limpio[columna] = (
            data_frame_limpio[columna].astype("string").str.strip().str.lower()
        )

    data_frame_limpio["autorNombre"] = data_frame_limpio["autor"].apply(obtener_nombre_autor)
    data_frame_limpio["categoriaNombre"] = data_frame_limpio["categoria"].apply(obtener_nombre_categoria)

    data_frame_limpio["id"] = pd.to_numeric(data_frame_limpio["id"], errors="coerce")
    data_frame_limpio["anioPublicacion"] = pd.to_numeric(data_frame_limpio["anioPublicacion"], errors="coerce")
    data_frame_limpio["cantidadEjemplares"] = pd.to_numeric(data_frame_limpio["cantidadEjemplares"], errors="coerce")

    data_frame_limpio = data_frame_limpio.dropna(subset=["id"])
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id"] > 0]
    
    # Rellenar con 0 para evitar errores en dropna
    data_frame_limpio["cantidadEjemplares"] = data_frame_limpio["cantidadEjemplares"].fillna(0)

    columnas_obligatorias = ["id", "titulo", "isbn"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)
    data_frame_limpio = data_frame_limpio.drop_duplicates(subset=["id"])

    return data_frame_limpio[COLUMNAS_LIBROS]
