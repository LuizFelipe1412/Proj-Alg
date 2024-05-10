def calcular_terceiro_angulo(angulo1, angulo2):
    angulo3 = 180 - (angulo1 + angulo2)
    return angulo3

angulo1 = float(input("Digite a medida do primeiro ângulo do triângulo: "))
angulo2 = float(input("Digite a medida do segundo ângulo do triângulo: "))

terceiro_angulo = calcular_terceiro_angulo(angulo1, angulo2)

print(f"A medida do terceiro ângulo do triângulo é {terceiro_angulo} graus.")