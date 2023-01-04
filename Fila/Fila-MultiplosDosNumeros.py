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

q0 = Fila()
q3 = Fila()
q5 = Fila()
qr = Fila()
lista = list(map(int, input().split()))

for i in range (0, len(lista)):
    q0.enqueue(lista[i])

for i in range (0, len(lista)):
    aux = q0.front()
    if aux % 3 == 0:
        q3.enqueue(aux)
    if aux % 5 == 0:
        q5.enqueue(aux)
    if (aux % 3) != 0 and (aux % 5) != 0:
        qr.enqueue(aux)
    q0.dequeue()
    q0.enqueue(aux)

q3.show()
q5.show()
qr.show()