def bubblesort(lista):

    for i in range((len(lista))-1):                         # percorrendo todos os elementos
        for j in range(0, (len(lista)-i)-1):                # a cada loop os ultimos i elementos ja estão em ordem
            if lista[j] > lista[j+1]:                       # percorrendo a lista de 0 a (tamanho da lista)-i-1
                lista[j], lista[j+1] = lista[j+1], lista[j] # caso o elemento atual seja maior que o próximo, trocam os elementos