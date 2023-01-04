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

f = Fila()
s = list(input().strip())

for i in range (0, len(s)):
    f.enqueue(s[i])

v = []
for i in range (0, len(s)):
    aux = f.front()
    if aux == '(':
        v.append(aux)
    elif aux == ')':
        if len(v) > 0 and ('(' == v[-1]):
            v.pop()
        else:
            print("ERRADO: Fecha um parênteses sem ter aberto")
            v.append(False)
    f.dequeue()
    f.enqueue(aux)
#print(v)
if len(v) == 0:
    print("CERTO")
elif v[0] == '(':
    print("ERRADO: Abre parênteses sem o fecha parênteses correspondente")
#f.show()