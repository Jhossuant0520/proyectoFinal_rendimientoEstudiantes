
# ADR-004: Estrategia de almacenamiento y despliegue

## Estado

Aceptado.

## Fecha

2026-11-08.

## Contexto

El proyecto requiere almacenar el conjunto de datos utilizado para el entrenamiento y conservar los artefactos generados por el modelo de Machine Learning.

El alcance corresponde a un prototipo académico ejecutado localmente mediante Python y Jupyter Notebook. No se requiere infraestructura de producción ni acceso concurrente de múltiples usuarios.

## Decisión

Se establece una estrategia de almacenamiento basada en archivos locales:

| Elemento | Almacenamiento | Propósito |
|---|---|---|
| Dataset | CSV | Conservar los registros académicos originales. |
| Modelo | Joblib | Persistir el clasificador entrenado. |
| Escalador | Joblib | Persistir el objeto StandardScaler. |
| Dependencias | requirements.txt | Registrar las bibliotecas necesarias. |

El despliegue se mantiene en un entorno local de desarrollo y experimentación.

No se implementa una base de datos, API REST, servicio en la nube ni interfaz de usuario externa.

## Alternativas consideradas

### Base de datos relacional

Permitiría almacenar información estructurada y gestionar consultas, pero incrementaría la complejidad sin aportar ventajas necesarias para el alcance actual.

### Servicio de almacenamiento en la nube

Facilitaría la distribución y administración centralizada de artefactos, pero requeriría infraestructura, configuración y medidas adicionales de seguridad.

### Registro de modelos

Una plataforma de gestión de modelos facilitaría el versionamiento y seguimiento de experimentos. Se considera una mejora futura, no una necesidad del prototipo.

## Justificación

El almacenamiento mediante archivos resulta suficiente para el volumen de información y las necesidades experimentales del proyecto.

Joblib permite serializar objetos de Python y Scikit-learn, facilitando la reutilización del modelo y del escalador sin repetir necesariamente todo el entrenamiento.

## Consecuencias positivas

- Implementación sencilla.
- Menor complejidad de infraestructura.
- Facilidad para versionar los artefactos mediante Git.
- Reutilización local de los objetos serializados.
- Reproducción del entorno mediante requirements.txt.

## Consecuencias negativas

- Dependencia del entorno local.
- Ausencia de disponibilidad como servicio externo.
- Necesidad de mantener compatibilidad entre versiones de bibliotecas.
- Ausencia de mecanismos centralizados para el versionamiento de experimentos.

## Consideraciones de seguridad

Los archivos Joblib deben cargarse únicamente desde fuentes confiables, debido a que la deserialización de archivos no confiables puede ejecutar código.

Los artefactos deben conservarse junto con la documentación de las dependencias y su origen.

## Evolución futura

En una versión posterior se podría incorporar una API REST, almacenamiento centralizado y un registro de modelos para administrar versiones, métricas y experimentos.

Estas funcionalidades están fuera del alcance de la implementación académica actual.

## Referencias

- Joblib Documentation: https://joblib.readthedocs.io/en/stable/
- Scikit-learn Model Persistence: https://scikit-learn.org/stable/model_persistence.html
