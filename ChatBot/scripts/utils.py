import pickle
from config import URL_LISTA_VERBOS, URL_VERBOS_IRREGULARES

# Función para cargar archivos pickle desde una ruta local
def cargar_pickle_desde_archivo(ruta):
    with open(ruta, 'rb') as file:
        return pickle.load(file)

# Cargar los archivos en variables
lista_verbos = cargar_pickle_desde_archivo(URL_LISTA_VERBOS)
verbos_irregulares = cargar_pickle_desde_archivo(URL_VERBOS_IRREGULARES)
