from vetores import vrand, vrev, vord
from teste import teste
from bubble import bubblesort
from counting import countingsort
from heap import heapsort
from radix import radixsort


print("----------Bem-vindo ao ordenador de vetores!----------")
while True:
    print("\nEscolha qual método deseja usar:")
    print("1. Bubble sort")
    print("2. Counting sort")
    print("3. Heap sort")
    print("4. Radix sort")
    print("5. Sair")

    op = int(input("\nEntre com o número correspondente ao método:"))

    if op == 1:
        print("\n-----    Bubble sort    -----\n")
        for i in range(4):
            teste(vrand[i], bubblesort)
        print("------------------------------")
    elif op == 2:
        print("\n-----    Counting sort    -----\n")
        for i in range(5):
            teste(vrev[i], countingsort)
        print("------------------------------")
    elif op == 3:
        print("\n-----    Heap sort    -----\n")
        for i in range(5):
            teste(vrand[i], heapsort)
        print("------------------------------")
    elif op == 4:
        print("\n-----    Radix sort    -----\n")
        for i in range(5):
            teste(vord[i], radixsort)
        print("------------------------------")
    elif op == 5:
        print("\nPrograma encerrado.\n")
        break
    else:
        print("Opção invalida.")