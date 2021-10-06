n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
if n1 > n2:
    print(f'\033[1;33m - \033[mO \033[1;33mPRIMEIRO valor\033[m é \033[1;34mmaior\033[m')
elif n2 > n1:
    print(f'\033[1;33m - \033[mO \033[1;33mSEGUNDO valor\033[m é \033[1;34mmaior\033[m')
else:
    print('\033[1;33m- Não exite\033[m valor maior,os dois são\033[1;34m iguais\033[m ')