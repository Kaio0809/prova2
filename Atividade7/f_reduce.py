from functools import reduce

def produto(lista):
    return reduce(lambda x, y: x * y, lista)

def maior(lista):
    return reduce(lambda x, y: x if x >= y else y, lista)

def dict(lista):
    somas = reduce(lambda x, y: {**x, y[0]: x.get(y[0], 0) + y[1]}, lista, {})
    return somas
    


def testes():
    print("Produto: ", produto([1,2,3,4,5]))
    print("Maior: ", maior([1,20,50,3,1000,5, 10]))
    print("Pares: ", dict([("a", 2),("b", 15),("a", 4),("c", 8),("b", 5)]))

testes()