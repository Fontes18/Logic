#Juntar listas, Ordenar e cuidados especiais
# 2 Formas:

#lista1.extend(lista2)
#lista_nova = lista1 + lista2

#Obs: o método .append não junta listas, mas adiciona um valor no final da lista

produtos = ['apple tv', 'mac', 'iphone', 'Ipad', 'apple watch', 'mac book', 'airpods']
novos_produtos = ['iphone 12', 'ioculos']

# produtos.extend(novos_produtos)

produtos_juntos = produtos + novos_produtos
print(produtos_juntos)

# Cuidado

""" [1] + [2] não é a mesma coisa que 1 + 2, então cuidado sempre com 
o formato dos valores na hora de fazer opearções."""

vendas = [1000, 1500, 15000, 20000, 270, 900, 100, 1200]
vendas_iphonex = [15000]
vendas_iphone11 = [20000]

#Ordenar listas

vendas.sort(reverse=True)
print(vendas)