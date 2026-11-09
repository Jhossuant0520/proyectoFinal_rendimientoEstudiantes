
# Evaluación del modelo de Machine Learning

## 1. Información general

| Campo | Descripción |
|---|---|
| Proyecto | Predicción del rendimiento académico en matemáticas |
| Tipo de aprendizaje | Supervisado |
| Tipo de problema | Clasificación binaria |
| Modelo principal | Regresión logística |
| Modelo de referencia | DummyClassifier |
| Dataset | Student Performance Mathematics |
| Registros originales | 395 |
| Variables originales | 33 |
| Variable objetivo | aprueba |
| División de datos | 80 % entrenamiento / 20 % prueba |

## 2. Objetivo de la evaluación

Evaluar el desempeño de los modelos implementados para clasificar el resultado académico de los estudiantes en matemáticas.

Se busca determinar si los modelos identifican correctamente a los estudiantes que aprueban y a quienes no aprueban, prestando especial atención a la detección de la clase minoritaria.

La evaluación compara tres configuraciones:

- DummyClassifier como línea base.
- Regresión logística convencional.
- Regresión logística con ponderación de clases mediante `class_weight='balanced'`.

## 3. Descripción del conjunto de datos

Se utiliza el conjunto Student Performance Mathematics del repositorio UCI Machine Learning Repository.

El archivo empleado es:

`data/student-mat.csv`

El conjunto original contiene 395 registros y 33 variables.

Se construye una nueva variable objetivo denominada `aprueba`, a partir de la calificación final G3:

| Condición | Valor de aprueba |
|---|---:|
| G3 >= 10 | 1 |
| G3 < 10 | 0 |

La variable G3 no se utiliza como característica predictora, puesto que determina directamente la variable objetivo.

También se excluyen G1 y G2 para evaluar un escenario en el que la clasificación no dependa de las calificaciones de los dos periodos anteriores.

Después de incorporar la variable objetivo, el conjunto de datos contiene 34 columnas.

## 4. Metodología experimental

El proceso de evaluación comprende las siguientes etapas:

1. Carga del conjunto de datos.
2. Exploración de las variables y sus distribuciones.
3. Construcción de la variable objetivo `aprueba`.
4. Exclusión de las variables G1, G2 y G3 como características predictoras.
5. Codificación de variables categóricas mediante One-Hot Encoding.
6. Estandarización de características numéricas mediante StandardScaler.
7. División de los registros en entrenamiento y prueba, utilizando una proporción de 80 % y 20 %.
8. Entrenamiento del modelo de referencia.
9. Entrenamiento de las configuraciones de regresión logística.
10. Comparación de los resultados mediante métricas de clasificación.

El conjunto de prueba contiene 79 registros.

## 5. Métricas utilizadas

Se utilizan las siguientes métricas:

### Accuracy

Mide la proporción de predicciones correctas respecto al total de predicciones.

### Precision

Mide la proporción de predicciones positivas que realmente pertenecen a la clase evaluada.

### Recall

Mide la proporción de registros de una clase que el modelo logra identificar correctamente.

Se presta especial atención al Recall de la clase 0, correspondiente a los estudiantes que no aprueban.

### F1-score

Representa la media armónica entre Precision y Recall, permitiendo analizar el equilibrio entre ambas métricas.

### Matriz de confusión

Permite identificar los verdaderos positivos, verdaderos negativos, falsos positivos y falsos negativos.

## 6. Resultados experimentales

Los resultados obtenidos en el conjunto de prueba fueron:

| Modelo | Accuracy | Recall aprueba (1) | Recall no aprueba (0) |
|---|---:|---:|---:|
| DummyClassifier | 67,1 % | 100 % | 0 % |
| Regresión logística | 63,3 % | 77,4 % | 34,6 % |
| Regresión logística balanceada | 55,7 % | 60,4 % | 46,2 % |

### 6.1 Interpretación del modelo de referencia

DummyClassifier obtuvo una exactitud de 67,1 %, pero presentó un Recall de 0 % para la clase de estudiantes que no aprueban.

Este resultado se explica porque el modelo de referencia predice todos los registros como estudiantes que aprueban.

Por tanto, aunque alcanza una exactitud relativamente elevada, no identifica a ningún estudiante de la clase minoritaria.

### 6.2 Interpretación de la regresión logística convencional

La regresión logística obtuvo una exactitud de 63,3 %.

Su Recall para la clase que no aprueba fue de 34,6 %, lo que representa una mejora frente al modelo de referencia.

Sin embargo, el modelo todavía presenta dificultades para identificar correctamente a una proporción importante de los estudiantes que no aprueban.

### 6.3 Interpretación de la regresión logística balanceada

La configuración con `class_weight='balanced'` obtuvo una exactitud de 55,7 %.

Su Recall para la clase que no aprueba aumentó hasta 46,2 %.

Esto representa una mejora en la identificación de la clase minoritaria, aunque se produce una disminución en la exactitud global y en el Recall de la clase que aprueba.

Por consiguiente, la ponderación de clases modifica el equilibrio entre los errores de clasificación.

## 7. Matrices de confusión

