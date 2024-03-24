"""Construa um programa que calcule: Tenho uma lista de preços de 
produtos, se fizermos u reajuste de 5% a mais em todos os produtos, como
ficam os preços dos produtos?"""
lista_precos = [100,500,1000,1500]
reajuste = 0.05
lista_reajustada = []

for preco in lista_precos:
    novo_preco = preco * (1 + reajuste)
    lista_reajustada.append(novo_preco)
print(lista_reajustada)
