"""
    Uma função é chamada de Função de Ordem Superior se:
        - receber outras funções como parâmetro
        - retornar uma função como saída
"""

import requests

def busca_na_api(formato):
    API_URL = f"https://baconipsum.com/api/?type=meat-and-filler&paras=2&start-with-lorem=1&format={formato}"

    res = requests.get(API_URL)

    parser = parser_for(formato)

    return parser(res)


def parser_for(formato):
    if formato == "json":
        def json_parser(res):
            return res.json()

        return json_parser

    if formato == "text":
        def text_parser(res):
            return res.text

        return text_parser
    
    raise Exception("Formato invalido")



valor_parseado = busca_na_api("text")
print(valor_parseado)
