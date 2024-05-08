import math

cat1 = int(input('Digite o comprimento do primeiro cateto:'))
cat2 = int(input('Digite o comprimento do segundo cateto:'))

hipotenusa = math.sqrt((cat1**2)+(cat2**2))

print(f'O comprimento da Hipotenusa é {hipotenusa}')