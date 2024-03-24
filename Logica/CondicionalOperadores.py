"""Construa um programa que calcule: Qual deve ser o bônus de um funcionário?
Se a empresa bateu a meta de 10000 vendas E se ele vendeu mais de 1000 unidades,
o Bônus tem que ser de R$250,caso contrário, o bônus tem que ser R$50"""
Meta_func = 1000
Meta_emp = 10000
quant_vend_emp = int(input('Digite a quantidade vendida pela empresa: '))
quant_vend_func = int(input('Digite a quantidade vendida pelofuncionário: '))

if quant_vend_emp > Meta_emp and quant_vend_func > Meta_func:
    bonus = 250
else:
    bonus = 50 

str(print('Seu bônus é: ',bonus))