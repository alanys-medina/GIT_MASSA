#Codigo do cardapio questão 31

codigo = int(input("Código do produto: "))
quant = int(input("Quantidade:"))

if codigo == 100:
    preco = 1.20
elif codigo == 101:
    preco = 1.30
elif codigo == 102:
    preco = 1.50
elif codigo == 103:
    preco = 1.20
elif codigo == 104:
    preco = 17.00
elif codigo == 105:
    preco = 9.50
elif codigo == 106:
    preco = 6.00
else:
    print("Código inválido.")
    preco = -1 

if preco != -1:
    total = quant * preco
    print("O total a pagar: R$",total) 
print ("==============================================================================")

#Questao 32
preco = float(input("Preço do produto: "))
if preco <=50:
    aumento = preco * 0.05
elif preco <= 100:
    aumento = preco * 0.10
else:
    aumento = preco * 0.15
novo = preco + aumento
print("Novo preço: ",novo)

print ("==============================================================================")
