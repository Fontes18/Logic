"""Construa um programa que calcule: Você tem uma lista de preços 
de produtos, todos od produtos acima de R$5000 vão ser reajustados em 5%
e todos abaixo de R$5000 vão ser reajustados em 10%, como ficam os
preços dos produtos?"""
lista_precos = [100,6000,1000,1500]
reajuste_faixa1 = 0.05
reajuste_faixa2 = 0.1
nova_lista = []

for preco in lista_precos:
    if preco > 5000:
        nova = preco * (1 + reajuste_faixa1)
    elif preco < 5000:
        nova = preco * (1 + reajuste_faixa2)
    nova_lista.append(nova)
print(nova_lista)
