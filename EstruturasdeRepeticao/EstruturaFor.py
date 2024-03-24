#Estrutura de Repetição: for
#Funcionamento:

#for i in range(n):
    #repetir código n vezes

"""for i in range(5):
    print(i)"""

""" Imagine que você está construindo uma automação para enviar todo dia
por e-mail um resumo da produção de uma fábrica. Construa um código
que exija a quantidade produzida de cada um dos produtos nesse e-mail"""

produtos = ['coca', 'pepsi', 'guarana', 'sprite', 'fanta']
producao = [15000, 12000, 13000, 5000, 230]

for i in range(len(produtos)):
    print(f'A quantidade de {produtos[i]} vendida foi {producao[i]}')
    i = i + 1