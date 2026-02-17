# Servicio_hotel 

# 🏨 Sistema ETL y Análisis Predictivo para Optimización Hotelera

**Dashboard interactivo con ETL, minería de datos, clustering, clasificación y reportes automáticos**

Este proyecto implementa un sistema completo de **Extracción, Transformación y Carga (ETL)** junto con **análisis predictivo y exploratorio**, utilizando **Dash**, **Plotly**, **scikit-learn** y **Bootstrap Components**.

El sistema permite cargar datasets del sector hotelero y realizar análisis avanzados enfocados en:

* Identificación de patrones de cancelación
* Optimización de servicios para familias, comidas, estancias largas
* Segmentación de reservas (clustering)
* Predicción de demanda de servicios (Random Forest)
* Visualización dinámica en un Dashboard intuitivo
* Exportación de reportes analíticos automáticos

---

## ✨ Características principales

### 📁 **1. Carga de Datos**

* Subida de archivos CSV, Excel y JSON.
* Detección automática de codificación.
* Vista previa de datos y estadísticas descriptivas.
* Visualización interactiva por pestañas.

### 🔧 **2. Proceso ETL Completo**

Incluye:

* Limpieza de valores nulos
* Eliminación de duplicados
* Tratamiento de outliers
* Feature engineering automático:

  * `total_guests`
  * `total_nights`
  * `family_size`
  * `estimated_revenue`
  * `has_children`
  * `long_stay`
* Codificación de variables categóricas
* Transformaciones numéricas: Normalización, Z-score, log
* Comparación antes/después con gráficos y heatmaps
* Histograma automático para columnas numéricas
* Comparación detallada por columna

### 🤖 **3. Minería de Datos**

Incluye dos módulos:

#### ✔ Clasificación (Random Forest)

* Predicción de **reservas con alta demanda de servicios**
* Métricas generadas: Accuracy, Precision, Recall, F1, ROC-AUC
* Gráfica de matriz de confusión
* Importancia de características

#### ✔ Clustering (K-Means)

* Segmentación de reservas por tipo de hotel (City/Resort)
* Gráfica interactiva de clusters
* Resumen estadístico por segmento:

  * ADR promedio
  * Tasa de cancelación
  * Tamaño de familia
  * Solicitudes especiales

### 📊 **4. Análisis Exploratorio (EDA)**

Incluye múltiples visualizaciones interactivas:

* Distribución de hoteles
* ADR por tipo de hotel
* Tamaño de familia
* Ingresos estimados
* Composición de clientes (Treemap)
* Servicios por temporada
* Solicitudes especiales vs tamaño familiar

### 🧠 **5. Módulo de Toma de Decisiones**

Incluye:

* KPIs dinámicos
* Visualizaciones para decisiones ejecutivas
* Recomendaciones generadas automáticamente
* Exportación de reporte completo a Excel

### 📤 **6. Exportación de Reportes**

El sistema genera un archivo Excel con:

* Datos completos transformados
* Resumen ejecutivo
* Estadísticas
* Análisis de cancelaciones
* Análisis de ingresos
* Formato profesional (encabezados, filtros congelados, estilos)

---

## 🏗 Tecnologías utilizadas

| Categoría        | Tecnologías                                |
| ---------------- | ------------------------------------------ |
| Backend          | Python 3+, Pandas, NumPy                   |
| Dashboards       | Dash, Plotly, Dash Bootstrap Components    |
| Machine Learning | scikit-learn                               |
| Visualización    | Plotly Express, Graph Objects              |
| Reportes         | XlsxWriter                                 |
| Preprocesamiento | LabelEncoder, MinMaxScaler, StandardScaler |

---

## 🚀 Instalación y ejecución

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/Niuska0212/Servicio_hotel.git
cd Servicio_hotel
```

### 2️⃣ Crear entorno virtual (opcional)

```bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
```

### 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4️⃣ Ejecutar la aplicación

```bash
python dash_ETL_proyect.py
```

La aplicación se abrirá en:

```
http://127.0.0.1:8050
```

---


## 📈 Ejemplo del Flujo Completo

1. Subes un CSV de reservas hoteleras
2. El sistema limpia y transforma automáticamente
3. Visualizas la calidad de datos antes/después
4. Ejecutas clustering o clasificación
5. Obtienes gráficas y métricas
6. Exportas un reporte profesional

---

## 💡 Posibles mejoras futuras

* Integración con base de datos SQL
* Implementación de modelos más robustos (XGBoost, CatBoost)
* Predicción de ADR
* Forecasting de demanda
* Exportación PDF automática
* Control de usuarios y autenticación

---

## 🧑‍💻 Autores
Estudiantes de Ingeniería Informática
* NIUSKA ISABEL GONZALEZ RANGEL
* JESUS YAHIR ACEVES TORRES
* YADSIRI YAMILETH VAZQUEZ GARCIA
* DIEGO ARATH MALDONADO CARDENAS

---

