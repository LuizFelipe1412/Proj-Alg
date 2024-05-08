salario = float(input('Digite o valor do seu salário:'))
div1 = float(input('Digite o valor da sua primeira divída atrasada:'))
div2 = float(input('Digite o valor da sua segunda divída atrasada:'))

divtotal = (div1 + (div1*0.02))+(div2 + (div2*0.02))

print(f'Após o pagamento das divídas atrasadas, restará R${salario-divtotal} do seu salário')