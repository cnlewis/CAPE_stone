# -*- coding: utf-8 -*-
"""

"""
import pandas as pd
import re
from collections import Counter
import enchant as ench
import pickle
import nltk
from PyDictionary import PyDictionary
import timeit

dictionary=PyDictionary()

"""
Leemos el fichero corregido y con el idioma asignado y nos quedamos con los campos que nos interesan
"""
df_words = pd.read_csv('C:/Users/Paqui/Programas Python/Capstone project/queries003_corrected.csv')
df_words1 = df_words[['customer','query_2', 'language']]


"""
Seleccionamos las queries en inglés y vemos cuantas hay
"""
df_words2 = df_words1[df_words1['language'] == 'en']

df_words2.head()
print "Querys corregidas en todos los idiomas ",    df_words1['query_2'].count()
print "Querys en inglés ",    df_words2['query_2'].count()

"""
Creamos un variable string juntando todas las queries. Ponemos en minúsculas todas las 
palabras
"""
size =  int(df_words2['query_2'].count() -1)
print size
df_words3 = df_words2.iloc[0:size, 1]
string = pd.DataFrame(' '.join(df_words3.tolist()), columns=['query_2'], index=[0]).iloc[0,0]
string = string.lower()
print string

"""
Definimos el idioma que vamos a usar para la libreria Enchant y el vocabulario inglés de 
la libreria nltk
"""
diction = ench.Dict("en_UK")
english_vocab = set(w.lower() for w in nltk.corpus.words.words())

"""
Definimos la función que nos permitirá buscar una palabra en el diccionario de Python y ver
si la encuentra (se puede buscar en el normal o usando la versión google)
"""

def dictionary_meaning(word):
    try:
        meaning_1 = dictionary.meaning(word) 
        
    except:
        pass
    try:
        meaning_2 = dictionary.googlemeaning(word) 
         
    except:
        pass
    
    if meaning_1 == None and meaning_2 == None:
        return False
    else:
        return True



def words(text): return re.findall(r'\w+', text.lower())


"""
Comprobamos usando varios métodos si la palabra existe o no:
    libreria enchant 
    libreria nltk
    Diccionario python
En caso que no exista en ninguno no la adjuntaremos al contador final de palabras
Si la palabra ya ha sido chequeada entonces la adjuntmmos o no directamente
"""

WORDS = Counter(words(string))

print WORDS
string_errors = ""

start_time = timeit.default_timer()


inputfile_001 = open('C:/Users/Paqui/Programas Python/Capstone project/Counter copy/counter', 'rb')

WORDS_exist001 = Counter (pickle.load(inputfile_001))

inputfile_002 = open('C:/Users/Paqui/Programas Python/Capstone project/Counter copy/counter_002', 'rb')

WORDS_exist002 = Counter (pickle.load(inputfile_002))

WORDS_exist = WORDS_exist001 + WORDS_exist002
"""
Primero miramos si la palabara ya está en el diccionario procesado en pasos anteriores, si no
Comprobamos usando varios métodos si la palabra existe o no:
    libreria enchant 
    libreria nltk
    Diccionario python
En caso que no exista en ninguno no la adjuntaremos al contador final de palabras
Si la palabra ya ha sido chequeada entonces la adjuntmmos o no directamente
"""
for word in WORDS:
    if word in WORDS_exist.keys():
        pass
    else:
        if diction.check(word) == True:
            pass
        else:
            if word in english_vocab:
                pass          
            else: 
                if dictionary_meaning(word) == True: 
                    pass
                else:
                    string_errors = string_errors + " " + word
               
errors = string_errors.split()
print errors
stop_time = timeit.default_timer()    
for word in errors:
    del WORDS[word]
    
stop_time = timeit.default_timer()

print'Tiempo de ejecución',  stop_time - start_time

"""
Ahora creamos el contador con todas las palabras correctas seleccionadas que nos servirá
para corregir el spelling
"""
print "WORDS FINAL", WORDS

WORDS
with open('C:/Users/Paqui/Programas Python/Capstone project/counter_003', 'wb') as outputfile:
    pickle.dump(WORDS , outputfile)
    


errors
with open('C:/Users/Paqui/Programas Python/Capstone project/errors003_counter', 'wb') as outputfile:
    pickle.dump(errors , outputfile)
    
print 'FINISHED'
