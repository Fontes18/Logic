#Listas de listas
#Estrutura

"""
Cada item de uma lista pode ser qualquer tipo de variável. Inclusive
uma lista.

Quando dentro de uma lista temos cada item como sendo uma outra lista, temos
uma "nested list", ou seja, uma lista de listas

Todas as regras de lista e tudo que vimos funciona exatamente igual
"""
vendedores = ['lira', 'joão', 'diego', 'alon']
produtos = ['ipad', 'iphone']
vendas = [
    [100, 200],
    [300, 500],
    [50, 1000],
    [900, 10]
]

"""
Quanto joão vendeu de ipad ?
Quanto diego vendeu de iphone ?
Qual o total de vendas de iphone ?
"""
print(f'A quantidade que joão vendeu de ipads foi de {vendas[1][0]}')
print(f'A quantidade que diego vendeu de iphones foi de {vendas[2][1]}')
print(f'A quantidade de vendas de iphones foi de {vendas[0][1] + vendas[1][1] + vendas[2][1] + vendas[3][1]}')

"""
e se lira na verdade fez apenas 50 vendas de iphone, como eu modifico
na minha lista o valor de vendas dele?
"""
vendas[0][1] = 50
print(vendas)