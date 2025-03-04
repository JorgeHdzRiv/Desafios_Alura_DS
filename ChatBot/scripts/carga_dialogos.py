from config import os,re,pd,URL_DIALOGOS
from preprocesamiento import tratamiento_texto

# Cargar archivos de diálogos
def cargar_base_dialogos():
    """Carga los diálogos desde archivos de texto en la carpeta especificada."""
    lista_documentos = [x for x in os.listdir(URL_DIALOGOS) if x.endswith(".txt")]
    
    lista_dialogos, lista_dialogos_respuesta, lista_tipo_dialogo = [], [], []
    
    for documento in lista_documentos:
        tipo = documento.replace('.txt', '')
        with open(os.path.join(URL_DIALOGOS, documento), 'r', encoding='utf-8', errors='ignore') as f:
            lineas = [line.strip() for line in f.readlines() if line.strip()]
            for i in range(0, len(lineas) - 1, 2):
                pregunta = re.sub(r"[^\w\s+\-*/]", '', lineas[i])
                pregunta = tratamiento_texto(pregunta)
                respuesta = lineas[i + 1]
                lista_dialogos.append(pregunta)
                lista_dialogos_respuesta.append(respuesta)
                lista_tipo_dialogo.append(tipo)
    
    datos = {
        'dialogo': lista_dialogos,
        'respuesta': lista_dialogos_respuesta,
        'tipo': lista_tipo_dialogo,
        'interseccion': 0,
        'jaro_winkler': 0,
        'probabilidad': 0
    }
    
    df_dialogo = pd.DataFrame(datos)
    df_dialogo = df_dialogo.drop_duplicates(keep='first').reset_index(drop=True)
    
    return df_dialogo