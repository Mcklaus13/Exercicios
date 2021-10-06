'''tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('----FIM----')
'''

'''nome = str(input('Qual é o seu nome? '))
print(f'Bom dia, {nome}!')
if nome == 'Victor':
    print('Que nome lindo você tem!')
else:
    print(f'Seu nome é tão normal, {nome}!')'''


'''import emoji
nome = str(input('Qual é o seu nome? '))
idade = int(input('Quantos anos você tem? '))
print(f'Bom dia {nome} ')
if idade <= 18:
    print(emoji.emojize('Você ainda é um jovem :pray:',use_aliases=True))
else:
    print(emoji.emojize('Você está começando a ficar velho :older_man:',use_aliases=True))'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua média foi {m :.1f}')
if m >= 6.0:
    print('Você está aprovado!')
else:
    print('Você está reprovado!')


