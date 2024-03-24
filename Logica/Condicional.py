"""Construa um programa que calcule: Qual deve ser o bônus de um funcionário? Se ele vendeu mais de 1000 unidades, o bônus tem que ser de 250
Caso contário, o bônus tem que ser R$50"""
Total_vendas = int(input("Digite quanto o funcionário vendeu: "))
Meta = 1000

if Total_vendas > Meta:
    bonus = 250
else:
    bonus = 50
print(bonus)