"""
    Sintaxe:
        lambda <argumentos> : <expressão>
    
    Quando? Onde? PQ!?:

        Usamos funções lambda (anônimas) quando de uma função que não será usada novvamente no código.

        Geralmente o usamos como um argumento para uma função de ordem superior:
            - filter
            - map
            - sorted
            - groupby

        Para garantir que não sejam usadas apenas em higer-order functions,
        alguns linters fazem a checagem para garantir que o lambda não é armazenado em alguma variavel.

        Isso faz parte do PEP-8 https://www.python.org/dev/peps/pep-0008/#programming-recommendations
"""

# Exemplo 0 - Sem argumento 😶
from uuid import uuid4

gera_cadatro = lambda: hash(uuid4())



# Exemplo 1 - Funções simples 🏳️

def dobra(valor):
    return valor * 2

dobra_lambda = lambda valor : valor * 2



# Exemplo 2 - Ordenando uma lista de objetos 🥇🥈🥉
from dataclasses import dataclass, field
from uuid import uuid4

@dataclass
class Aluno:
    nome : str
    idade: int
    matricula: int = field(default_factory=lambda: hash(uuid4()))
    # função anonima sendo usada como 'factory'


alunos = [
    Aluno("João", 27),
    Aluno("Maria", 22),
    Aluno("Lara", 22),
    Aluno("Rodrigo", 21)
]

alunos_ordenados = sorted(alunos, key=lambda aluno: aluno.idade)




# Exemplo 3 - Filtrando uma lista 🗑️

lista_qualquer = [1,2,3,None,4, "cinco", 6]

# por listcomp
lista_filtrada = [valor for valor in lista_qualquer if isinstance(valor, int)]


# filter + lambda
lista_filtrada_2 = list(
    filter(
        lambda valor: isinstance(valor, int),
        lista_qualquer
    )
)



# Exemplo 4 - Map! 🆕
nova_lista = list(
    map(
        lambda x: x + 1,
        [3,5,7]
    )
)
