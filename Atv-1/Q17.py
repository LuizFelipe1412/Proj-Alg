import math

raio = int(input('Digite o raio:'))

comp = (2*math.pi)*raio
area = math.pi*raio**2
vol = (3/4*math.pi)*raio**3

print(f'Comprimento é {comp}\nArea é {area}\nVolume é {vol}')