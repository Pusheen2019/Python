larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))

area = larg * alt
print('A parede tem a dimensão de {}x{} e a sua área é de {} m²'.format(larg,alt,area))

tinta = area / 2
print('Para pintar a parede será preciso {}l de tinta.'.format(tinta))
