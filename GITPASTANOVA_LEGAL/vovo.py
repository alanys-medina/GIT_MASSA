n1 = float(input("Digite a N1: "))
n2 = float(input("Digite a N2: "))
n3 = float(input("Digite a N3: "))
n4 = float(input("Digite a N4: "))

media = (n1 + n2 + n3 + n4) / 4

if media >= 6:
    print(f"MEDIA: {media} - >>> APROVADO")
else:
    print(f"MEDIA: {media} - >>> REPROVADO")