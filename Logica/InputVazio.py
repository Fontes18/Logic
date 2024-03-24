"""para identificar se o usuário preencheu corretamente os inputs
if e o nome das variáveis
ex :"""
faturamento = input("Qual foi o faturamento da loja nesse mês?: ")
custo = input("Qual foi o custo da loja nesse mês?")

while faturamento and custo == '':
    if faturamento and custo:
        print("Preencha o faturamento e o lucro corretamente")
    break
    
if faturamento and custo:
    lucro = int(faturamento) - int(custo)
    print(f"O lucro da loja foi de {lucro} reais")