"""Construa um programa para:
    - Calcular o salário dos funcionários com reajuste de 10%
    (a partir de de uma lista de salários)
    - Calcular o custo total de salários que o RH vai ter q pagar
    - Calcular a diferença em R$ entre o cenário anterior e o cenário
    atual"""
lista_salarios = [1500,2500,2000,3000]
reajuste = 0.1

def calcular_lista_salarios_reajustados(reajuste, lista_salarios):
    nova_lista_salarios = []
    for salarios in lista_salarios:
        novo_salario = salarios * (1 + reajuste)
        nova_lista_salarios.append(novo_salario)
    print(nova_lista_salarios)
    return nova_lista_salarios

x = calcular_lista_salarios_reajustados(reajuste, lista_salarios)

def calcular_novo_custo_total(x):
    total = sum(x)
    print(total)

#calcular_novo_custo_total(x)



        

