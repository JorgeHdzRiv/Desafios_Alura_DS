from comparar_textos import dialogo
from modelo import clasificacion_modelo

def obtener_respuesta(pregunta):
    """Combina métodos de comparación de texto y modelo ML para obtener la mejor respuesta."""
    respuesta_texto = dialogo(pregunta)
    
    if respuesta_texto:
        return respuesta_texto
    
    respuesta_modelo = clasificacion_modelo(pregunta)
    return respuesta_modelo if respuesta_modelo else "Lo siento, no tengo una respuesta para eso, puedes intentar con otras palabras o hacer otra pregunta."

if __name__ == "__main__":
    user_response = "hola como estas mi hermano"
    respuesta = obtener_respuesta(user_response)
    print("Respuesta:", respuesta)
