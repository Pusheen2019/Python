preco = float(input('Qual é o preço do produto? '))

novo = preco - (preco * 5 / 100)

print('O produto que custava {}, com desconto custa {}'.format(preco,novo))