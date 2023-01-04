lista = list(map(float,input().split()))
lista = list(map(int, lista))
print(lista)

n=0
m=0
while len(lista)>0:
    x = lista.pop(0)
    if (x%2 == 0):
        n += -1 * x
    else:
        m += x
print(n*m)
print(lista)