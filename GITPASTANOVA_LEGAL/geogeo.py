a = float(input("Digite o lado 1: "))
b = float(input("Digite o lado 2: "))
c = float(input("Digite o lado 3: "))

if a + b > c and a + c > b and b + c > a:
    print("Então formará um triângulo.")
    if a == b == c:
        print("Triângulo Equilátero.")
    elif a == b or a == c or b == c:
        print("Triângulo Isosceles.")
    else:
        print("Triângulo Escaleno.")
else: 
    print("Não é triângulo.")

    