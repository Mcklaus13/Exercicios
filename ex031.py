vel = int(input('Passou pelo radar em que velocidade? '))
mul = (vel - 80) * 7
if vel <= 80:
    print('Está dentro do limite permitido!')
else:
    print(f'Você foi multado! A velocidade permitida é de 80 km/h.\n'
          f'Você passou a {vel}km/h. A multa custa R$7.00 reais por cada km/h a mais permitido!\n'
          f'O valor da multa é de R${mul:.2f} Reais')
print('Tenha um bom dia! Dirija com segurança!')