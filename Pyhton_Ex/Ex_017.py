#ler o comprimento do cateto oposto e adjacente e mostrar comprimento da hipotenusa

from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hi = hypot(co, ca)
print('A hipotenusa vai medir {}'.format(hi))