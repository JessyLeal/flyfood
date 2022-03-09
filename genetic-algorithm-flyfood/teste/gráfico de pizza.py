import matplotlib.pyplot as plt

points= {'ABCD': 0.15, 'ADCB': 0.25, 'ACBD':0.20, 'CDAB':0.4}
# labels = 'ABCD', 'ADCB', 'ACBD', 'CDAB'
# size = [1, 2, 3, 4]
ranking = {'ABCD': 0.15, 'ADCB': 0.40, 'ACBD':0.60, 'CDAB':1}
fig1, axl = plt.subplots()

axl.pie(points.values(), labels=points.keys(), shadow=True, autopct='%1.2f%%' ,startangle = 90)

axl.axis('equal')
plt.show()