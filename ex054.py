n = int(input("Digite um número para saber se ele é primo ou não: "))
tot = 0
for c in range(1,n +1 ):
    if n % c == 0:
        print('\033[33m', end='')
        tot = tot + 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c),end=' ')
print(f'\n\033[mO numero {n} foi divisível {tot} vezes')
if tot == 2:
    print('É primo')
else:
    print('Não é primo')

