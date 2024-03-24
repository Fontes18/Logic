#Enumerate
#Estrutura:

"""O enumerate permite que você percorra uma lista e ao mesmo tempo
tenha em uma variável o índice daquele item.
"""
#for normalmente

"""
for item in lista:
    resto do código
"""
funcionarios = ['maria', 'josé', 'Antônio', 'joão', 'francisco', 'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel', 'Pedro', 'Francisco']
"""for funcionario in funcionarios:
    print(funcionario)"""

"""
for i, item in enumerate(lista):
    resto do código
"""
"""for i, funcionario in enumerate(funcionarios):
    print(f'{i} é o funcionário {funcionario}')"""

"""Vamos pegar um exemplo de nível mínimo de estoque. Em uma fábrica você
tem vários produtos e não pode deixar que os produtos fiquem em falta.
Para isso, foi definido uma quantidade mínima de estoque que os produtos
precisam ter"""

#Identifique os produtos que estão abaixo do estoque.
estoque = [1200, 30, 800, 40, 700, 49, 900]
produtos = ['coca', 'dolly', 'água', 'guarana', 'brahma', 'red bull', 'vinho']
minimo = 50

for i, qtde in enumerate(estoque):
    if qtde < minimo:
        print(f'{produtos[i]} está abaixo do nível mínimo, temos apenas {estoque[i]}')
