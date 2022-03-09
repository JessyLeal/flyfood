file = open('teste.txt', 'r')

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