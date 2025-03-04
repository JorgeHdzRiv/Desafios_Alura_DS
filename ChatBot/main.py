import sys
sys.path.append("./scripts")
from scripts.respuesta import obtener_respuesta

def main():
    print("¡Hola! Soy tu chatbot. Pregúntame lo que quieras. Escribe 'salir' para terminar.")
    while True:
        pregunta = input("Tú: ")
        if pregunta.lower() in ["salir", "adios", "bye"]:
            print("Chatbot: ¡Hasta luego!")
            break
        print("Chatbot: Esperando... estoy buscando una respuesta para ti.")
        respuesta = obtener_respuesta(pregunta)
        print("Chatbot:", respuesta)

if __name__ == "__main__":
    main()
