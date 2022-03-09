from random import *

points = {
            'A': (1,2),
            'B':(0,9),
            'C':(1,9),
            'D':(2,3),
            'R':(0,0)
        }

population = [i for i in points.keys() if i!= 'R']
# print(population)
# population2= []
k = len(population)
lambda lista: lista.insert(0, 'R')

def inicial_population(p):
    def lamb(x):
        x.insert(0,'R')
        x.insert(len(x),'R')

    population_i=[sample(p, k) for i in range(20)]   
    list(map(lamb, population_i))
    return population_i  
    
    # for i in population_i: print(i)

# print(inicial_population(population))





def short_path(routes, points):
    routes_costs = {}
    mn = 10**6
    smaller = str
    for r in routes:
        cost = 0
        for p in range (len(r)-1):
            cost+= abs(points[r[p+1]][0] - points[r[p]][0]) + abs(points[r[p+1]][1] - points[r[p]][1])
        v = [i for i in r[1:(len(r)-1)]]
        routes_costs[" ". join(v)] = cost
    print(routes_costs)

    for i in routes_costs.items():
        k , vl = i
        if vl< mn:
            smaller = k
            mn = vl    
    return print(smaller) 

# short_path(inicial_population(), points)