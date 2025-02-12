# 🛒 Análisis de hábitos de compra en supermercados  

Este proyecto tiene como objetivo comprender los hábitos de compra de los clientes de la cadena de supermercados **Universal Food**, utilizando técnicas de **Machine Learning** para segmentarlos mediante **clustering**. Se trabajará con datos históricos, realizando un preprocesamiento adecuado y aplicando algoritmos de aprendizaje no supervisado para generar insights que permitan personalizar la experiencia de compra.

## 🎯 **Objetivos del proyecto**
- Obtener y transformar los datos del comportamiento de compra de los clientes.
- Explorar visualmente los datos con **Matplotlib** y **Seaborn** para identificar patrones y distribuciones.
- Preprocesar la información: codificación de variables categóricas, reducción de dimensionalidad y estandarización de datos.
- Aplicar algoritmos de **clustering** con **Scikit-Learn** para segmentar clientes según sus hábitos de compra.
- Evaluar y validar los clusters utilizando métricas de calidad y estabilidad.
- Interpretar los resultados y proponer estrategias para mejorar la experiencia del cliente.

📂 Explora las carpetas del proyecto para conocer más sobre la implementación. 🚀📊

## 📂 Estructura del proyecto

| Carpeta/Archivo       | Descripción |
|----------------------|-------------|
| `data/`             | Conjunto de datos en formato CSV o JSON. |
| `notebooks/`        | Jupyter Notebooks con el análisis y visualización de datos. |
| `scripts/`          | Código fuente en Python para procesamiento y clustering. |
| `docs/`             | Documentación del proyecto y referencias. |
| `results/`          | Gráficos y reportes de análisis de clusters. |
| `readme.md`         | Descripción general del proyecto. |
| `requirements.txt`  | Lista de librerías necesarias. |
| `.gitignore`        | Archivos a excluir en el repositorio. |

¡Explora y contribuye a este proyecto de análisis de datos para mejorar la experiencia de compra en supermercados! 🛍️📊

## ⚙️ Instalación y configuración

### 🔹 1. Clonar el repositorio
```bash
git clone https://github.com/JorgeHdzRiv/Desafios_Alura_DS.git
cd EsenciaCliente
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
python main.py
```
3. Sigue las instrucciones en la terminal para ver las decisiones de compra/venta del bot.
4. Puedes visualizar los gráficos generados en la carpeta results/.

## 🛑 Desactivar el ambiente virtual
Si necesitas salir del ambiente virtual, usa:
```bash
deactivate
```
