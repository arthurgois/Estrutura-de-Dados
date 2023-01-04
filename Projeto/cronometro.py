'''
def cronometro(end, start):       #criei uma funcao que serve como cronometro e imprime na tela o tempo em hr, min e seg.
    tempo = end - start
    tempoH = (tempo/60)/24
    horas = int(tempoH)

    tempoM = (tempoH - horas)*24
    minutos = int(tempoM)

    tempoS = (tempoM - minutos)*60
    segundos = int(tempoS)

    tempoMS = (tempoS - segundos)*1000
    ms = int(tempoMS)

    print(horas, "h, ", minutos, "min, ", segundos, "seg,", ms,"ms.\n")
'''
def cronometro(end, start):       #criei uma funcao que serve como cronometro e imprime na tela o tempo em hr, min e seg.
    tempo = end - start

    print(tempo ,"s.\n")