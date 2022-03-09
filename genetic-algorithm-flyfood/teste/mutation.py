from random import choices, random, choice

def mutation(paths):
    for individual in range(len(paths)):
        pc = random()
        if pc<=0.05: #0.1
            for gene in range(len(paths[individual])):
                pg = random()
                if pg<=0.05 : #0.05
                    while True: 
                        s = choices(paths[individual])
                        if s != paths[individual][gene]: break
                    a, b = paths[individual].index(s[0]), gene
                    paths[individual][a], paths[individual][b] = paths[individual][b], paths[individual][a]

    print(paths)
lista = [['A','B','C','D'], ['B','D','C','A'], ['D','C','A','B'], ['C','A','B','D']]
mutation(lista)
