
# Predicción del rendimiento académico en matemáticas

Mini-proyecto académico de Machine Learning desarrollado para clasificar el rendimiento de estudiantes en matemáticas, utilizando información académica, familiar y social del conjunto de datos Student Performance Mathematics de UCI.

## 1. Descripción del problema

El proyecto aborda un problema de clasificación binaria supervisada: identificar si un estudiante aprueba o no matemáticas a partir de diferentes características disponibles en el conjunto de datos.

La finalidad es experimentar con un modelo básico de Machine Learning, evaluar su desempeño mediante métricas cuantitativas y analizar sus limitaciones técnicas y éticas.

**Pregunta orientadora:** ¿En qué medida las características personales, familiares y escolares disponibles permiten clasificar el resultado académico de un estudiante en matemáticas?

El modelo es un prototipo académico. No está diseñado para tomar decisiones institucionales ni para reemplazar la evaluación de docentes.

## 2. Objetivos

### Objetivo general

Implementar y evaluar un modelo básico de clasificación supervisada que permita analizar el rendimiento académico en matemáticas.

### Objetivos específicos

- Explorar y preparar un conjunto de datos educativo.
- Construir una variable objetivo binaria.
- Entrenar un modelo de regresión logística.
- Comparar los resultados contra un modelo de referencia.
- Evaluar el desempeño mediante métricas de clasificación.
- Identificar riesgos, sesgos y limitaciones del uso de predicciones académicas.

## 3. Conjunto de datos

**Fuente:** UCI Machine Learning Repository — Student Performance.

**Enlace:** https://archive.ics.uci.edu/dataset/320/student+performance

**Archivo utilizado:** `data/student-mat.csv`

| Característica | Descripción |
|---|---|
| Registros | 395 estudiantes |
| Variables originales | 33 |
| Tipo de información | Académica, familiar, personal y social |
| Variable objetivo | `aprueba` |
| Tipo de problema | Clasificación binaria |

Entre las variables disponibles se encuentran:

- Personales: sexo, edad y zona de residencia.
- Familiares: nivel educativo y ocupación de los padres, composición familiar y relaciones familiares.
- Académicas: tiempo de estudio, asignaturas reprobadas y ausencias.
- Sociales: actividades, acceso a Internet, relaciones y hábitos.

### Construcción de la variable objetivo

Se crea la variable `aprueba` a partir de la calificación final `G3`:

| Condición | Valor |
|---|---:|
| G3 >= 10 | 1 — Aprueba |
| G3 < 10 | 0 — No aprueba |

La variable G3 no se utiliza como predictor porque determina directamente el objetivo. También se excluyen G1 y G2 para estudiar un escenario que no dependa de las calificaciones de los dos periodos anteriores.

Después de crear `aprueba`, el DataFrame contiene 34 columnas.

## 4. Modelo seleccionado

Se utiliza **Regresión Logística**, un algoritmo de aprendizaje supervisado empleado en problemas de clasificación.

Se seleccionó porque:

- Es adecuado para clasificación binaria.
- Tiene una implementación sencilla mediante Scikit-learn.
- Permite estudiar la relación entre las características de entrada y la probabilidad de pertenecer a cada clase.
- Facilita comparar configuraciones y analizar sus resultados.

También se utiliza `DummyClassifier` como modelo de referencia. Se evalúa adicionalmente una configuración de regresión logística con ponderación de clases mediante `class_weight='balanced'`.

## 5. Funcionamiento del sistema

El flujo general de Machine Learning comprende:

1. Carga del archivo CSV mediante Pandas.
2. Exploración de datos y revisión de variables.
3. Construcción de la variable objetivo `aprueba`.
4. Exclusión de G1, G2 y G3 de las características predictoras.
5. Codificación de variables categóricas mediante One-Hot Encoding.
6. Estandarización de características numéricas mediante StandardScaler.
7. División de los datos en entrenamiento (80 %) y prueba (20 %).
8. Entrenamiento del modelo de referencia.
9. Entrenamiento de regresión logística convencional y balanceada.
10. Evaluación mediante métricas y matrices de confusión.
11. Persistencia de los artefactos mediante Joblib.

### Estructura del proyecto

```text
proyectoFinal_rendimientoEstudiantes/
│
├── data/
│   └── student-mat.csv
│
├── models/
│   ├── modelo_final.joblib
│   └── scaler.joblib
│
├── tests/
│   └── test_model_artifacts.py
│
├── docs/
│   ├── architecture/
│   │   ├── arquitectura.md
│   │   └── adr/
│   │       ├── ADR-001-stack-tecnologico.md
│   │       ├── ADR-002-modelo-predictivo.md
│   │       └── ADR-003-prevencion-data-leakage.md
│   │
│   └── evaluation/
│       └── evaluacion-modelo.md
│
├── analisis.ipynb
├── requirements.txt
├── .gitignore
└── README.md
```

## 6. Instalación y ejecución

### Requisitos

- Python 3.12.
- Git.
- Entorno compatible con Jupyter Notebook para ejecutar `analisis.ipynb`.

### Clonar el repositorio

