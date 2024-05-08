import math

def calcular_escada(angulo_graus, distancia_parede):
    angulo_radianos = math.radians(angulo_graus)
    
    comprimento_escada = distancia_parede / math.cos(angulo_radianos)
    
    return comprimento_escada

angulo = float(input("Digite o ângulo formado pela escada em graus: "))
distancia = float(input("Digite a distância da escada até a parede em metros: "))

escada = calcular_escada(angulo, distancia)

print(f"A medida da escada para alcançar a ponta é de {escada:.2f} metros.")
