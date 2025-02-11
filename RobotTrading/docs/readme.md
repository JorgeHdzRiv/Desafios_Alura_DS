# 📖 Documentación - RobotTrading

Este documento contiene toda la información detallada sobre la implementación del **Robot Trading** en Python.

## 📌 Contenido

1. [Introducción](#introducción)
2. [Requisitos](#requisitos)
3. [Instalación](#instalación)
4. [Estructura del Proyecto](#estructura-del-proyecto)
5. [Funcionamiento](#funcionamiento)
6. [Uso del Bot](#uso-del-bot)
7. [Automatización](#automatización)
8. [Referencias](#referencias)

---

## 📜 Introducción

El proyecto **RobotTrading** es un bot de trading automatizado que toma decisiones de compra y venta de Bitcoin en tiempo real. Se basa en datos históricos, análisis de tendencias y visualización gráfica.

---

## 💻 Requisitos

Antes de ejecutar el proyecto, asegúrate de cumplir con los siguientes requisitos:

- **Python 3.11 o superior**
- Librerías necesarias:
  - Pandas
  - Numpy
  - Yfinance
  - Matplotlib
  - Requests
  - BeautifulSoup4
  - Time

Si no tienes estas librerías, puedes instalarlas con:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Instalación

### **1️⃣ Clonar el repositorio**
```bash
git https://github.com/JorgeHdzRiv/Desafios_Alura_DS.git
cd RobotTrading
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
| `data/`             | Archivos de datos obtenidos (JSON, CSV). |
| `notebooks/`        | Jupyter Notebooks con análisis y pruebas. |
| `scripts/`          | Código fuente del bot de trading en Python. |
| `docs/`             | Documentación y referencias del proyecto. |
| `results/`          | Gráficos y reportes generados. |
| `README.md`         | Descripción general del proyecto. |
| `requirements.txt`  | Lista de librerías necesarias. |
| `.gitignore`        | Archivos a excluir en el repositorio. |

---

## 🚀 Funcionamiento

El bot de trading sigue los siguientes pasos:

1. **Obtención de datos**: Se obtiene el precio histórico de Bitcoin desde una API y se usa Web Scraping para extraer tendencias del mercado.
2. **Limpieza y análisis de datos**: Se eliminan valores nulos y se calcula el precio promedio.
3. **Estrategia de trading**:
   - Si el precio actual es mayor/igual a la media y la tendencia es a la baja → **Vender**.
   - Si el precio actual es menor que la media y la tendencia es al alza → **Comprar**.
4. **Visualización**: Se generan gráficos con la evolución del precio y la media.
5. **Automatización**: El bot ejecuta el análisis cada cierto numero de interacciones y minutos dados por el usuario.

---

## 🛠 Uso del Bot

Para ejecutar el bot, usa:

```bash
python main.py
```

El bot mostrará en la terminal la decisión de compra/venta y generará gráficos en la carpeta `results/`.

---

## 🔄 Automatización

Puedes automatizar la ejecución del bot de acuerdo al numero de iteracciones y minutos que quieras.

---

## 📚 Referencias

- [Documentación de Pandas](https://pandas.pydata.org/docs/)
- [Documentación de Matplotlib](https://matplotlib.org/stable/users/index.html)
- [Documentación de yfinance](https://pypi.org/project/yfinance/)\
- [Documentación de BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [CoinMarketCap](https://coinmarketcap.com/)
- [Web Scraping con Python: Cómo Extraer Datos de Sitios Web](https://www.youtube.com/watch?v=IKlwNKG2dus&t=972s)
- [Pandas-Ta](https://github.com/twopirllc/pandas-ta)


---

## 📖 Glosario
 ---
**RSI:** El índice de fuerza relativa (RSI) es un indicador técnico que se usa para medir la fuerza de los movimientos de precios de un activo. Se trata de un oscilador que va de 0 a 100 y que se representa gráficamente como una línea continua. 

El RSI es un indicador popular que se usa en el trading de criptomonedas, materias primas y Forex. Los traders lo utilizan para identificar situaciones de sobrecompra o sobreventa, que pueden indicar un cambio en la tendencia. 

---
**SMA:** La media móvil simple (SMA) es una herramienta estadística que calcula el precio promedio de un activo durante un período específico. Es un indicador técnico que se utiliza para analizar tendencias de precios. 
---