```bash
git clone https://github.com/Jhossuant0520/proyectoFinal_rendimientoEstudiantes.git
cd proyectoFinal_rendimientoEstudiantes
```

### Crear un entorno virtual en Windows

```powershell
py -3.12 -m venv .venv
```

### Activar el entorno

```powershell
.\.venv\Scripts\Activate.ps1
```

### Instalar dependencias

```powershell
python -m pip install -r requirements.txt
```

### Ejecutar el análisis

Abrir `analisis.ipynb` desde Jupyter Notebook o desde un IDE compatible y ejecutar las celdas del flujo experimental.

### Ejecutar las pruebas automatizadas

```powershell
python -m unittest discover -s tests -v
```

Las pruebas verifican la carga y el funcionamiento básico del modelo serializado y del escalador.

## 7. Evaluación y resultados

La evaluación se realiza sobre un conjunto de prueba de 79 registros.

Se compararon tres configuraciones:

- DummyClassifier.
- Regresión logística convencional.
- Regresión logística con ponderación de clases.

### Resultados cuantitativos

La siguiente tabla presenta Accuracy global y Precision, Recall y F1-score de la clase `0` (estudiantes que no aprueban). Estas tres métricas por clase se obtienen a partir de las matrices de confusión documentadas.

| Modelo | Accuracy | Precision clase 0 | Recall clase 0 | F1 clase 0 |
|---|---:|---:|---:|---:|
| DummyClassifier | 67,1 % | 0 %* | 0 % | 0 % |
| Regresión logística | 63,3 % | 42,9 % | 34,6 % | 38,3 % |
| Regresión logística balanceada | 55,7 % | 36,4 % | 46,2 % | 40,7 % |

*En DummyClassifier no se predicen registros de la clase 0; por eso, su Precision para esa clase se presenta como cero bajo la convención de evaluación utilizada.*

### Interpretación

- **Accuracy:** proporción de predicciones correctas sobre el total de registros.
- **Precision:** proporción de predicciones de no aprobación que realmente corresponden a estudiantes que no aprueban.
- **Recall:** proporción de estudiantes que no aprueban y que el modelo identifica correctamente.
- **F1-score:** media armónica de Precision y Recall.

La regresión logística balanceada obtiene el mayor Recall de la clase 0 (46,2 %), aunque su Accuracy disminuye a 55,7 %.

El resultado de DummyClassifier demuestra que una exactitud aparentemente aceptable puede ocultar la incapacidad de identificar la clase minoritaria.

### Matrices de confusión

Las filas representan las clases reales y las columnas las clases predichas. El orden de las etiquetas es `[0, 1]`.

**DummyClassifier**

```text
[[ 0, 26],
 [ 0, 53]]
```

**Regresión logística**

```text
[[ 9, 17],
 [12, 41]]
```

**Regresión logística balanceada**

```text
[[12, 14],
 [21, 32]]
```

Considerando la clase positiva convencional `1 = aprueba`, la matriz balanceada contiene:

- Verdaderos positivos (TP): 32 estudiantes que aprueban y fueron clasificados correctamente.
- Verdaderos negativos (TN): 12 estudiantes que no aprueban y fueron clasificados correctamente.
- Falsos positivos (FP): 14 estudiantes que no aprueban, pero fueron clasificados como aprobados.
- Falsos negativos (FN): 21 estudiantes que aprueban, pero fueron clasificados como no aprobados.

Al evaluar específicamente la clase 0 como una categoría de interés, el modelo identifica correctamente 12 de los 26 estudiantes que no aprueban.

La interpretación de los errores debe considerar siempre cuál clase se define como positiva.

## 8. Análisis ético

### Sesgos y equidad

El dataset contiene características sociodemográficas como sexo, edad, residencia y contexto familiar. Estas variables pueden introducir diferencias en el comportamiento del modelo.

Durante la exploración se observaron diferencias de Accuracy por sexo: aproximadamente 40,4 % para mujeres y 78,1 % para hombres. Estos resultados deben interpretarse con cautela debido al tamaño limitado de los grupos y no permiten concluir por sí solos que exista discriminación.

Es necesario evaluar el desempeño por subgrupos y analizar si determinadas características generan errores sistemáticos.

### Privacidad

Aunque se utiliza un dataset público, la información educativa y familiar requiere un tratamiento responsable. No se deben incorporar datos personales identificables ni publicar información individual de estudiantes.

En aplicaciones futuras se deben aplicar medidas de minimización de datos, control de acceso y protección de la información.

### Impacto social

Una predicción incorrecta podría generar estigmatización o influir injustamente en las expectativas académicas sobre un estudiante.

Los falsos negativos y falsos positivos pueden afectar la identificación de necesidades de apoyo y la asignación de recursos educativos.

### Uso responsable y transparencia

El modelo debe utilizarse únicamente como herramienta experimental de apoyo al análisis. Ninguna decisión académica debe tomarse exclusivamente a partir de sus predicciones.

Se deben comunicar las limitaciones, los errores y las variables utilizadas, manteniendo la supervisión humana.

## 9. Riesgos técnicos

