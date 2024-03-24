"""Construa um programa que calcule: Qual seria o salário de um
funcionário após 10 anos se todo ano ele ganhasse 10% de aumento,
salário inicial de R$2.000"""
salario = 2000
aumento = 0.1
tempo = 10

for i in range(tempo):
    salario = salario * (1 + aumento)
print(int(salario)) 