#######################################
'''
class Pilha:
    def __init__(self):
        self.pilha = []

    def bota(self, a):
        self.pilha.append(a)

    def tira(self):
        return self.pilha.pop()
    
    def show(self):
        for i in self.pilha:
            print(i, end=' ')
        print()
'''
#######################################

s = list(map(str,input()))
#print(s)
del_abertos = ['(', '[', '{']
del_fechados = [')', ']', '}']

def teste(s):
    pilhav = []
    for i in s:
        if i in del_abertos:
            pilhav.append(i)
        elif i in del_fechados:
            p = del_fechados.index(i)
            if ((len(pilhav) > 0) and (del_abertos[p] == pilhav[-1])):
                pilhav.pop()
            else:
                return 'mal formado'
    if len(pilhav) == 0:
        return 'bem formado'
    else:
        return 'mal formado'

print(teste(s))