| Riesgo | Impacto | Mitigación |
|---|---|---|
| Tamaño y representatividad limitada del dataset | Alto | Validar con conjuntos adicionales y poblaciones diferentes. |
| Fuga de información (data leakage) | Alto | Separar entrenamiento y prueba y ajustar transformaciones únicamente con entrenamiento. |
| Sobreajuste | Medio/alto | Aplicar validación cruzada y comparar con el modelo de referencia. |
| Sesgos sociodemográficos | Alto | Evaluar resultados por subgrupos y mantener supervisión humana. |

## 10. Alcance y limitaciones

### Qué hace

- Procesa un dataset educativo.
- Construye una variable objetivo binaria.
- Entrena y evalúa modelos de clasificación.
- Compara resultados con una línea base.
- Guarda el modelo y el escalador para su reutilización.
- Ejecuta pruebas automatizadas sobre los artefactos serializados.

### Qué no hace

- No ofrece predicciones mediante una API.
- No tiene una interfaz de usuario para docentes o estudiantes.
- No se integra con plataformas académicas.
- No determina automáticamente el futuro académico de un estudiante.
- No está validado para su despliegue institucional.

El modelo es un prototipo académico. Su desempeño y representatividad no permiten asegurar que se comporte de la misma manera en instituciones o poblaciones diferentes.

## 11. Criterios de aceptación del proyecto

- El dataset se carga y procesa correctamente.
- La variable objetivo se construye conforme a la regla definida.
- Se implementa un modelo de clasificación supervisada.
- Se compara contra un modelo de referencia.
- Se reportan Accuracy, Precision, Recall y F1-score.
- Se presentan e interpretan matrices de confusión.
- Se documentan los riesgos y las consideraciones éticas.
- Los artefactos serializados pueden cargarse y utilizarse.
- Las pruebas automatizadas finalizan correctamente.

El cumplimiento de estos criterios demuestra la ejecución del prototipo académico, pero no certifica su idoneidad para producción.

## 12. Documentación complementaria

- [Arquitectura y diagrama C4](docs/architecture/arquitectura.md)
- [ADR-001: selección del stack tecnológico](docs/architecture/adr/ADR-001-stack-tecnologico.md)
- [ADR-002: selección del modelo predictivo](docs/architecture/adr/ADR-002-modelo-predictivo.md)
- [ADR-003: prevención de data leakage](docs/architecture/adr/ADR-003-prevencion-data-leakage.md)
- [Evaluación detallada del modelo](docs/evaluation/evaluacion-modelo.md)

## 13. Glosario

| Término | Definición |
|---|---|
| Machine Learning | Área de la inteligencia artificial que permite aprender patrones a partir de datos. |
| Clasificación binaria | Problema predictivo con dos clases posibles. |
| Regresión logística | Algoritmo supervisado utilizado para estimar probabilidades de clasificación. |
| Dataset | Conjunto organizado de datos utilizado para el análisis y entrenamiento. |
| Feature | Variable utilizada como entrada del modelo. |
| Target | Variable que el modelo busca predecir. |
| Accuracy | Proporción de predicciones correctas. |
| Precision | Proporción de predicciones positivas que son correctas. |
| Recall | Proporción de casos positivos reales identificados correctamente. |
| F1-score | Media armónica entre Precision y Recall. |
| Matriz de confusión | Tabla que compara clases reales y predichas. |
| Data leakage | Uso indebido de información que no debería estar disponible durante el entrenamiento. |
| Overfitting | Situación en la que el modelo se ajusta demasiado a los datos de entrenamiento. |
| One-Hot Encoding | Transformación de variables categóricas en columnas binarias. |
| StandardScaler | Transformación que estandariza características numéricas. |
| DummyClassifier | Clasificador de referencia que permite establecer una línea base. |

## 14. Referencias

- Cortez, P., & Silva, A. (2008). Using Data Mining to Predict Secondary School Student Performance. https://doi.org/10.1145/1401890.1401967
- UCI Machine Learning Repository. Student Performance Dataset. https://archive.ics.uci.edu/dataset/320/student+performance
- Scikit-learn. Documentation. https://scikit-learn.org/stable/
- Pandas. Documentation. https://pandas.pydata.org/docs/
- NumPy. Documentation. https://numpy.org/doc/
- Joblib. Documentation. https://joblib.readthedocs.io/en/stable/
- Project Jupyter. Documentation. https://docs.jupyter.org/

## 15. Integrantes y organización del repositorio

El proyecto se desarrolla en equipo, manteniendo ramas individuales para evidenciar los aportes y una rama de integración.

| Integrante | Rama individual |
|---|---|
| Jhossuant Cabezas | `dev_jhossuant` |
| Karen Sanchez | `dev_ksanchez90` |

La integración se realiza mediante Pull Requests hacia `develop`. La rama `main` se reserva para la versión consolidada del proyecto.

- [ADR-004: almacenamiento y despliegue](docs/architecture/adr/ADR-004-persistencia-despliegue.md)
- [Análisis ético](docs/ethics/analisis-etico.md)
- [Registro de riesgos técnicos](docs/risks/riesgos-tecnicos.md)