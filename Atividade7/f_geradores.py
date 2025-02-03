def pares(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            yield i

def quadrados():
    soma = 0
    for i in range(1, 11):
        soma += i*i
        yield soma

def fib():
    sequencia = [0,1]
    yield 0
    yield 1
    while True:
        proximo = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo)
        yield proximo

primo = lambda num: True if 0 in [num % k for k in range(2, num)] else False

def i_f(inicio, fim):
    for i in range(inicio, fim + 1):
        if primo(i):
            yield i

def limite_fibonacci(n):
    ultimo = 1
    penultimo = 0
    yield 0
    while ultimo <= n:
        yield ultimo
        x = penultimo + ultimo
        penultimo = ultimo
        ultimo = x


def testes():
    print([x for x in pares(50)],"\n")
    print([x for x in quadrados()],"\n")
    fibb = fib()
    [print(next(fibb)) for _ in range(10)]
    print([x for x in i_f(10,50)])
    print([x for x in limite_fibonacci(10000)])

testes()