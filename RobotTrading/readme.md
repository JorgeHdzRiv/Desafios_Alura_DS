# 🤖 RobotTrading - Bitcoin Trading Bot

Este proyecto consiste en la construcción de un **Robot Trading en Python** capaz de tomar decisiones de compra y venta de Bitcoin en tiempo real. Para lograrlo, se implementarán técnicas de obtención y limpieza de datos, análisis de tendencias y visualización gráfica.

## 🎯 **Objetivos del proyecto**
- Obtener datos históricos de precios de Bitcoin desde una API y realizar Web Scraping de noticias relevantes.
- Limpiar y procesar los datos para eliminar valores atípicos y calcular el precio promedio.
- Implementar una estrategia de compra y venta basada en la comparación del precio actual con la media y la tendencia del mercado.
- Visualizar los datos mediante gráficos que indiquen la evolución del precio y las decisiones del bot.
- Automatizar la ejecución del algoritmo de decisión cada 5 minutos.

📂 Explora las carpetas del proyecto para conocer más sobre la implementación. 🚀📊

## 📂 Estructura del proyecto

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


## ⚙️ Instalación y configuración

### 🔹 1. Clonar el repositorio
```bash
git clone https://github.com/JorgeHdzRiv/Desafios_Alura_DS.git
cd RobotTrading
```

### 🔹 2. Crear un ambiente virtual
Ejecuta el siguiente comando según tu sistema operativo:

**Windows(CMD)**

```bash
python -m venv venv
venv\Scripts\activate
```

**Windows (PowerShell)**

Si aparece un error de permisos, primero ejecuta este comando en PowerShell como administrador:
```bash
Set-ExecutionPolicy Unrestricted -Scope CurrentUser
```

Luego activa el ambiente:
```bash
.\venv\Scripts\activate
```

**Mac/Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 🔹 3. Instalar dependecias
Ejecuta el siguiente comando para instalar las librerías necesarias:
```bash
pip install -r requirements.txt
```

Si quieres agregar nuevas librerías (en caso de ser necesarias), usa:
```bash
pip install nombre_libreria
pip freeze > requirements.txt
```

## 🚀 Uso del proyecto

1. Asegúrate de estar en el ambiente virtual (venv activado).
2. Ejecuta el script principal:
```bash
python scripts/main.py
```
3. Sigue las instrucciones en la terminal para ver las decisiones de compra/venta del bot.
4. Puedes visualizar los gráficos generados en la carpeta results/.

## 🛑 Desactivar el ambiente virtual
Si necesitas salir del ambiente virtual, usa:
```bash
deactivate
```
