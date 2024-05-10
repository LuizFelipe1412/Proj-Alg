def converter_moedas(reais):
    dolar = reais / 1.80
    marco_alemao = reais / 2.00
    libra_esterlina = reais / 1.57
    return dolar, marco_alemao, libra_esterlina

quantidade_reais = float(input("Digite a quantidade de dinheiro em reais: "))

dolar, marco_alemao, libra_esterlina = converter_moedas(quantidade_reais)

print(f"R${quantidade_reais:.2f} em reais equivale a US${dolar:.2f} dólares.")
print(f"R${quantidade_reais:.2f} em reais equivale a DEM{marco_alemao:.2f} marcos alemães.")
print(f"R${quantidade_reais:.2f} em reais equivale a £{libra_esterlina:.2f} libras esterlinas.")
