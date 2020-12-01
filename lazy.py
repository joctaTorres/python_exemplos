"""
    Lazy Evaluation é uma estratégia que atrasa a avaliação de uma expressão
    até que seu valor seja necessário.
"""



# Exemplo 1 💤

from time import sleep

dorme = [sleep(1), sleep(2), sleep(2)][0]


# O código só é avaliado quando necessário

def lazy_function():
    [sleep(1), sleep(2), sleep(2)]
    return None

def lazy_error():
    raise Exception("Erooor!")



# Exemplo 2: Geradores (mas não de energia) 💡

# Medindo a memória antes e depois:
from guppy import hpy; h=hpy()
h.heap()

# Usa mto espaço:
not_lazy = [x/2 for x in range(50000)]

# Usa quase nenhum espaço:

gen = (x/2 for x in range(50000)) 

def gen():
    for x in range(50000):
        yield x/2


# map(), range(), zip() são funções nativas lazy
