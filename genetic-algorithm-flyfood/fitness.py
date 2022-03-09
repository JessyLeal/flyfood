def PopulationFitness(population = list, DeliveryPoints = dict):
    fitness = {}
    def InsertR(x):
        x.insert(0,'R')
        x.insert(len(x),'R')
    for individual in population:
        cost = 0
        InsertR(individual)
        for coordinate in range (len(individual)-1):
            cost+= abs(DeliveryPoints[individual[coordinate+1]][0] - DeliveryPoints[individual[coordinate]][0]) + abs(DeliveryPoints[individual[coordinate+1]][1] - DeliveryPoints[individual[coordinate]][1])
        v = [i for i in individual[1:(len(individual)-1)]]
        fitness["".join(v)] = 1/cost
    return fitness


population = [['A', 'B', 'C', 'D'], ['A', 'B', 'C', 'D'], ['C','D', 'B', 'A'], ['A', 'C', 'D', 'B']]
dp = {'A' : (0,1), 'B': (2,1), 'C':(3,2), 'D':(1,3), 'R':(0,0) }

print(PopulationFitness(population, dp))