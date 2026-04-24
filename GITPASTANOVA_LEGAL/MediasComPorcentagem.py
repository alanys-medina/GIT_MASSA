nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

media = (nota1 + nota2) / 2

if media == 10:
    print("Média: %.2f" %media)
    print("Aprovado com Distinção.")

elif media >=7:
    print("Média: %.2f" %media)
    print("Aprovado.")

else: 
    print("Média: %.2f" %media)
    print("Reprovado.")
