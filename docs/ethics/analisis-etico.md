
# Análisis ético del modelo de predicción académica

## 1. Propósito

Este documento analiza los aspectos éticos relacionados con el desarrollo de un modelo de clasificación del rendimiento académico en matemáticas.

Se consideran los posibles sesgos del conjunto de datos, la equidad, la privacidad, el impacto social y la transparencia de las predicciones.

## 2. Sesgos del conjunto de datos

El dataset Student Performance Mathematics contiene información personal, familiar, académica y social de estudiantes de instituciones educativas de Portugal.

Su tamaño es limitado, con 395 registros, por lo que no representa necesariamente la diversidad de estudiantes de otros países o sistemas educativos.

Entre los posibles factores de sesgo se encuentran:

- Diferencias socioeconómicas.
- Condiciones familiares.
- Ubicación geográfica.
- Acceso a Internet y recursos educativos.
- Diferencias en la distribución de las variables sociodemográficas.

Un patrón identificado en el análisis exploratorio mostró diferencias de Accuracy entre grupos de sexo: aproximadamente 40,4 % para mujeres y 78,1 % para hombres.

Este resultado requiere cautela: el tamaño de los grupos, su distribución y la cantidad de observaciones disponibles pueden afectar las métricas. No demuestra por sí solo que el modelo sea discriminatorio.

## 3. Equidad

Un modelo puede producir resultados diferentes entre grupos de estudiantes incluso cuando utiliza las mismas reglas de clasificación.

Por esta razón, es necesario analizar las métricas por subgrupos y revisar especialmente los falsos positivos y falsos negativos.

La evaluación debe buscar que los errores no generen desventajas sistemáticas para determinados grupos.

No se considera ético utilizar una predicción automatizada como criterio único para clasificar, excluir o limitar oportunidades académicas.

## 4. Privacidad y protección de datos

El dataset utilizado es público, pero esto no significa que cualquier uso de información educativa esté libre de consideraciones de privacidad.

Las variables familiares, personales y académicas pueden representar información sensible en determinados contextos.

Para futuras aplicaciones se recomienda:

- Evitar almacenar datos personales identificables innecesarios.
- Limitar la recolección de información al propósito del análisis.
- Controlar el acceso a los archivos.
- No divulgar registros individuales.
- Mantener medidas de seguridad sobre los datos y los artefactos generados.

## 5. Impacto social

Una predicción incorrecta podría generar consecuencias negativas para un estudiante.

Por ejemplo, clasificar a un estudiante como alguien que probablemente no aprobará podría generar estigmatización, expectativas negativas o decisiones educativas injustificadas.

Por otra parte, no identificar correctamente a estudiantes que necesitan apoyo puede retrasar la implementación de estrategias de acompañamiento.

El modelo debe considerarse una herramienta experimental de apoyo al análisis, no un sustituto del criterio docente.

## 6. Transparencia y explicabilidad

Los resultados deben comunicarse mediante métricas comprensibles y explicaciones sobre el funcionamiento general del modelo.

Es importante informar:

- Qué datos se utilizaron.
- Qué variables intervienen en el análisis.
- Cómo se construyó la variable objetivo.
- Qué métricas se calcularon.
- Qué errores presentó el modelo.
- Cuáles son sus limitaciones.

La transparencia permite que las personas comprendan que una predicción representa una estimación y no una certeza sobre el resultado académico.

## 7. Responsabilidad y supervisión humana

Se recomienda que cualquier posible uso futuro de las predicciones mantenga supervisión humana.

Los docentes y responsables académicos deben analizar el contexto individual del estudiante y evitar depender exclusivamente de los resultados automatizados.

El modelo no debe utilizarse para asignar sanciones, restringir oportunidades ni determinar el futuro académico de una persona.

## 8. Conclusión ética

El desarrollo del modelo permite estudiar cómo las características personales, familiares y escolares pueden relacionarse con el rendimiento académico.

Sin embargo, el dataset tiene limitaciones de tamaño y representatividad, y el modelo presenta errores de clasificación importantes.

Por ello, no se considera adecuado utilizarlo como mecanismo autónomo de toma de decisiones educativas.

Su aplicación debe limitarse al contexto experimental, manteniendo transparencia, protección de datos, análisis de equidad y supervisión humana.
