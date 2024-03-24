"""Construa um programa que calcule: Calcule o contrário agora,
quanto tempo demora para esse funcionário chegar em um salário
de 10.000 reais?"""
salario = 2000
aumento = 0.1
tempo = 0

while salario < 10000:
    salario = salario * (1 + aumento)
    tempo = tempo + 1
print(tempo)
