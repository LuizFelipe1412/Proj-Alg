def calcular_diagonais(numero_lados):
    diagonais = (numero_lados * (numero_lados - 3)) // 2
    return diagonais

numero_lados = int(input("Digite o número de lados do polígono convexo: "))

num_diagonais = calcular_diagonais(numero_lados)

print(f"O número de diagonais do polígono convexo é {num_diagonais}")
