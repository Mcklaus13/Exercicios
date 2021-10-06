'''dis = int(input('Digite  a distância da sua viagem: '))
print(f'Você está prestes a começar uma viagem de {dis}Km.')
if dis <= 200:
    print(f'E o valor da sua passagem é R${dis * 0.50:.2f} Reais')
else:
    print(f'E o valor da sua passagem é de R${dis * 0.45:.2f} Reais ')'''

dis = int(input('Digite  a distância da sua viagem: '))
dis1 = dis * 0.50
dis2 = dis * 0.45
print(f'Você está prestes a começar uma viagem de {dis}Km.')
if dis <= 200:
    print(f'E o valor da sua passagem é de R${dis1:.2f}')
else:
    print(f'E o valor da sua passagem é de R${dis2:.2f}')