lista = ['oi', 'bem', 'meu']
a, b = lista.index('bem'), lista.index('meu')
lista[b], lista[a] = lista[a], lista[b]
print(lista)