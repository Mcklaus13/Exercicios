'''import random
import time
computador = random.randint(0,5) # Faz o computador escolher algo aleatório
print('-=--' * 15)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=--' * 15 )
chute = int(input('Em que número eu pensei? ')) # Jogador tenta advinhar o numero
print('PROCESSANDO....')
time.sleep(2)
if chute == computador:
    print(f'PARABÉNS! Você conseguiu me vencer! {chute}')
else:
    print(f'GANHEI! Eu pensei no numero {computador} e não {chute}!')'''


import random
from time import sleep
print('\033[1;33m-=--\033[m'*15)
print('\033[1;34mVou pensar em um número entre 0 e 5. Tente adivinhar.... \033[m')
print('\033[1;33m-=--\033[m'*15)
num = int(input('Em que número eu pensei? '))
print('\033[1;35mPROCESSANDO...\033[m')
sleep(2)
esc = random.randint(0,5)
if num == esc:
    print(f'\033[31mPARABÉNS, O número escolhido foi o {esc}!\033[m')
else:
    print(f'\033[31mGanhei! Eu pensei no número {esc} e não no {num}!\033[m ')