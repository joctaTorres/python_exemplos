"""
    Uma função é chamada de Função de Ordem Superior se:
        - receber outras funções como parâmetro
        - retornar uma função como saída
    
    As funções que mostramos anteriormente:
        - filter
        - map
    São funções de ordem superior.

"""

# Exemplo 1 - O básico:
def inc(x):
    return x + 1

def dec(x):
    return x - 1

def opera(func, x):
    return func(x)



# Exemplo 2 :

import requests

# Uma função de ordem superior é flexivel
def escreve(get_valores):
    valores = get_valores()

    for valor in valores:
        print(valor)


def busca_na_api():
    API_URL = "https://baconipsum.com/api/?type=meat-and-filler&paras=5&format=text&start-with-lorem=1"

    res = requests.get(API_URL)
    text = res.text

    for linha in text.split(".")[:3]:
        yield linha.strip()


def busca_na_lista():
    exemplo = [
        "Bacon ipsum dolor amet aliquip turducken ullamco qui consectetur.",
        "Cow leberkas drumstick enim, bacon do kevin pork loin deserunt brisket dolore.",
        "Prosciutto picanha pig, bresaola occaecat exercitation anim cupim est."
    ]

    for linha in exemplo:
        yield linha




escreve(busca_na_api)

