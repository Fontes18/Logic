#Como descobrir o índice de um item de uma lista?
#i = lista.index('intem')

#Exemplo

"""Digamos que você puxou do banco de dados da sua empresa uma lista
com todos os produtos que a empresa vende e a quantidade
em estoque de todos eles.
"""

produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno']
estoque = [100, 150, 100, 120, 70, 180, 80]

"""e agora, como eu faço para descobrir a quantidade em estoque
do produto geladeira?"""

# i = produtos.index('geladeira')
# qtde_estoque = estoque[i]

"""Crie um programa para fazer uma consulta de estoque. O usuário
do programa deve inserir o nome do produto e, caso ele não exista na lista,
ele é avisado, caso exista, o programa deve retornar a quantidade 
de unidades em estoque do produto"""
def retornarestoque(produtos,estoque):
    escolha = input('Digite o nome do produto que deseja: ')
    i = produtos.index(escolha)
    qtde_estoque = estoque[i]
    if escolha in produtos:
        print(f'o número de unidades no estoque é: {qtde_estoque}')
    else:
        print(f'não esxiste o produto {qtde_estoque} no estoque')

retornarestoque(produtos, estoque)