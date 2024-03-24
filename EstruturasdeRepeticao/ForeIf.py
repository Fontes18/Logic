# for + if

#Estrutura:
"""
for item in lista:
    if condicao:
        faça alguma coisa
    else
        outra coisa
"""

"""
Digamos que a gente esteja analisando a meta de vendas de vários
funcionários de uma empresa. A meta de vendas é de 1000 reais em 1 dia.
temos uma lista com as vendas de todos os funcionários e quero calcular 
qual % de pessoas que bateram a meta.
"""
vendas = [1200, 300, 800, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 800, 870, 50, 1111, 120, 300, 450, 600]
meta = 1000
i = 0
for venda in vendas:
    if venda >= meta:
        i = i + 1
funcionarios = len(vendas)

print(f'O percentual de pessoas que bateram a meta foi de {i/funcionarios:.0%}')