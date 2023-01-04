class Node:
    def __init__(self, nome, numero):
        self.dado = nome
        self.idade = numero
        self.next = None
    
    def getData(self):
        return self.dado
    
    def getNext(self):
        return self.next
    
    def setData(self, nome, numero):
        self.dado = nome
        self.idade = numero
    
    def setNext(self, prox):
        self.next = prox

class LSE:
    def __init__(self):
        self.head = None

    def addFront(self, dado):
        nodo_novo = Node(dado)
        nodo_novo.next = self.head
        self.head = nodo_novo

    def addEnd(self, dado):
        nodo_novo = Node(dado)
        if self.head is None:
            self.head = nodo_novo
            return
        nodo_atual = self.head
        while nodo_atual.next is not None:
            nodo_atual = nodo_atual.next
        nodo_atual.next = nodo_novo
    
    def addOrd(self, dado, idade):
        nodo_novo = Node(dado, idade)
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
            print("Idade:", elementos.idade, "Nome:", elementos.dado)
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
    
    def get(self, idx):
        if idx >= self.len() or idx < 0:
            print("Indice fora do alcance")
            return None
        idx_atual = 0
        nodo_atual = self.head
        while nodo_atual != None:
            if idx_atual == idx:
                return int(nodo_atual.dado)
            nodo_atual = nodo_atual.next
            idx_atual += 1

pessoas = LSE()
pessoasinv = LSE()

n = int(input("Entre com o numero de pessoas:"))

for i in range (0, n):
    strc = list(map(str, input("Entre com o nome e idade:").split()))
    idade = int(strc.pop(-1))
    nome = ' '.join(strc)
    pessoas.addOrd(nome, idade)
#pessoas.show()

pessoasinv = pessoas
pessoasinv.rev()
pessoas.show()