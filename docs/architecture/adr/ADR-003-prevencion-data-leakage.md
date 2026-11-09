
# ADR-003: Prevención de fuga de información (Data Leakage)

## Estado

Aceptado.

## Fecha

2026-11-08.

## Contexto

Durante la construcción de un modelo predictivo es necesario evitar que las variables utilizadas para entrenarlo contengan información que no estaría disponible en el momento real de realizar una predicción.

La presencia de información relacionada directamente con el resultado que se desea predecir puede generar estimaciones artificialmente optimistas y afectar la validez de la evaluación.

En este proyecto, la variable objetivo `aprueba` se construye a partir de la calificación final G3.

Además, el conjunto de datos contiene las calificaciones parciales G1 y G2, que presentan una relación académica con el resultado final.

## Decisión

Se establece que:

1. La variable objetivo `aprueba` se construye utilizando la calificación final G3.
2. G3 no se utiliza como característica predictora, ya que es la información a partir de la cual se define el resultado.
3. Las variables G1 y G2 se excluyen de las características predictoras para evitar depender de calificaciones parciales que podrían no estar disponibles en un escenario de predicción temprana.
4. La evaluación del modelo se realiza utilizando una división de datos de entrenamiento y prueba de 80 % y 20 %, respectivamente.
5. Las transformaciones que aprenden parámetros de los datos, como StandardScaler, deben ajustarse exclusivamente con el conjunto de entrenamiento. Posteriormente, se utiliza el mismo objeto para transformar el conjunto de prueba.

## Justificación

La exclusión de G1 y G2 busca que el modelo estudie la relación entre otras características del estudiante y su resultado académico, sin depender de evaluaciones parciales que pueden actuar como indicadores indirectos muy fuertes de la calificación final.

También se busca evitar que la información estadística del conjunto de prueba intervenga en el ajuste de las transformaciones utilizadas durante el entrenamiento.

Estas medidas contribuyen a obtener una evaluación más representativa del comportamiento del modelo sobre datos no utilizados durante su ajuste.

## Alternativas consideradas

### 1. Utilizar G1 y G2 como características

Podría mejorar las métricas predictivas, ya que las calificaciones parciales guardan relación con la calificación final.

Sin embargo, esta alternativa cambia el escenario de predicción y puede hacer que el modelo dependa de información académica que no estaría disponible en etapas tempranas.

### 2. Utilizar G3 como característica predictora

Se descarta debido a que G3 es la variable utilizada para definir el objetivo `aprueba`. Incorporarla como predictor produciría una fuga directa de información.

### 3. Ajustar el escalador utilizando todos los registros

Se descarta como procedimiento recomendado porque introduce información estadística del conjunto de prueba en el preprocesamiento.

El escalador debe aprender sus parámetros a partir del conjunto de entrenamiento.

## Consecuencias positivas

- Se reduce el riesgo de fuga de información relacionada con la variable objetivo.
- Se define un escenario de predicción más exigente.
- Se favorece una evaluación más realista del modelo.
- Se documentan criterios para mantener la separación entre entrenamiento y prueba.

## Consecuencias negativas

- La exclusión de G1 y G2 puede reducir el rendimiento predictivo.
- El modelo pierde información académica potencialmente útil.
- Las métricas pueden ser inferiores a las obtenidas por modelos que utilizan calificaciones parciales.

## Consideración de implementación

La exclusión de G1, G2 y G3 como características debe mantenerse en el proceso de selección de variables.

También debe verificarse en el notebook que StandardScaler se ajuste después de la división de entrenamiento y prueba. En caso contrario, deberá corregirse el procedimiento antes de considerar validada esta decisión.

## Referencias

- Scikit-learn. Common pitfalls and recommended practices. https://scikit-learn.org/stable/common_pitfalls.html
- Scikit-learn. StandardScaler. https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html
- UCI Machine Learning Repository. Student Performance Dataset. https://archive.ics.uci.edu/dataset/320/student+performance
