'''num = int(input('Digite um número inteiro: '))
if (num % 2) == 1 :
    print(f'O número {num} é Impar ')
else:
    print(f'O número {num} é Par')'''

num = int(input('Digite um número inteiro: '))
resultado = num % 2
if resultado == 1:
    print(f'O número {num} é Impar ')
else:
     print(f'O número {num} é Par')