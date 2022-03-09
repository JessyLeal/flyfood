from random import sample
population = [1,2,3,4,5]
k = len(population)
for i in range(10):
    print(sample(population, k))

