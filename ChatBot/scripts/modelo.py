from config import torch, BertForSequenceClassification, BertTokenizer,TfidfVectorizer,cosine_similarity,URL_MODELO
from preprocesamiento import normalizar,tratamiento_texto
from carga_dialogos import cargar_base_dialogos

# Cargar el modelo entrenado y el tokenizer
ruta_modelo = URL_MODELO
Modelo_TF = BertForSequenceClassification.from_pretrained(ruta_modelo)
tokenizer_TF = BertTokenizer.from_pretrained(ruta_modelo)
df_dialogo = cargar_base_dialogos()

# Diccionario de clases
diccionario = {0: 'Agradecimiento', 1: 'Aprendizaje', 2: 'Contacto', 3: 'Continuacion',
               4: 'Despedida', 5: 'Edad', 6: 'Error', 7: 'Funcion', 8: 'Identidad',
               9: 'Nombre', 10: 'Origen', 11: 'Otros', 12: 'Saludos', 13: 'Sentimiento',
               14: 'Usuario'}

def clasificacion_modelo(pregunta):
    frase = ' '.join(normalizar(pregunta))

    # Tokenizar la frase de entrada
    tokens = tokenizer_TF.encode_plus(
        frase,
        add_special_tokens=True,
        max_length=128,
        padding='max_length',
        truncation=True,
        return_tensors='pt'
    )

    # Obtener los input_ids y attention_mask
    input_ids = tokens['input_ids']
    attention_mask = tokens['attention_mask']

    # Realizar la predicción
    with torch.no_grad():
        outputs = Modelo_TF(input_ids, attention_mask)

    # Obtener las etiquetas predichas
    etiquetas_predichas = torch.argmax(outputs.logits, dim=1)

    # Decodificar las etiquetas predichas
    etiquetas_decodificadas = etiquetas_predichas.tolist()

    # Obtener la clase encontrada
    llave_buscada = etiquetas_decodificadas[0]
    clase_encontrada = diccionario[llave_buscada]
    print("Respuesta encontrada por el modelo Transformers", "se clasifica como: ", clase_encontrada)

    # Buscar la respuesta más parecida si no es 'Otros'
    if clase_encontrada != 'Otros':
        # Buscar respuesta más parecida en la clase encontrada
        df = df_dialogo[df_dialogo['tipo'] == clase_encontrada]
        df.reset_index(inplace=True)

        # Vectorización del texto
        vectorizer = TfidfVectorizer()
        dialogos_num = vectorizer.fit_transform(df['dialogo'])
        pregunta_num = vectorizer.transform([tratamiento_texto(pregunta)])

        # Calcular la similaridad
        similarity_scores = cosine_similarity(dialogos_num, pregunta_num)
        indice_pregunta_proxima = similarity_scores.argmax()

        # Si la similaridad es mayor a 0.5, devolver la respuesta
        if max(similarity_scores) > 0.5:
            respuesta = df['respuesta'][indice_pregunta_proxima]
        else:
            respuesta = ''
            print('No se encontró una respuesta suficiente')

    else:
        respuesta = ''

    return respuesta

if __name__ == "__main__":
    user_response = "'hola como estas mi hermano'"
    respuesta = clasificacion_modelo(user_response)
    print("Respuesta:", respuesta)
