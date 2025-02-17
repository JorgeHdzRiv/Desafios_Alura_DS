"""
En este script se obtienen los datos de la base de datos de kaggle, en este caso ya los tenemos descargados en las carpetas correspondientes, por lo que no es necesario ejecutar este script, sin embargo se recomienda ver el tratamiento y traduccion de los datos en ingles contenido dentro de este script.
"""

import pandas as pd
import os
import sys
import diccionarios

df = pd.read_csv("./data/media_prediction_cost.csv")
sys.path.append(os.path.abspath("./scripts"))
df.rename(columns=diccionarios.columnas, inplace=True)

# Ciclo para cada columna del dataframe
for column in df.columns:
    # Verificar si existe un diccionario con el nombre de la columna
    if hasattr(diccionarios, column):
        # Obtener el diccionario correspondiente a la columna
        translation_dict = getattr(diccionarios, column)

        # Traducir los valores de la columna usando el diccionario
        df[column] = df[column].map(translation_dict).fillna(df[column])

# Ruta Guardado
output_path = './data/media_prediction_cost_spa.csv'

# Exportar el dataframe a un archivo .csv
df.to_csv(output_path, index=False)

# Confirmacion
print(f"El dataset traducido se ha guardado en: {output_path}")
