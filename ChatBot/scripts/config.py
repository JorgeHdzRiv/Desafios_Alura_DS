import os
import re
import random
import pickle
import unicodedata
import pandas as pd
import numpy as np
import spacy
import jellyfish
import torch
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import BertForSequenceClassification, BertTokenizer

# Cargar modelo de procesamiento de lenguaje natural
nlp = spacy.load('es_core_news_md')

# Definir rutas de archivos
URL_LISTA_VERBOS = "./models/lista_verbos.pickle"
URL_VERBOS_IRREGULARES = "./models/verbos_irregulares.pickle"
URL_DIALOGOS = "./data/dialogos"
URL_MODELO = "./models/modelo"