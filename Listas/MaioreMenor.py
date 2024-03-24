# Algumas funções básicas de lista

# Tamanho da lista

# tamanho = len(lista)

produtos = ['apple tv', 'mac', 'iphone', 'Ipad', 'apple watch', 'mac book', 'airpods']

# Quantos produtos temos a venda?

tamanho = len(produtos)
# print(tamanho)

# Maior e Menor Valor
# maior = max(lista)
# menor = min(lista) 

vendas = [1000, 1500, 270, 900, 100, 1200, 5000]

# Qual o item mais vendido ?
# Qual o item menos vendido ?
maior = max(vendas)
menor = min(vendas)
nome_produto_maior = produtos[vendas.index(maior)]
nome_produto_menor = produtos[vendas.index(menor)]
print(f'O produto que mais vendeu foi {nome_produto_maior} com {maior} unidades vendidas e o que menos vendeu foi {nome_produto_menor} com {menor} unidades ')

