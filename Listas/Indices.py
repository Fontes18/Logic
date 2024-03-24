"""Estrutura:
lista =[valor, valor, valor, valor]

lista[i]-> é o valor de índice i da lista
Obs: Lembre que no python o índice começa em 0, então o primeiro item
de uma lista é o item lista[0]

Para substituir um valor de uma lista você pode fazer:
lista[i] = novo_valor

Listas de produtos de uma loja:
"""
produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet']

#lista de unidades vendidas de cada produto da loja

vendas = [1000, 1500, 350, 270, 900]

#Nesse caso, as listas funcionam da seguinte forma:

"""Produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet']
                 0,      1,        2,        3,         4
    vendas  = [1000,    1500,     350,      270,       900]"""

print(f'Vendas do produto {produtos[0]} foram {vendas[0]} unidades')