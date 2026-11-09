
# Registro de riesgos técnicos

## 1. Propósito

Identificar los principales riesgos técnicos asociados al desarrollo, entrenamiento y utilización del modelo de Machine Learning.

Se documentan sus posibles impactos y las medidas de mitigación recomendadas.

## 2. Matriz de riesgos

| ID | Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|---|
| R01 | Datos insuficientes o poco representativos | Alta | Alto | Evaluar la representatividad del dataset, documentar sus limitaciones y realizar validaciones con datos adicionales. |
| R02 | Fuga de información entre entrenamiento y prueba | Media | Alto | Separar los conjuntos antes de ajustar transformaciones y evitar utilizar información derivada del objetivo como predictor. |
| R03 | Sobreajuste del modelo | Media | Alto | Utilizar validación cruzada, comparar modelos y revisar las diferencias entre resultados de entrenamiento y prueba. |
| R04 | Sesgos sociodemográficos | Media | Alto | Analizar métricas por subgrupos, documentar diferencias y mantener supervisión humana. |
| R05 | Incompatibilidad de artefactos o dependencias | Media | Medio | Registrar versiones en requirements.txt, comprobar la carga de los archivos Joblib y ejecutar pruebas automatizadas. |

## 3. Análisis de riesgos

### R01. Datos insuficientes o poco representativos

El conjunto utilizado contiene 395 registros y corresponde a estudiantes de Portugal.

Su tamaño y procedencia pueden limitar la generalización a otros entornos educativos.

**Mitigación:** utilizar conjuntos de datos adicionales, evaluar la calidad de los registros y evitar generalizar los resultados a poblaciones no representadas.

### R02. Fuga de información

La fuga de información puede ocurrir cuando el entrenamiento utiliza datos que no deberían estar disponibles durante la predicción o cuando el conjunto de prueba participa en el ajuste de transformaciones.

**Mitigación:** dividir los datos antes de ajustar transformaciones, utilizar únicamente información disponible en el escenario de predicción y considerar Pipeline de Scikit-learn para encapsular el preprocesamiento.

### R03. Sobreajuste

El modelo podría aprender patrones específicos de los registros de entrenamiento que no se reproduzcan en datos nuevos.

**Mitigación:** aplicar validación cruzada, comparar los resultados de entrenamiento y prueba y evaluar alternativas de regularización.

### R04. Sesgos sociodemográficos

Las características personales, familiares y sociales pueden relacionarse con diferencias en las predicciones y en los errores del modelo.

**Mitigación:** evaluar el comportamiento por subgrupos, analizar los errores de clasificación y no utilizar las predicciones como único criterio de decisiones académicas.

### R05. Incompatibilidad de artefactos

Los archivos serializados pueden presentar problemas de compatibilidad debido a cambios en las versiones de Python o de las bibliotecas utilizadas.

**Mitigación:** mantener un archivo de dependencias, conservar los artefactos junto con la documentación y ejecutar pruebas automatizadas de carga y predicción.

## 4. Seguimiento

Los riesgos deben revisarse cuando se modifiquen los datos, el proceso de preprocesamiento, la configuración de entrenamiento o las versiones de las dependencias.

La mitigación documentada no representa una garantía de eliminación total del riesgo.
