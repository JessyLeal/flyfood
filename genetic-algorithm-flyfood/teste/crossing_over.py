from math import floor
from random import randint


def cro(FatherA = list, FatherB = list):
    lenF = len(FatherB)
    sonA, sonB = [None]*lenF, [None]*lenF
    i, j, z= 0, 0, 1

    if lenF%2 == 0: 
        l = floor(lenF/2)-1
    else: 
        l = floor(lenF/2)


    while i != lenF:
        r = randint(0, lenF-1)
        if i > l: 
            if FatherA[r] not in sonB and FatherA[r] not in sonA :
                if sonB[i] == None:
                    sonB[i] = FatherA[r]
                    i +=1

            # sonB[i] = FatherA[i]
        else:  
            if FatherA[r] not in sonA:
                if sonA[i] == None:
                    sonA[i] = FatherA[r]
                    i +=1
    
    while True :
        if z+l == lenF:
            z = 0
            break
        r = randint(0, lenF-1)

        if FatherB[r] not in sonA:
            if sonA[l+z] == None:
                sonA[l+z] = FatherB[r]
                z+=1

    if lenF%2 == 0:  lenF-=1

    while z+l != lenF:
        r = randint(0, lenF-1)

        if FatherB[r] not in sonB:
            if sonB[l-z] == None:
                sonB[l-z] = FatherB[r]
            z+=1

    return sonA, sonB


    # while True: #mudar essa parte
    #     if l+z == lenF or j==len(FatherB): 
    #         z, j = 0, 0
    #         break
    #     if FatherB[j] not in sonA:
    #         sonA[l+z] = FatherB[j]
    #         z+=1
        
    #     j+=1

    # while True: #mudar essa daqui tbm
    #     if l+z == lenF or j==len(FatherB):
    #         break
    #     if FatherB[j] not in sonB:
    #         sonB[z] = FatherB[j] 
    #         z+=1
    #     j+=1

    # return sonA, sonB


# print(cro(['D', 'A', 'C', 'B', 'E'], ['A','E','B', 'D', 'C']))
# p = [[['D', 'A', 'C', 'B', 'E'], ['A','E', 'C', 'D', 'B']], [['A', 'D', 'E', 'B', 'C'], ['D','E','B', 'A', 'C']], [['E', 'A', 'B', 'C', 'D'], ['E','B','A', 'D', 'C']]]
# x = [['A','E', 'C', 'D', 'B'], ['D', 'A', 'C', 'B', 'E']]
# x = [['A','E', 'C', 'D', 'B'], ['D', 'A', 'C', 'B', 'E']]
p1 = ['D', 'A', 'C', 'B', 'E']
p2= ['A','E', 'C', 'D', 'B']
print(cro(p1, p2))
print(cro(p2, p1))

# print(x in p)



