N1 = int(input("Digite um número:"))
N2 = int(input("Digite outro número:"))

if N2 == 0:
    print("O segundo número não pode ser 0")
    N2 = int(input("Digite outro número:"))

N3 = N1//N2

print(f"{N1}/{N2}={N3}")