El orden de las clases utilizado en las matrices es [0, 1]:

- Clase 0: no aprueba.
- Clase 1: aprueba.

Las filas representan las clases reales y las columnas las clases predichas.

### 7.1 DummyClassifier

```text
[[ 0, 26],
 [ 0, 53]]
```

El modelo clasifica todos los registros como estudiantes que aprueban.

No identifica correctamente ningún estudiante de la clase 0.

### 7.2 Regresión logística convencional

```text
[[ 9, 17],
 [12, 41]]
```

Interpretación:

- Verdaderos negativos: 9.
- Falsos positivos: 17.
- Falsos negativos: 12.
- Verdaderos positivos: 41.

El modelo identifica correctamente 9 de los 26 estudiantes que no aprueban.

### 7.3 Regresión logística balanceada

```text
[[12, 14],
 [21, 32]]
```

Interpretación:

- Verdaderos negativos: 12.
- Falsos positivos: 14.
- Falsos negativos: 21.
- Verdaderos positivos: 32.

El modelo identifica correctamente 12 de los 26 estudiantes que no aprueban.

Sin embargo, todavía deja 21 estudiantes de la clase que aprueba clasificados incorrectamente como no aprobados.

## 8. Comparación y análisis

Los resultados muestran que la exactitud global no es suficiente para evaluar la utilidad de un modelo cuando existe desbalance entre las clases.

El DummyClassifier alcanza 67,1 % de Accuracy, pero no identifica estudiantes que no aprueban.

La regresión logística convencional mejora la detección de la clase minoritaria, aunque su Recall sigue siendo limitado.

La regresión logística balanceada consigue el mayor Recall para la clase 0, con 46,2 %. Sin embargo, reduce el Accuracy hasta 55,7 %.

La elección entre los modelos depende del objetivo de evaluación:

- Si se prioriza la exactitud global, la regresión logística convencional supera a la configuración balanceada.
- Si se prioriza detectar estudiantes que podrían no aprobar, la configuración balanceada presenta un mejor resultado entre las alternativas evaluadas.

Ninguno de los modelos consigue resultados suficientes para justificar su utilización como mecanismo autónomo de toma de decisiones académicas.

## 9. Limitaciones identificadas

### 9.1 Tamaño y representatividad del dataset

El conjunto de datos cuenta con 395 registros y corresponde a estudiantes de Portugal.

Por tanto, sus resultados no pueden generalizarse automáticamente a instituciones educativas colombianas.

### 9.2 Desbalance de clases

La distribución de las clases afecta el desempeño del clasificador y dificulta la identificación de estudiantes que no aprueban.

### 9.3 Rendimiento predictivo limitado

El Recall de la clase 0 alcanza como máximo 46,2 % en los modelos evaluados.

Esto significa que todavía existe una proporción considerable de estudiantes que no aprueban y que no son identificados correctamente.

### 9.4 Alcance experimental

El modelo se desarrolla como un prototipo académico y no cuenta con validación externa ni despliegue en un entorno institucional real.

### 9.5 Consideraciones éticas

Las predicciones no deben utilizarse como único criterio para clasificar, excluir o tomar decisiones sobre estudiantes.

Se requiere supervisión humana, protección de la privacidad y evaluación de posibles sesgos.

## 10. Criterios de aceptación del experimento

El experimento se considera documentado y reproducible cuando cumple las siguientes condiciones:

- El notebook permite cargar el dataset y ejecutar el flujo de procesamiento.
- Se documenta la construcción de la variable objetivo.
- Se describen las características excluidas para evitar fuga de información.
- Se realiza la comparación contra un modelo de referencia.
- Se reportan métricas de clasificación.
- Se incluyen las matrices de confusión.
- Se documentan las limitaciones y riesgos de interpretación.

El cumplimiento de estos criterios representa la finalización del experimento académico, no la certificación de que el modelo tenga un desempeño adecuado para producción.

## 11. Conclusiones

La experimentación permitió comparar una línea base y dos configuraciones de regresión logística para la clasificación del rendimiento académico.

La configuración balanceada obtuvo el mayor Recall para la clase de estudiantes que no aprueban, alcanzando 46,2 %.

No obstante, la reducción del Accuracy evidencia que mejorar la detección de una clase puede generar un costo en otras métricas.

Los resultados confirman la necesidad de evaluar modelos de clasificación mediante múltiples indicadores y de analizar sus errores antes de considerar cualquier aplicación práctica.

Se concluye que el modelo desarrollado constituye un prototipo académico útil para estudiar el proceso de clasificación supervisada, pero requiere mejoras y validaciones adicionales antes de utilizarse en contextos educativos reales.

## 12. Referencias

- Cortez, P., & Silva, A. (2008). Using Data Mining to Predict Secondary School Student Performance. https://doi.org/10.1145/1401890.1401967
- UCI Machine Learning Repository. Student Performance Dataset. https://archive.ics.uci.edu/dataset/320/student+performance
- Scikit-learn. Classification metrics. https://scikit-learn.org/stable/modules/model_evaluation.html
- Scikit-learn. DummyClassifier. https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html
- Scikit-learn. Logistic Regression. https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
