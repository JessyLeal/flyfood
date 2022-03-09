file = open('teste.txt', 'r')
from time import time
all_routes = []
inicio = time()
def in_data():
    """Na funçao `in_data` é tratado os dados da matriz lida do arquivo txt."""
    points = {}
    i, j =  map(int, file.readline().split(' '))
    for l in range(i):
        line = file.readline().split(' ')
        if len(line)==j:
            for colun in range(len(line)):
                if line[colun].find("\n")!= -1:
                    line[colun] = line[colun][-2]
                if line[colun] not in '0' :
                    points[line[colun]] = (l, colun)
        else:
            raise ValueError('Incosistence number of coluns in line. ')
    return points

def perm(points, i=0):
    """Na função `perm` é obtido todos os arranjos possíveis de n pontos sendo p = n. """
    if i == len(points):   	  
        all_routes.append('R'+"".join(points)+'R')

    for j in range(i, len(points)):
            routes = [i for i in points]
            routes[i], routes[j] = routes[j], routes[i]
            perm(routes, i+1)
    return all_routes

def min_cost(routes, points):
    """A função `min_cost` receberá todas as possíveis rotas dos pontos da matriz e um dicionário com as coordenadas de cada ponto presente na matriz e retornará a rota menos custosa. """
    routes_costs = {}
    mn = 10**6
    smaller = str
    for r in routes:
        cost = 0
        for p in range (len(r)-1):
            cost+= abs(points[r[p+1]][0] - points[r[p]][0]) + abs(points[r[p+1]][1] - points[r[p]][1])
        v = [i for i in r[1:(len(r)-1)]]
        routes_costs[" ". join(v)] = cost

    for i in routes_costs.items():
        k , vl = i
        if vl< mn:
            smaller = k
            mn = vl    

    return print(smaller)

in_= in_data()
min_cost(perm([p for p in in_ if p !='R']), in_)
fim = time()
print(fim-inicio)

