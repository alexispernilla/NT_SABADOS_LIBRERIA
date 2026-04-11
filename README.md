# NT_SABADOS_LIBRERIA

Proyecto integrador de Nuevas Tecnologias para simular datos de autores y libros.
Las simulaciones incluyen errores intencionales para apoyar pruebas de calidad de datos.

## Requisitos

- Python 3
- Entorno virtual recomendado

## Instalacion

```bat
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecucion

```bat
python utils\main.py
```

Los archivos generados se guardan automaticamente en la carpeta `data/`.
La salida combina registros validos con registros ensuciados de forma intencional.
