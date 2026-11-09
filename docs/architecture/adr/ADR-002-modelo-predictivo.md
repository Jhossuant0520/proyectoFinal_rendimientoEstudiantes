
# ADR-002: Selección del modelo de clasificación

## Estado

Aceptado.

## Fecha

2026-11-08.

## Contexto

El objetivo del proyecto consiste en predecir si un estudiante aprueba o no matemáticas, utilizando variables disponibles en el conjunto de datos Student Performance Mathematics.

La variable objetivo es binaria:

- `aprueba = 1`: cuando la calificación final G3 es mayor o igual a 10.
- `aprueba = 0`: cuando la calificación final G3 es inferior a 10.

Se necesita un modelo sencillo que permita abordar un problema de clasificación supervisada y analizar su desempeño mediante métricas cuantitativas.

## Decisión

Se selecciona la regresión logística como modelo principal de clasificación.

Adicionalmente, se utiliza DummyClassifier como modelo de referencia para establecer un punto de comparación y evaluar si el modelo entrenado aporta información predictiva frente a una estrategia básica.

Durante la experimentación también se evalúan configuraciones de regresión logística con y sin ponderación de clases mediante `class_weight='balanced'`.

## Alternativas consideradas

### 1. DummyClassifier

Se utiliza como línea base. Su propósito es establecer un rendimiento de referencia sin aprender relaciones complejas entre las características y la variable objetivo.

### 2. Regresión logística

Se selecciona por ser un algoritmo de clasificación supervisada, relativamente sencillo de implementar y analizar. Permite estudiar cómo las características de entrada se relacionan con la probabilidad de pertenecer a cada clase.

### 3. Otros algoritmos de clasificación

Árboles de decisión, K-Nearest Neighbors y Random Forest representan alternativas que podrían evaluarse en futuras iteraciones. No forman parte de la implementación principal documentada en esta decisión.

## Consecuencias positivas

- Implementación sencilla.
- Adecuación al problema de clasificación binaria.
- Posibilidad de comparar el modelo contra una línea base.
- Facilidad para calcular métricas de clasificación.
- Permite estudiar el efecto del desbalance entre clases mediante ponderación.

## Consecuencias negativas

- Puede presentar limitaciones cuando las relaciones entre variables no son lineales.
- Su desempeño puede verse afectado por el desbalance de clases.
- Una exactitud elevada no garantiza una detección adecuada de estudiantes que no aprueban.
- Requiere preprocesamiento adecuado de las variables de entrada.

## Evaluación del desempeño

El modelo se evalúa utilizando:

- Accuracy.
- Precision.
- Recall.
- F1-score.
- Matriz de confusión.

Se presta especial atención al Recall de la clase `aprueba = 0`, ya que permite identificar qué proporción de estudiantes que no aprueban es reconocida correctamente por el modelo.

El uso de estas métricas permite analizar los errores de clasificación y evitar depender exclusivamente de la exactitud global.

## Limitaciones y alcance

La selección de regresión logística no implica que sea el algoritmo de mejor rendimiento para todos los escenarios.

La decisión responde al alcance académico del proyecto, que prioriza implementar y evaluar un modelo básico, comprender sus resultados y analizar críticamente sus limitaciones.

## Referencias

- Scikit-learn. Logistic Regression. https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
- Scikit-learn. DummyClassifier. https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html
- Scikit-learn. Model Evaluation. https://scikit-learn.org/stable/modules/model_evaluation.html
