# Dashboard de Evaluación · Línea Azul (PAC 2026)
### Programa de Acción Climática · Antofagasta

Dashboard interactivo e independiente para el análisis psicométrico, cualitativo y comparativo de los aprendizajes de la **Línea Azul** (Océano, Biodiversidad de Condrictios y Conservación Litoral), homologado a la escala canónica de la **Línea Verde**.

## 🚀 Acceso en Línea (GitHub Pages)
Puedes acceder directamente al dashboard en:
👉 **[https://badijoly.github.io/pac-linea-azul/](https://badijoly.github.io/pac-linea-azul/)**

---

## 🌊 1. Estructura del Dashboard

El proyecto está diseñado de forma modular y cuenta con las dos vistas requeridas:

1. **Resumen Ejecutivo:**
   - **Métricas Clave (KPIs):** Tasa Favorable, Nivel POST Logrado (Normalizado), Ganancia de Hake ($G$), Avance Neto (Delta), Cobertura Territorial y Climatón.
   - **Distribución de Estados:** Donut dinámico de trayectorias (Mejoró, Mantuvo, Requiere Refuerzo).
   - **Aciertos por Reactivo:** Gráfica comparativa PRE vs. POST de cada pregunta cerrada y residuo crítico (colillas).
   - **Impacto por Establecimiento:** Ranking de deltas netos en escala normalizada 0 a 5.0.
   - **Matriz de Maduración Semántica:** Análisis cualitativo del enriquecimiento del vocabulario ambiental y razonamiento ecológico marino.
   - **Módulo de Ensayo Comparativo:** Síntesis transversal que cruza los resultados de la **Línea Verde** ($N=127$) y la **Línea Azul** ($N=132$), proyectando el impacto global consolidado de todo el **PAC 2026** ($N=259$).

2. **Establecimientos y Aula:**
   - **Tabla Desagregada de las 8 Escuelas:** Indicadores de entrada, salida, deltas, tasa favorable, acreditación ambiental (SNCAE / Sello Ecológico) y participación en Climatón.
   - **Fichas Institucionales con Orientaciones de Aula:** Recomendaciones prácticas para que los profesores líderes refuercen los conceptos y proyecten las soluciones en sus comunidades escolares.
   - **Exportación en Tiempo Real:** Botón para descargar la matriz completa en formato CSV.

---

## 📐 2. Normalización y Homologación de Datos

Para hacer posible una comparación justa, científica y rigurosa entre ambas líneas:

* **Reactivos Cerrados:**
  * En la Línea Verde se utilizaron 5 preguntas cerradas (escala directa de 0.0 a 5.0 puntos).
  * En la Línea Azul se utilizaron 3 preguntas cerradas:
    * **Hito 3 («El litoral que nadie conoce»):** Rúbrica de 3 dimensiones de 0 a 3 puntos cada una (escala bruta de 0 a 9 puntos).
    * **Hito 4 («El plástico que viajó desde el desierto»):** 3 reactivos conceptuales de 0 a 3 puntos + 1 reactivo de residuo crítico (colillas de cigarro), totalizando una escala bruta de 0 a 4 puntos.
  * **Fórmula de Normalización Canónica:**
    $$\text{Puntaje Normalizado (0-5.0)} = \left(\frac{\text{Puntaje Bruto}}{\text{Puntaje Máximo}}\right) \times 5.0$$
* **Reactivos Abiertos:**
  * En Línea Verde se evaluaron 4 preguntas abiertas.
  * En Línea Azul se evaluaron 2 preguntas abiertas por hito (identificación de fauna/residuos y razonamiento ecológico).
  * Ambas líneas fueron procesadas mediante la misma técnica de **Análisis de Contenido Cualitativo con Codificación Categorial** para medir la apropiación del vocabulario científico.
* **Invarianza de la Ganancia de Hake ($G$):**
  $$g = \frac{\text{POST} - \text{PRE}}{\text{MÁXIMO} - \text{PRE}}$$
  Dado que la Ganancia Normalizada de Hake evalúa la fracción de la brecha disponible que fue efectivamente cerrada, es **invariante ante cambios de escala**, lo que permite comparar directamente el impacto pedagógico de ambas líneas sin sesgo.

---

## 📊 3. Resumen de Resultados Principales · Línea Azul

* **Muestra:** 76 estudiantes únicos, **132 evaluaciones pareadas analizadas** en 8 establecimientos educacionales de Antofagasta.
* **Tasa de Aprendizaje Favorable Global:** **91.7%** (121 de 132 evaluaciones mejoraron o mantuvieron nivel alto).
  * *Mejoraron:* 89 evaluaciones ($67.4\%$).
  * *Mantuvieron:* 32 evaluaciones ($24.2\%$).
  * *Requieren Refuerzo:* 11 evaluaciones ($8.3\%$).
* **Puntajes en Escala Normalizada (0 a 5.0 pts):**
  * Diagnóstico Inicial (PRE): **2.34 puntos**
  * Evaluación de Cierre (POST): **3.40 puntos**
  * Avance Neto (Delta): **+1.07 puntos** ($+21.4\%$ de ganancia absoluta sobre el total).
* **Ganancia Normalizada de Hake:** **$G = 0.412$** ($41.2\%$ de la brecha formativa cerrada).
* **Reconocimiento de Residuos Críticos:** La identificación de las colillas de cigarro como residuo costero tóxico aumentó de un **25.8% a un 69.7%** ($+43.9\%$).

---

## ⚡ 4. Ensayo Comparativo: Línea Verde vs. Línea Azul vs. PAC Total

| Dimensión / Indicador | Línea Verde (PAC) | Línea Azul (PAC) | Consolidado PAC 2026 (Global) |
| :--- | :---: | :---: | :---: |
| **Establecimientos Educacionales** | 7 escuelas | 8 escuelas | **15 escuelas** |
| **Estudiantes Únicos** | 67 estudiantes | 76 estudiantes | **143 estudiantes** |
| **Evaluaciones Pareadas Totales** | 127 evaluaciones | 132 evaluaciones | **259 evaluaciones** |
| **Tasa Favorable (Mejoró + Mantuvo)** | **79.5%** | **91.7%** | **85.7% (Ponderado)** |
| **Puntaje Inicial PRE (Norm. 0-5.0)** | 3.26 pts | 2.34 pts | **2.79 pts** |
| **Puntaje Cierre POST (Norm. 0-5.0)** | 3.71 pts | 3.40 pts | **3.55 pts** |
| **Delta Promedio Neto (POST - PRE)** | +0.45 pts (+9.0%) | +1.07 pts (+21.4%) | **+0.76 pts (+15.2%)** |
| **Ganancia Normalizada de Hake ($G$)** | **0.214 (21.4%)** | **0.412 (41.2%)** | **0.315 (31.5% global)** |
| **Foco Temático** | Humedales costeros, aves nativas y cielos limpios | Océano, condrictios (tiburones/rayas), plásticos y colillas | **Educación climática integral de borde costero y desierto** |

---

## 🚀 5. Ejecución Local

El dashboard es completamente autónomo y no requiere dependencias externas de backend. Para visualizarlo:
1. Abrir directamente `index.html` en cualquier navegador moderno.
2. O levantar un servidor local rápido (por ejemplo: `python -m http.server 8080` o la extensión Live Server de VS Code).
