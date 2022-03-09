from in_data import in_data
from random import choice
import operator

from GA import *  
class main:
    DeliveryPoints = in_data()

    nth_population = 0
    
    BestSolution = None

    population= Inicial_Population(DeliveryPoints) 

    while nth_population < EndPoint:

        nth_population+=1

        Population_Fitness = PopulationFitness(population, DeliveryPoints) 

        if BestSolution == None:
            BestSolution = max(Population_Fitness.items(), key=operator.itemgetter(1))
        else: 
            b = max(Population_Fitness.items(), key=operator.itemgetter(1))
            if b[1] > BestSolution[1]:
                BestSolution =  max(Population_Fitness.items(), key=operator.itemgetter(1))

        selection = Selection(Population_Fitness) 

        i = 0

        #crossing over
        NextGeneration = [] 

        while i < PopulationSize:
            while True:
                p, j = choice(list(selection.values())), choice(list(selection.values()))

                p1 = [i for i in p]
                p2 = [i for i in j]

                while p2 == p1:
                    j = choice(list(selection.values()))
                    p2 = [i for i in j]

                if p2 != p1: break

            f1, f2 = CrossingOver(p1, p2)
            if f1 not in NextGeneration: 
                NextGeneration.append(f1)
                i+=1
            if f2 not in NextGeneration: 
                NextGeneration.append(f2)
                i+=1

        #mutation

        population = Mutation(NextGeneration)

    print(BestSolution[0])

