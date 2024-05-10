def calcular_salario(horas_trabalhadas, salario_minimo, horas_extra):

    valor_hora_trabalhada = salario_minimo / 8
    valor_hora_extra = salario_minimo / 4

    salario_bruto = horas_trabalhadas * valor_hora_trabalhada
    salario_horas_extra = horas_extra * valor_hora_extra

    salario_total = salario_bruto + salario_horas_extra

    return salario_total

horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
salario_minimo = float(input("Digite o valor do salário mínimo: "))
horas_extra = float(input("Digite o número de horas extras trabalhadas: "))

salario_receber = calcular_salario(horas_trabalhadas, salario_minimo, horas_extra)

print(f"O salário a receber é R${salario_receber:.2f}")
