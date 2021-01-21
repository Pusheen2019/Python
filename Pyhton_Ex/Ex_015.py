#perguntar a quantidade de km e a quantidade de dias pelos quais o carro foi alugado
#carro custa 50euro por dia e 0.15 por km

dias = int(input('Quantod dias foi alugado: '))
km = float(input('Quantos km feitos? '))

pagar = (dias * 50) + (km * 0.15)
print('O total a pagar é {} euros.'.format(pagar))