class Node:
    def __init__(self, tarefa, prioridade):
        self.prev = None
        self.task = tarefa
        self.prior = prioridade
        self.next = None

    def getTask(self):
        return self.task

    def setTask(self, tarefa):
        self.task = tarefa
    
    def getPrior(self):
        return self.prior
    
    def setPrior(self, prioridade):
        self.prior = prioridade

    def getNext(self):
        return self.next
    
    def setNext(self, next):
        self.next = next

    def getPrev(self):
        return self.prev

    def setPrev(self, prev):
        self.prev = prev

class LDE:
    def __init__(self):
        self.head = None

    def add(self, tarefa, prioridade):
        if self.buscarap(tarefa) == False:
            node = Node(tarefa, prioridade)

            if self.head == None:
                self.head = node
                return True
            
            elif node.getPrior() > self.head.getPrior():        #se a prioridade for maior que a do cabeca ele entra atrás
                aux1 = self.head
                node.setNext(aux1)
                self.head.setPrev(node)
                self.head = node
                return True
            
            else:
                aux1 = self.head
                aux2 = self.head.getNext()
                flag_insert = False
                while aux2 != None:
                    if aux2.getPrior() < node.getPrior():
                        flag_insert = True
                        break
                    aux1 = aux1.getNext()
                    aux2 = aux2.getNext()
                    
                if flag_insert == True:
                    node.setNext(aux1.getNext())
                    node.setPrev(aux1)
                    aux1.setNext(node)
                    aux2.setPrev(node)
                    return True
                else:
                    aux1.setNext(node)
                    aux1.getNext().setPrev(aux1)
                    return True
            
        else:
            return False
    
    def buscarap(self, atv):
        aux = self.head
        while aux != None:    
            if aux.getTask() == atv:
                return True
            aux = aux.getNext()
        return False
    
    def search(self, atv):
        aux = self.head
        cont = 0
        while aux != None:
            if aux.getTask() == atv:
                print("serão executadas ", cont, " tarefas antes da informada", sep='', end='\n')
            aux = aux.getNext()
            cont += 1
        return False
    
    def buscaPrior(self, prior):
        aux = self.head
        flag = False
        while aux != None:
            if aux.getPrior() == int(prior):
                print("Descrição : ", aux.getTask(), sep='', end='\n')
                flag = True
            aux = aux.getNext()
        if flag is False:
            print("nenhuma tarefa como esse prioridade foi encontrada")
    
    def show(self):
        if self.head != None:
            aux = self.head
            while aux.getNext() != None:
                print("Descricao: ", aux.getTask(), ", Prioridade: ", aux.getPrior(), sep='', end='\n')
                aux = aux.getNext()
            if aux.getNext() == None:
                print("Descricao: ", aux.getTask(), ", Prioridade: ", aux.getPrior(), sep='', end='\n')
    
    def alterar(self, atv, newprior):
        if (int(newprior) >= 1) and (int(newprior) <= 10):
            aux = self.head
            while aux != None:
                if aux.getTask() == atv:
                    self.cancelar(atv)
                    self.add(atv, newprior)
                    print("tarefa alterada com sucesso")
                aux = aux.getNext()
        else:
            print("tarefa não alterada por não ter prioridade válida")
    
    def executarTarefa(self):
        self.head = self.head.getNext()
        self.head.setPrev(None)
        print("Tarefa executada")
    
    def cancelar(self, atv):
        if self.buscarap(atv) == True:
            if self.head.getTask() == atv and self.head.getNext() == None:
                self.head = None
                return True
            elif self.head.getTask() == atv:
                self.head = self.head.getNext()
                self.head.setPrev(None)
                return True
            else:
                aux1 = self.head
                aux2 = self.head.getNext()
                while aux2 != None:
                    if aux2.getTask() == atv:
                        #aux1.setNext(aux2.getNext())
                        aux2 = aux2.getNext()
                        aux1.setNext(aux2)
                        if aux2 != None:
                            aux2.setPrev(aux1)
                        break
                    aux1 = aux1.getNext()
                    aux2 = aux2.getNext()
                return True
        else:
            return False




dll = LDE()
op = True

while op != "H":
    #print("Entre com a operação, a tarefa e a prioridade: ")
    n = list(input().split())
    op = n[0]

    if op == "A":
        atv = n[1]
        prior = n[2]
        #print(int(prior))
        if (int(prior) >= 1) and (int(prior) <= 10):
            ret = dll.add(atv, int(prior))
            if ret == True:
                print("tarefa adicionada com sucesso")
            elif ret == False:
                print("já tem uma atividade com essa descrição")

        else:
            print("tarefa não inserida por não ter prioridade válida")        
    
    elif op == "B":
        atv = n[1]
        dll.search(atv)
    
    elif op == "C":
        dll.executarTarefa()
    
    elif op == "D":
        atv = n[1]
        ret = dll.cancelar(atv)
        if ret == True:
            print("Tarefa removida")
        elif ret == False:
            print("Tarefa inexistente")
    
    elif op == "E":
        prior = n[1]
        dll.buscaPrior(int(prior))
    
    elif op == "F":
        dll.show()
    
    elif op == "G":
        atv = n[1]
        newprior = int(n[2])
        dll.alterar(atv, newprior)
    
    elif op == "H":
        print("programa encerrado")