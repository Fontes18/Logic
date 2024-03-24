#Adicionar e Remover itens de uma lista

# Adicionar :
# lista.append(item)

#Remover:
"""item_removido = lista.pop(indice)
lista.remove(item)"""

"""Digamos que você está construindo o controle de produtos da Apple.
e a Apple lançou o Iphone 11 e irá tirar dos estoques o Iphone X"""

produtos = ['apple tv', 'mac', 'iphone', 'Ipad', 'apple watch', 'mac book', 'airpods']
#produtos.append('iphone 11')
#produtos.remove('iphone')
#print(produtos)
produto_remover = input('Digite o produto')

# Existem duas formas de tratar o erro:

# 1. Criar um if para evitar que ele aconteça
# 2. Esperar que ele possa acontecer e tratar caso o erro aconteça com:
try:
    produtos.remove(produto_remover)
except:
    print(f'{produto_remover} não existe na lista de produtos')
print(produtos)




