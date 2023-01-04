import time
from cronometro import cronometro

def teste(lista, metodo):
    vteste = lista.copy()
    print("Ordenação de", len(vteste), "elementos:")
    print("Antes da ordenação:", end=' ')
    for i in range (5):
        print(vteste[i], sep='', end=' ')

    start = time.time()
    metodo(vteste)
    end = time.time()

    print("\nDepois da ordenação usando o método:", end=' ')
    for i in range (5):
        print(vteste[i], sep='', end=' ')
    print("\n\nA ordenação teve duração de: ", end='')
    cronometro(end,start)