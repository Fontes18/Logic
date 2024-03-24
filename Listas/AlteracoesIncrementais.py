#Alterações "incrementais" de variáveis

#Estrutura:
"""variável = variavel + outro_valor
ou então
variavel += outro_valor"""

#exemplo: vamos adicionar às variáveis criadas o produto ipad, 500 vendas
lista = ['mac', 'iphone']
vendas = [100, 200]
#Adicionando ipad na lista
lista = lista + ['ipad']

soma_vendas = 300
#adicionando na soma a quantidade de ipad
soma_vendas = soma_vendas + 500

email = 'esse mês vendemos um total de {} produtos, sendo: {} unidades de {}, e {} unidades de {}'.format(soma_vendas,vendas[0],lista[0],vendas[1],lista[1])
email = email + ' também {} unidades de ipad'.format(500)
print(email)

