sal = float(input('Digite o valor do seu salário? R$ '))
au1 = sal + (sal * 10 / 100)
au2 = sal + (sal * 15 / 100)
if (sal >= 1250):
    print(f'Quem ganhava R${sal:.2f} passa a ganhar R${au1:.2f} agora.')
else:
    print(f'Quem ganhava R${sal:.2f} passa a ganhar R${au2:.2f} agora.')

