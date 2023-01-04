import numpy as np
import matplotlib.pyplot as plt  # biblioteca para plotar gráficos

#tabelamentos ORD
#x = [100,1000,10000,100000,150000] 
#f = [0.0, 0.03191351890563965, 3.826925039291382, 354.5753653049469, 787.5887463092804]

#tabelamentos REV
#x = [100,1000,10000,100000,150000] 
#f = [0.0009975433349609375, 0.08178043365478516, 9.31391978263855, 905.2316131591797, 2027.4793527126312]

#tabelamentos RAND
x = [100,1000,10000,100000,150000] 
f = [0.0, 0.06283092498779297, 6.448749303817749, 661.9817333221436, 1480.9866366386414]


n = len(x)
A2 = [[0., 0., 0.],[0., 0., 0.], [0., 0., 0.]]  # matriz dos coeficientes do sistema linear
B2 = [0., 0., 0.]

for i in range(len(x)):
  A2[0][0] +=1
  A2[1][1] += x[i]*x[i]
  A2[2][2] += (x[i]*x[i])**2
  A2[0][1] += x[i]
  A2[0][2] += x[i]**2
  A2[1][2] += x[i]**3
  B2[0] += f[i]
  B2[1] += x[i]*f[i]
  B2[2] += (x[i]**2)*f[i]

A2[1][0] = A2[0][1]
A2[2][0] = A2[0][2]
A2[2][1] = A2[1][2]

[a2, b2, c2] = np.linalg.solve(A2, B2)   # resolucao do sistema linear

# definicao da funcao de ajustamento
def P2(c,b,a,t):
  return c*t*t + b*t + a

# impressao da funcao de ajuste
print('P(x) = ' ,c2,'*x^2 +' ,b2,'*x + ',a2, '   =>\nP(1000000) = ',P2(c2,b2,a2,1000000),'\n')

#grafico com a função de ajustamento e os dados originais
y = np.linspace(x[0],x[n-1]) #limites no eixo x
plt.plot(x,f,'o',y,P2(c2,b2,a2,y)) 
plt.legend(['Dados originais - ORD','P(x) = cx² + bx + a - ajuste quadrático'])
plt.xlabel('N de elementos') 
plt.ylabel('Tempo em segundos') 
plt.grid()
plt.show()