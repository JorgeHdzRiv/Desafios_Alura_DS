from config import jellyfish,cosine_similarity,TfidfVectorizer,re
from preprocesamiento import tratamiento_texto
from carga_dialogos import cargar_base_dialogos

# Cargar base de datos
df_dialogos = cargar_base_dialogos()
vectorizer = TfidfVectorizer()

# Método 1: Intersección de palabras
def interseccion(text1, text2):
    palabras_text1 = set(text1.split())
    palabras_text2 = set(text2.split())
    return len(palabras_text1 & palabras_text2) / max(1, len(palabras_text1))  # Evitar división entre 0

# Método 2: Similaridad con TfidfVectorizer + Cosine Similarity
def similarity(text1, text2):
    tfidf_matrix = vectorizer.fit_transform([text1, text2])  # Solo usa text1 y text2
    return cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]

# Método 3: Jaro-Winkler Similarity
def jaro_winkler(text1, text2):
    return jellyfish.jaro_winkler_similarity(text1, text2)

# Función para verificar si el usuario inició un diálogo
def dialogo(user_response):
    # Tratamiento del texto del usuario
    user_response = tratamiento_texto(user_response)  # Normalización del texto
    user_response = re.sub(r"[^\w\s]", '', user_response)  # Elimina signos de puntuación

    df = df_dialogos.copy()  # Copia del DataFrame

    # Asegurar que todas las columnas existen en el DataFrame
    columnas_faltantes = {'interseccion', 'jaro_winkler', 'probabilidad', 'similarity'} - set(df.columns)
    for col in columnas_faltantes:
        df[col] = 0.0  # Inicializar como float

    # Convertir columnas a float64 para evitar advertencias
    df[['interseccion', 'jaro_winkler', 'probabilidad', 'similarity']] = df[
        ['interseccion', 'jaro_winkler', 'probabilidad', 'similarity']
    ].astype(float)

    for idx, row in df.iterrows():
        # Comparaciones de texto
        df.at[idx, 'interseccion'] = float(interseccion(user_response, row['dialogo']))
        df.at[idx, 'similarity'] = float(similarity(user_response, row['dialogo']))  # Se añadió 'similarity'
        df.at[idx, 'jaro_winkler'] = float(jaro_winkler(user_response, row['dialogo']))

        # Determinar la mayor probabilidad entre los métodos
        df.at[idx, 'probabilidad'] = float(max(df.at[idx, 'interseccion'], df.at[idx, 'similarity'], df.at[idx, 'jaro_winkler']))

    # Ordenar por la mejor coincidencia
    df.sort_values(by=['probabilidad', 'jaro_winkler'], inplace=True, ascending=False)
    probabilidad = df['probabilidad'].head(1).values[0]

    if probabilidad >= 0.93:
        print('Respuesta encontrada por el método de comparación de textos - Probabilidad: ', probabilidad)
        respuesta = df['respuesta'].head(1).values[0]
    else:
        respuesta = ''

    return respuesta
