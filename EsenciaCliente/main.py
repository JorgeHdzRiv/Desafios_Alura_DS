import pandas as pd
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "scripts"))

# Importar las funciónes desde scripts
from exploracion_datos import generar_graficos_eda,generar_graficos_clustering
from preprocesamiento import preprocesamiento
# from clusterizacion import comprobacion_clusters
from clusterizacion import instanciar_kmeans

# Cargar los datos
df = pd.read_csv('./data/media_prediction_cost_esp.csv')

# Funciones a ejecutar
generar_graficos_eda(df)
X_std = preprocesamiento(df)
# comprobacion_clusters(X_std) #No ejecutar ya que los resultados de la comprobacion ya estan en el repositorio
df_clusters = instanciar_kmeans(df,X_std) 
generar_graficos_clustering(df_clusters)
