def num_positivos(lista):
    positivos = filter(lambda x: True if x >= 0 else False, lista)
    return [x for x in positivos]

def palavras_curtas(lista):
    curtas = filter(lambda x: True if len(x) <= 5 else False, lista)
    return [x for x in curtas]

def inteiros(lista):
    multiplos = filter(lambda x: True if x % 3 == 0 or x % 5 == 0 else False, lista)
    positivos = filter(lambda x: True if x >= 0 else False, list(multiplos))
    return [x for x in positivos]
    

def testes():
    print("Filtro de Positivos: ", num_positivos([-10, 15, -20, 25, 0, 30]))
    print("Filtro de Palavras Curtas: ", palavras_curtas(["Abelha", "Caju", "Ameixa", "Beijo", "Pá", "Beleza"]))
    print("Filtro Múltiplos: ", inteiros([1, 3, 15, 5, 10, -3, -2, -20, 55, 103]))

testes()