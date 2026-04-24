nome = input("Digite o nome do cliente: ")

p1 = float(input("Digite o valor do primeiro produto: "))
p2 = float(input("Digite o valor do segundo produto: "))
p3 = float(input("Digte o valor do terceiro produto: "))
           
total = p1 + p2 + p3 
media = total / 3
imposto = total * 0.12
total_com_imposto = total + imposto
desconto = total * 0.5
total_com_desconto = total - desconto

print("========== Relátorio ==========")
print("O cliente é",nome)
print("O total da compra é de %.2f" % total)
print("A média dos preços é de %.2f" % media)
print("O valor do imposto é %.2f" % imposto)
print("O total com imposto é de %.2f" % total_com_imposto)
print("O total com imposto é de %.2f" % total_com_desconto)