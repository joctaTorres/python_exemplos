"""
    Temos um closure quando uma função aninhada faz referência a um valor em seu escopo envolvente.
"""

# Exemplo 1:
def multiplicador_de(numero):
    def multiplicador(x):
        return x * numero

    # retorna a referência para a função multiplicador
    return multiplicador

pares = multiplicador_de(2)


# Exemplo 2: Decorators

def soma(x, y):
    return x + y


def imprime_operacao(op):

    def imprime(x, y):
        res = op(x, y)
        print(f"Resultado: {op.__name__}({x},{y}) = {res}")

    return imprime

imprime_soma = imprime_operacao(soma)
imprime_soma(2, 2)


@imprime_operacao
def mutiplicacao(x, y):
    return x * y

# multiplicacao = imprime_operacao(multiplicacao)