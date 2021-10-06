valor = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o seu salário mensal?R$ '))
anos = int(input('Em quantos anos, você quer pagar? '))
meses = anos * 12
valor = valor / meses
sal = sal * 30 / 100
if valor <= sal:
    print(f'Crédito aprovado. A parcela vai ficar de R${valor:.2f} durante {meses} meses ')
else:
    print('Crédito negado. O valor excedeu 30% do seu salário .')