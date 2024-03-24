#Print de listas

# 2 Opções

# print('nromal')
# método join -> texto.join(lista)

produtos = ['apple tv', 'mac', 'iphone', 'Ipad', 'apple watch', 'mac book', 'airpods']
print(produtos)

print('\n'.join(produtos))

#Lembrando método split de strings:

# lista = texto.split(separador)

produtos2 = 'apple tv, mac, iphone'
lista = produtos2.split(',')
print(produtos2)