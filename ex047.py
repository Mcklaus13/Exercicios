from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print('''Vamos brincar de jokenpô
[0] PEDRA.
[1] PAPEL.
[2] TESOURA.''')
jogador  = int(input('Escolha uma das opções acima : '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
print('-='*15)
print(f'Computador jogou: {itens[computador]}')
print(f'O Jogador jogou: {itens[jogador]}')
print('-='*15)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1 :
        print('JOGADOR VENCE')
    elif jogador == 2 :
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')

if computador == 1 :
    if jogador ==  0:
        print('COMPUTADOR VENCE')
    elif jogador  == 1 :
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')

if computador == 2 :
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1 :
        print('COMPUTADOR VENCE')
    elif jogador == 2  :
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')




