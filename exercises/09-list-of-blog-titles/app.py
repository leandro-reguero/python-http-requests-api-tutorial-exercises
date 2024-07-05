import requests
from collections import defaultdict
import numpy as np


def get_titles():
    # Your code here
    # Primero llamamos la api y convertimos la respuesta json en dict
    url = 'https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php'
    response = requests.get(url)    
    data = response.json()

    # Ahora accedo a todos los posts de la respuesta
    posts = data['posts']

    #Quiero crear un diccionario con todos los títulos de los posts:
    # Primero ennumero los posts y creo listas vacias para los pares llave valor
    post_ix = np.arange(len(posts))
    keys = []
    values = []
    # ahora accedo a cada post y su título del blog y guardo ennumerado el titulo del post en keys,
    #  y el titulo correspondiente en values
    for i in post_ix:
        k = f'Title {i+1}'
        keys.append(k)
        v = posts[i]['title_plain']
        values.append(v)
    
    # ahora creo un diccionario con un loop para guardar el contenido de las listas keys, values en pares llave-valor
    title_dict = {keys[i]: values[i] for i in range(len(keys))}
    
    return title_dict





print(get_titles())