num = int(input())
base = int(input())

saida = []
while num > 1:
    saida.append(int(num % base))
    num = num/base

list.reverse(saida)
saida = "".join(map(str, saida))

print(saida)