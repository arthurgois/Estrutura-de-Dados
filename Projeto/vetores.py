from random import randint #, shuffle

v1 = list(range(1,101))
v2 = list(range(1,1001))
v3 = list(range(1,10001))
v4 = list(range(1,100001))
v5 = list(range(1,150001))


vord = [v1.copy(), v2.copy(), v3.copy(), v4.copy(), v5.copy()]

vrev= []
for i in range(5):
    vrev.append(vord[i].copy())
    vrev[i].reverse()

#shuffle(v1), shuffle(v2), shuffle(v3), shuffle(v4), shuffle(v5)
#vrand = [v1, v2, v3, v4, v5]

v6 = list(); v7 = list(); v8 = list(); v9 = list(); v10 = list()
vrand = [v6, v7, v8, v9, v10]
for i in range (100):
    vrand[0].append(randint(0,10000))
for i in range (1000):
    vrand[1].append(randint(0,100000))
for i in range (10000):
    vrand[2].append(randint(0,1000000))
#for i in range (100000):
#    vrand[3].append(randint(0,10000000))
for i in range (150000):
    vrand[3].append(randint(0,10000000))

#vrand[0] = [54342432, 54214134, 54214123, 54231449, 54254232]
#print(vrand[2])
#vrand[0][-1] = 6536536