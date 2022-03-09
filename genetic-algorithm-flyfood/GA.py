from random import sample, random, choices, choice, randint
from math import floor

PopulationSize = 10
MutationCTax = 0.1
BreedTax = 1
MutationGTax = 0.05
EndPoint = 10

def Inicial_Population(DeliveryPoints):

    population = [i for i in DeliveryPoints.keys() if i!= 'R']

    inicial_population = []
    i = 0
    while i != PopulationSize:
        ip = sample(population, len(population))
        if ip not in  inicial_population:
            inicial_population.append(ip)
            i +=1
    return inicial_population


def PopulationFitness(population, DeliveryPoints):
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

        fitness["". join(v)] = 1/cost
    return fitness

def Selection(PopulationFitness): #rank based probability

    #ranking
    Ranking_V = []
    Ranking_K= []

    v = 1
    w = sum(range(len(PopulationFitness)+1))

    for i in sorted(PopulationFitness, key = PopulationFitness.get):
        Ranking_K.append(i)
        if len(Ranking_V) == 0:
            Ranking_V.append(v/w)
        else:
            Ranking_V.append( v/w + Ranking_V[-1])
        v +=1

    #selection

    selection = {}
    i = 1
    while True:
        r = random()
        for index in range(len(Ranking_V)):
            if index == 0:
                if r <= Ranking_V[index] :
                    selection[f"parent{i}"]=Ranking_K[index]
                    i+=1
            else:
                if r <= Ranking_V[index] and r > Ranking_V[index-1] and Ranking_K[index] not in selection.values():
                    selection[f"parent{i}"]=Ranking_K[index]
                    i+=1
        if i == 7: return selection

def CrossingOver(FatherA = list, FatherB = list):
    lenF = len(FatherB)
    sonA, sonB = [None]*lenF, [None]*lenF
    i, z= 0, 1

    if lenF%2 == 0: 
        l = floor(lenF/2)-1
    else: 
        l = floor(lenF/2)


    while i != lenF:
        if i == lenF-1:
            if sonB[i] == None:
                for j in FatherA:
                    if j not in sonB and j not in sonA:
                        sonB[i] = j
                        i+=1
        else:
            r = randint(0, lenF-1)
            if i > l: 
                if FatherA[r] not in sonB and FatherA[r] not in sonA :
                    if sonB[i] == None:
                        sonB[i] = FatherA[r]
                        i +=1

            else:  
                if FatherA[r] not in sonA:
                    if sonA[i] == None:
                        sonA[i] = FatherA[r]
                        i +=1
    while True :
        if z+l == lenF:
            z = 0
            break
        if z+l == lenF-1:
            if sonA[z+l] == None:
                for j in FatherB:
                    if j not in sonA:
                        sonA[z+l] = j
                        z+=1
        else:
            r = randint(0, lenF-1)

            if FatherB[r] not in sonA:
                if sonA[l+z] == None:
                    sonA[l+z] = FatherB[r]
                    z+=1

    if lenF%2 == 0:  lenF-=1

    while z+l != lenF:
       if z+l == lenF-1:
            if sonB[l-z] == None:
                for j in FatherB:
                    if j not in sonB:
                        sonB[l-z] = j
                        z+=1
                        
       else:
            r = randint(0, lenF-1)

            if FatherB[r] not in sonB:
                if sonB[l-z] == None:
                    sonB[l-z] = FatherB[r]
                z+=1

    return sonA, sonB


def Mutation(Paths): 
    for individual in range(len(Paths)): 
        pc, pg = random(), random()
        if pc <= MutationCTax: 
            for gene in range(len(Paths[individual])):
                pg = random()
                if pg<= MutationGTax:
                    while True: 
                        s = choices(Paths[individual])
                        if s != Paths[individual][gene]: break

                    a, b = Paths[individual].index(s[0]), gene
                    Paths[individual][a], Paths[individual][b] = Paths[individual][b], Paths[individual][a]
    return Paths
