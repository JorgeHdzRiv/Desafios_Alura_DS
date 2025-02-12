# 🛒 Documentación - Análisis de Hábitos de Compra en Supermercados

Este documento contiene toda la información detallada sobre la implementación del **análisis de hábitos de compra** mediante clustering en la cadena de supermercados **Universal Food**.

## 📌 Contenido

1. [Introducción](#introducción)
2. [Requisitos](#requisitos)
3. [Instalación](#instalación)
4. [Estructura del Proyecto](#estructura-del-proyecto)
5. [Funcionamiento](#funcionamiento)
6. [Uso del Análisis](#uso-del-análisis)
7. [Validación de Clusters](#validación-de-clusters)
8. [Referencias](#referencias)

---

## 📜 Introducción

El proyecto **Análisis de Hábitos de Compra en Supermercados** busca segmentar clientes según sus patrones de compra utilizando **clustering**. Se emplean técnicas de preprocesamiento, exploración de datos y validación de modelos para entender mejor el comportamiento de los consumidores y mejorar su experiencia de compra.

---

## 💻 Requisitos

Antes de ejecutar el proyecto, asegúrate de contar con los siguientes requisitos:

- **Python 3.x**
- Librerías necesarias:
  - Pandas
  - Numpy
  - Matplotlib
  - Seaborn
  - Scikit-learn

Si no tienes estas librerías, instálalas con:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Instalación

### **1️⃣ Clonar el repositorio**
```bash
git clone https://github.com/JorgeHdzRiv/Desafios_Alura_DS.git
cd EsenciaCliente
```

### **2️⃣ Crear y activar el entorno virtual**
#### **Windows (CMD)**
```cmd
python -m venv venv
venv\Scripts\activate
```

#### **Windows (PowerShell)**
```powershell
.\venv\Scripts\activate
```

#### **Mac/Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

### **3️⃣ Instalar las dependencias**
```bash
pip install -r requirements.txt
```

---

## 📂 Estructura del Proyecto

| Carpeta/Archivo       | Descripción |
|----------------------|-------------|
| `data/`             | Conjunto de datos en formato CSV o JSON. |
| `notebooks/`        | Jupyter Notebooks con el análisis y visualización de datos. |
| `scripts/`          | Código fuente en Python para procesamiento y clustering. |
| `docs/`             | Documentación y referencias del proyecto. |
| `results/`          | Gráficos y reportes de análisis de clusters. |
| `README.md`         | Descripción general del proyecto. |
| `requirements.txt`  | Lista de librerías necesarias. |
| `.gitignore`        | Archivos a excluir en el repositorio. |

---

## 🚀 Funcionamiento

El análisis de clustering sigue los siguientes pasos:

1. **Obtención de datos**: Se extrae la base de datos con el historial de compras de los clientes.
2. **Transformación de datos**: Se traduce la base de datos del inglés al español y se normalizan los valores.
3. **Exploración y visualización**: Se generan gráficos con Matplotlib y Seaborn para identificar patrones.
4. **Preprocesamiento**:
   - Codificación de variables categóricas.
   - Reducción de dimensionalidad.
   - Estandarización de datos.
5. **Segmentación con clustering**: Se aplican algoritmos de Machine Learning para agrupar clientes según sus patrones de compra.
6. **Interpretación y generación de estrategias**: Se analizan los clusters y se plantean estrategias de personalización.

---

## 🛠 Uso del Análisis

Para ejecutar el análisis, utiliza el siguiente comando:

```bash
python scripts/main.py
```

El resultado incluirá la segmentación de clientes y gráficos en la carpeta `results/`.

---

## 🔄 Validación de Clusters

Para garantizar la efectividad de la segmentación, se realizan:

- **Pruebas con diferentes números de clusters**.
- **Evaluaciones con métricas como Silhouette Score y Davies-Bouldin Index**.
- **Comparaciones de distribución y estabilidad entre clusters**.

---

## 📚 Referencias

- [Documentación de Pandas](https://pandas.pydata.org/docs/)
- [Documentación de Matplotlib](https://matplotlib.org/stable/users/index.html)
- [Documentación de Seaborn](https://seaborn.pydata.org/)
- [Documentación de Scikit-learn](https://scikit-learn.org/stable/)

---

## 📖 Glosario

### **Clustering**
Técnica de Machine Learning no supervisado utilizada para agrupar datos en categorías según sus similitudes.

### **Silhouette Score**
Métrica utilizada para evaluar la calidad de los clusters en un análisis de segmentación.

### **Estandarización de datos**
Proceso que ajusta las variables a una misma escala para evitar sesgos en los algoritmos de Machine Learning.

---

Este documento proporciona toda la información necesaria para entender y ejecutar el análisis de clustering aplicado en supermercados. 🚀📊

