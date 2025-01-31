
def maiusculas():
    lista = ["python", "lambda", "map"]
    maiusculas = map(lambda x: str(x).upper(),lista)
    return [x for x in maiusculas]

def raizes():
    lista = [2,3,4]
    raiz = map(lambda x: x**0.5, lista)
    return [x for x in raiz]


def dics(x: str):
    qtd = x.split(" ")
    return {"qtd_palavras": len(qtd), "qtd_caracteres": len(x)}

def strings():
    lista =  ["Python é incrível", "Lambda são úteis", "Map é funcional"]
    dicts = map(lambda x: dics(x), lista)
    return [x for x in dicts]

def main():
    print(maiusculas())
    print(raizes())
    print(strings())

main()