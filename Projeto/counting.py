def countingsort(lista):
    max_element = int(max(lista))
    min_element = int(min(lista))
    k = max_element - min_element + 1
    
    count_arr = [0 for _ in range(k)]   # count array inicia zerado do tamanho do rangeofelements(k). Ele vai guardando no vetor count as ocorrencias individuais
    output_arr = [0 for _ in range(len(lista))]         # elementos de saida inicia zerado do tamanho do vetor original

    #print(count_arr)
    #print(output_arr)
    #print(len(count_arr))
 
    # guarda a contagem de cada elemento
    for i in range(0, len(lista)):
        count_arr[lista[i]-min_element] += 1
    
    #print(count_arr)

    for i in range(1, len(count_arr)):      # muda o count_arr[i] para que ele receba o atual
        count_arr[i] += count_arr[i-1]      # posição desse elemento no vetor de saida
    
 
    # controi o vetor de saida
    for i in range(len(lista)-1, -1, -1):
        output_arr[count_arr[lista[i] - min_element] - 1] = lista[i]
        count_arr[lista[i] - min_element] -= 1
        #print(output_arr)
 
    # copia o vetor de saida para lista[]
    for i in range(0, len(lista)):
        lista[i] = output_arr[i]

#lista = [3,2,4,7,2,4,7,9,17453,3]
#countingsort(lista)
#print(lista)