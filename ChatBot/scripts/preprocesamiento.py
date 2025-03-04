from config import re,unicodedata,jellyfish,nlp
from utils import lista_verbos,verbos_irregulares

#Función para encontrar la raiz de las palabras
def raiz(palabra):
  max_similaridad = 0
  mejor_coincidencia = palabra #Por defecto, devolvemos la palabra original

  for verbo in lista_verbos:
    similitud = jellyfish.jaro_winkler_similarity(palabra, verbo)
    if similitud > max_similaridad:
      max_similaridad = similitud
      mejor_coincidencia = verbo

  return mejor_coincidencia if max_similaridad >= 0.93 else palabra

# Función para limpiar y normalizar texto
def tratamiento_texto(texto):
    texto = texto.lower()
    texto = ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto

# Función para reemplazar el final de una palabra por 'r'
def reemplazar_terminacion(palabra):
    terminaciones = ["ste", "es", "me", "as", "te"]
    for terminacion in terminaciones:
        if palabra.endswith(terminacion):
            return palabra[:-len(terminacion)] + "r"
    return palabra

#Función para devolver los tokens normalizados del texto
def normalizar(texto):
   tokens=[]
   doc = nlp(texto)
   for t in doc:
    lemma=verbos_irregulares.get(t.text, t.lemma_.split()[0])
    lemma=re.sub(r'[^\w\s+\-*/]', '', lemma)
    if t.pos_ in ('VERB','PROPN','PRON','NOUN','AUX','SCONJ','ADJ','ADV','NUM') or lemma in lista_verbos:
      if t.pos_=='VERB':
        lemma = reemplazar_terminacion(lemma)
        tokens.append(raiz(tratamiento_texto(lemma)))
      else:
        tokens.append(tratamiento_texto(lemma))

    tokens = list(dict.fromkeys(tokens))
    tokens = list(filter(None, tokens))
    return tokens