
# ADR-001: Selección del stack tecnológico

## Estado

Aceptado.

## Fecha

2026-11-08.

## Contexto

El proyecto requiere un entorno que permita cargar, explorar y transformar datos académicos, entrenar modelos básicos de Machine Learning y evaluar sus resultados mediante métricas cuantitativas.

También se requiere que el desarrollo sea reproducible en los equipos de los integrantes, evitando depender de servicios externos o infraestructura compleja.

## Decisión

Se selecciona Python como lenguaje principal y Jupyter Notebook como entorno de experimentación.

Se utilizan las siguientes bibliotecas:

| Tecnología | Justificación |
|---|---|
| Python | Lenguaje con amplio soporte para análisis de datos y Machine Learning. |
| Pandas | Permite cargar, transformar y analizar estructuras de datos. |
| NumPy | Facilita operaciones numéricas y manipulación de arreglos. |
| Scikit-learn | Proporciona herramientas de preprocesamiento, entrenamiento y evaluación. |
| Matplotlib | Permite representar gráficamente resultados y distribuciones. |
| Joblib | Permite almacenar y recuperar modelos y objetos de procesamiento. |
| Jupyter Notebook | Facilita documentar y ejecutar el flujo experimental. |

Las dependencias se registran en `requirements.txt` para facilitar la instalación y reproducibilidad del entorno.

## Alternativas consideradas

1. **R:** ofrece capacidades estadísticas y herramientas para Machine Learning, pero se mantiene Python para utilizar un único entorno de desarrollo.
2. **Aplicación web:** permitiría consumir predicciones mediante una interfaz, pero incrementaría la complejidad y se encuentra fuera del alcance del mini-proyecto.
3. **Plataformas administradas de Machine Learning:** ofrecen infraestructura de entrenamiento y despliegue, pero no son necesarias para el alcance académico definido.

## Consecuencias positivas

- Desarrollo de un flujo experimental sencillo.
- Disponibilidad de bibliotecas especializadas para cada etapa.
- Facilidad para documentar resultados mediante celdas de código y texto.
- Reutilización del entorno mediante un archivo de dependencias.
- Menor complejidad de infraestructura.

## Consecuencias negativas

- El entrenamiento y la ejecución dependen del entorno local.
- No se dispone de una interfaz para usuarios externos.
- La reproducibilidad depende de mantener las versiones y configuraciones necesarias.
- La solución no está preparada para atender múltiples solicitudes simultáneas.

## Referencias

- Python Documentation: https://docs.python.org/3/
- Scikit-learn: https://scikit-learn.org/stable/
- Pandas: https://pandas.pydata.org/docs/
- Project Jupyter: https://docs.jupyter.org/
