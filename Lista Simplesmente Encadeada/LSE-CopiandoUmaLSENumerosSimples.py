class Node:
    def __init__(self, numero):
        self.dado = numero
        self.next = None
    
    def getData(self):
        return self.dado
    
    def getNext(self):
        return self.next
    
    def setData(self, numero):
        self.dado = numero
    
    def setNext(self, prox):
        self.next = prox

class LSE:
    def __init__(self):
        self.head = None
    
    def addOrd(self, dado):
        nodo_novo = Node(dado)
        if self.head == None:       #se a cabeca da lista for vazia, ela recebe o novo nodo(valor)
            self.head = nodo_novo
            return
        else:
            nodo_atual = self.head      #logo, o nodo atual, recebe a cabeca
            while nodo_atual is not None and nodo_atual.dado <= dado:      #loop p percorrer a lista
                nodo_anterior = nodo_atual
                nodo_atual = nodo_atual.next
            if nodo_atual is self.head:
                aux = self.head
                self.head = nodo_novo
                nodo_novo.next = aux
            else:
                nodo_anterior.next = nodo_novo
                nodo_novo.next = nodo_atual
    
    def rev(self):
        nodo_anterior = None
        nodo_atual = self.head
        while nodo_atual != None:
            prox_nodo = nodo_atual.next
            nodo_atual.next = nodo_anterior
            nodo_anterior = nodo_atual
            nodo_atual = prox_nodo
        self.head = nodo_anterior
            
    
    def show(self):
        elementos = self.head
        if elementos is None:
            print("Lista vazia")
        while elementos:
            print(elementos.dado, end=' ')
            elementos = elementos.next
    
    def len(self):
        if self.head == None:
            return 0
        nodo_atual = self.head
        tam = 0
        while nodo_atual:
            tam += 1
            nodo_atual = nodo_atual.next
        return tam


sll = LSE()
l2 = LSE()
l = []

l = list(map(int, input().split()))

for i in range(0, len(l)):
    sll.addOrd(l[i])

l2 = sll
l2.rev()

l2.show()