# 1 parte receber o valor do salário
sal = float(input('Diga o valor do seu salário:R$ '))

if sal < 280:
    por = 20
    aumento = sal + (sal * por / 100)
    valoraumento = aumento - sal
    print(f'O seu salário antes do ajuste R${sal:.2f}\n'
          f'O percentual de aumento foi de {por}%\n'
          f'O valor do aumento foi de {valoraumento:.2f}\n'
          f'Seu novo salário é de {aumento:.2f}')
elif sal < 700:
        por = 15
        aumento = sal + (sal * por / 100)
        valoraumento = aumento - sal
        print(f'O seu salário antes do ajuste R${sal:.2f}\n'
              f'O percentual de aumento foi de {por}%\n'
              f'O valor do aumento foi de {valoraumento:.2f}\n'
              f'Seu novo salário é de {aumento:.2f}')
elif sal < 1500:
        por = 10
        aumento = sal + (sal * por / 100)
        valoraumento = aumento - sal
        print(f'O seu salário antes do ajuste R${sal:.2f}\n'
              f'O percentual de aumento foi de {por}%\n'
              f'O valor do aumento foi de {valoraumento:.2f}\n'
              f'Seu novo salário é de {aumento:.2f}')
else:
    por = 5
    aumento = sal + (sal * por / 100)
    valoraumento = aumento - sal
    print(f'O seu salário antes do ajuste R${sal:.2f}\n'
          f'O percentual de aumento foi de {por}%\n'
          f'O valor do aumento foi de {valoraumento:.2f}\n'
          f'Seu novo salário é de {aumento:.2f}')