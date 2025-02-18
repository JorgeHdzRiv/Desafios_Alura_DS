# 🤖 Documentación - Chatbot Inteligente

Este documento contiene toda la información detallada sobre la implementación del **Chatbot Inteligente** utilizando Machine Learning y procesamiento de lenguaje natural (NLP).

---

## 📌 Contenido

1. [Introducción](#introducción)
2. [Requisitos](#requisitos)
3. [Instalación](#instalación)
4. [Estructura del Proyecto](#estructura-del-proyecto)
5. [Funcionamiento](#funcionamiento)
6. [Uso del Chatbot](#uso-del-chatbot)
7. [Automatización](#automatización)
8. [Referencias](#referencias)
9. [Glosario](#glosario)

---

## 📜 Introducción

El proyecto **Chatbot Inteligente** consiste en un asistente virtual capaz de interpretar el lenguaje humano y generar respuestas coherentes basadas en información preprocesada. Para lograrlo, utilizaremos técnicas de procesamiento de lenguaje natural (NLP), modelos de Machine Learning y bases de datos de conversaciones estructuradas.

---

## 💻 Requisitos

Antes de ejecutar el proyecto, asegúrate de cumplir con los siguientes requisitos:

- **Google Colaboratory o un entorno de Python 3.11 o superior**
- Librerías necesarias:
  - Pandas
  - Numpy
  - Scikit-learn
  - NLTK
  - TensorFlow/Keras
  - Flask (para despliegue opcional)
  - Github (para almacenamiento de archivos y de este repositorio)

Si no tienes estas librerías, puedes instalarlas con:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Instalación

### **1️⃣ Clonar el repositorio**
```bash
git https://github.com/JorgeHdzRiv/Desafios_Alura_DS.git
cd ChatBot
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
| `data/`             | Contiene archivos de verbos y bases de datos de conversaciones. |
| `notebooks/`        | Jupyter Notebooks con análisis y pruebas. |
| `models/`           | Modelos entrenados de Machine Learning. |
| `scripts/`          | Código fuente del chatbot. |
| `docs/`             | Documentación del proyecto. |
| `README.md`         | Descripción general del proyecto. |
| `requirements.txt`  | Lista de librerías necesarias. |
| `.gitignore`        | Archivos a excluir en el repositorio. |

---

## 🚀 Funcionamiento

El Chatbot Inteligente sigue los siguientes pasos:

1. **Configuración del entorno**: Activar entorno e instalar dependencias y/o ejecutar cuaderno en Colab.
2. **Importación de verbos**: Se cargan archivos con verbos en español para mejorar la comprensión del lenguaje.
3. **Tratamiento de datos**: Se aplican técnicas de NLP para limpiar y normalizar los textos.
4. **Carga de bases de datos**: Se importan ejemplos de conversaciones para entrenar el modelo.
5. **Búsqueda de respuesta**: Se emplean técnicas de Machine Learning para encontrar la mejor respuesta a una consulta.
6. **Ejecución del Chatbot**: Se realiza la prueba en tiempo real y se evalúan sus respuestas.

---

## 🛠 Uso del Chatbot

Para ejecutar el chatbot dentro de Colab:

1. Abre el notebook [Chatbot_Inteligente](https://colab.research.google.com/drive/1nYXIkW67Oc6NcwMBwHINMaiqZZ1Im4jt?usp=sharing) 
2. Genera una copia del notebook
3. Sigue los pasos en cada celda para ejecutar el procesamiento y entrenamiento del chatbot.
4. Prueba el chatbot ingresando preguntas en la celda de ejecución final.

Si deseas ejecutarlo localmente:

```bash
python chatbot.py
```

El chatbot responderá en la terminal.

---

## 🔄 Automatización

Puedes automatizar la ejecución del chatbot usando tareas programadas o integrándolo con una API en Flask.

Ejemplo de ejecución con Flask:

```bash
python app.py
```

---

## 📚 Referencias

- [Documentación de Pandas](https://pandas.pydata.org/docs/)
- [Documentación de Scikit-learn](https://scikit-learn.org/stable/)
- [Documentación de NLTK](https://www.nltk.org/)
- [TensorFlow/Keras](https://www.tensorflow.org/api_docs)
- [Curso de NLP con Python](https://www.datacamp.com/courses/natural-language-processing-in-python)

---

## 📖 Glosario

**NLP (Procesamiento de Lenguaje Natural):** Rama de la inteligencia artificial que se enfoca en la interacción entre computadoras y humanos mediante el lenguaje natural.

**Lematización:** Técnica de NLP que convierte palabras a su forma base.

**Machine Learning:** Conjunto de algoritmos que permiten a una máquina aprender patrones a partir de datos.

**Tokenización:** Proceso de dividir un texto en palabras o frases individuales.

---

¡Listo! Ahora puedes comenzar a entrenar y mejorar tu **Chatbot Inteligente** 🚀🤖.