class FilaDupla:
    def __init__(self):
        self.fila = []

    def enqueueb(self, elem):       #insere no final
        self.fila.append(elem)
    
    def enqueuef(self, elem):       #insere no começo
        self.fila.insert(0, elem)
    
    def dequeuef(self):             #tira do começo
        if len(self.fila) != 0:
            self.fila.pop(0)
    
    def dequeueb(self):             #tira do final
        if len(self.fila) != 0:
            self.fila.pop(-1)
    
    def front(self):
        return self.fila[0]
    
    def back(self):
        return self.fila[-1]
    
    def show(self):
        print(self.fila)
    
    def regex(self):
        v = []
        while len(self.fila) > 1:
            front = self.fila.pop(0)
            back = self.fila.pop(-1)
            if front == back:
                v.append(True)
            elif front != back:
                v.append(False)
        if  v[0] == True:
            print("VERDADE")
        else:
            print("FALSO")

            

dq = FilaDupla()
s = list(input().strip())

for i in range (0, len(s)):
    dq.enqueueb(s[i])

#dq.show()
dq.regex()