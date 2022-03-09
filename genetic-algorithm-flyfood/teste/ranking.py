from random import random
import matplotlib.pyplot as plt

# um dict com a rota e sua nota de fitness
points = {
    'ABCD':12, 'BCDA':19, 'BADC':17, 'DCAB':14, 'CDBA':18, 'ACDB': 19, 'CDAB': 23, 'BDAC': 15
}
ranking_v=[]
ranking_k=[]

v = 1
w = sum(range(len(points)+1))
for i in sorted(points, key = points.get):
    ranking_k.append(i)
    if len(ranking_v) == 0:
        ranking_v.append(v/w)
    else:
        ranking_v.append( v/w + ranking_v[-1])
    v +=1


selecion = {}
i = 1
while True:
    r = random()
    for index in range(len(ranking_v)):
        if index == 0:
            if r <= ranking_v[index]:
                selecion[f"parent{i}"]=ranking_k[index]
                i+=1
        else:
            if r <= ranking_v[index] and r > ranking_v[index-1]:
                selecion[f"parent{i}"]=ranking_k[index]
                i+=1
    if i == 5: break
print(selecion)

# fig1, axl = plt.subplots()

# axl.pie(ranking_v, labels=ranking_k, shadow=True, autopct='%1.2f%%' ,startangle = 90)

# plt.show()
# print(ranking)
# print(sum(ranking.values()))

