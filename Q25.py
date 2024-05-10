def converter_para_minutos(horas, minutos):
    total_minutos = (horas * 60) + minutos
    total_segundos = total_minutos * 60
    return total_minutos, total_segundos

horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))

total_minutos, total_segundos = converter_para_minutos(horas, minutos)

print(f"A hora digitada convertida em minutos é: {horas} horas e {minutos} minutos = {total_minutos} minutos.")
print(f"O total de minutos é: {total_minutos} minutos.")
print(f"O total de minutos convertidos em segundos é: {total_segundos} segundos.")
