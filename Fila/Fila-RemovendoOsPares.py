class Fila:
    def __init__(self):
        self.fila = []

    def enqueue(self, elem):
        self.fila.append(elem)
    
    def dequeue(self):
        if len(self.fila) != 0:
            self.fila.pop(0)
    
    def front(self):
        return self.fila[0]
    
    def show(self):
        print(self.fila)
    
    def tiraPar(self):
        self.fila = [i for i in self.fila if i % 2 != 0]

q = Fila()
lista = list(map(int, input().split()))

for i in range (0, len(lista)):
    q.enqueue(lista[i])

#q.show()
q.tiraPar()
q.show()