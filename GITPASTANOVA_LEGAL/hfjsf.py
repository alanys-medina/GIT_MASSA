salario  = float(input("Digite o salário atual: R$" ))

if salario < 500:
    reajuste = salario * 00.15
elif salario > 500 and salario <=1000:
    reajuste = salario * 00.10
else: 
    reajuste = salario * 00.05

novo_salario = salario + reajuste

print("----- Resultado Novo salário -----")
print("Salário atual: R$ %.2f" %salario)
print("Reajuste: R$ %.2f" %reajuste)
print("Salário novo: %.2f" %novo_salario)