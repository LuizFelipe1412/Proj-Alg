import math

custo_espetaculo = float(input("Digite o custo total do espetáculo:"))
preco_ingresso = float(input("Digite o preço do ingresso:"))
qtd_ingressos = math.ceil(custo_espetaculo/preco_ingresso)

print(f"É nescessário vender {qtd_ingressos} para cobrir os custos do espetáculo")