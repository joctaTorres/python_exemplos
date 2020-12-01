"""
    Currying é a prática de simplificar a execução de uma função
    que precisa de vários argumentos em funções sequenciais de argumento único.
"""

# Exemplo 1:

def potencia(x):
    def elevado(y):
        return x ** y
    
    return elevado

potencia(2)(2)



# Exemplo 2:
def chain(*functions):
    def resolve(arg):
        result = None

        for function in reversed(functions):
            if not result:
                result = function(arg)
                continue
            
            result = function(result)
        
        return result
    
    return resolve



def hora_minuto(t):  
    return t * 60
      
def minuto_segundo(t): 
    return t * 60
    

chain(hora_minuto, minuto_segundo)(1)


