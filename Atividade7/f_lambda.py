soma = lambda x,y: x+y
def teste_soma():
    print(soma(1, 2))
    print(soma(2, 2))
    print(soma(-2, 2))
    print(soma(1000, 50))

paridade = lambda x: True if x % 2 == 0 else False
def teste_paridade():
    print(f'10: {paridade(10)}')
    print(f'15: {paridade(15)}')
    print(f'0: {paridade(0)}')
    print(f'1: {paridade(1)}')
    print(f'1000: {paridade(1000)}')

def teste_quadrado(lista):
    quadrado = map(lambda x: x**2, lista)
    for elemento in quadrado:
        print(elemento)

converte = lambda x: 32 + (9*x/5)
arredonda = lambda x: int(x) if x % 1 < 5 else int(x + 1)

conversao_inteira = lambda y: arredonda(converte(y))
def teste_conversao():
    temps = [15, 3.8, 59.3, 99.999]
    for i in temps:
        print(conversao_inteira(i))
print("Conversão: ")
teste_conversao()
print("\nParidade: ")
teste_paridade()
print("\nQuadrados: ")
teste_quadrado([1,2,3,4,5,6,7,8,9,10])
print("\nSoma: ")
teste_soma()