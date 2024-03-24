"""Contrua um progama que calcule: Qaual dever ser o bônus de um funcionário?
Se ele vendeu mais de 1000 unidades, o bônus tem que ser R$250,
caso contrário, o bônus tem que ser R$50. Se a empresa não bateu a meta de 
10000 vendas, o bônus dele tem que ser 0."""
Meta_emp = 10000
Meta_func = 1000
vendido_emp = int(input('digite aqui quanto a empresa vendeu: '))
vendido_func = int(input('digite aqui quanto o funcionário vendeu: '))

if not vendido_emp > Meta_emp:
    print('Infelizmente a empresa não bateu a meta, não teremos bônus')
elif vendido_emp > Meta_emp and vendido_func < Meta_func:
    print('Infelizmente o funcionário não bateu a meta, mas ganha R$50')
elif vendido_emp > Meta_emp and vendido_func > Meta_func:
    print('Parabéns seu bônus é de R$250')