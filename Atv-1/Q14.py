ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade_anos = ano_atual - ano_nascimento

idade_meses = idade_anos * 12

idade_dias = idade_anos * 365

idade_semanas = idade_dias // 7

print(f"A idade da pessoa em anos é: {idade_anos} anos")
print(f"A idade da pessoa em meses é: {idade_meses} meses")
print(f"A idade da pessoa em dias é: {idade_dias} dias")
print(f"A idade da pessoa em semanas é: {idade_semanas} semanas")
