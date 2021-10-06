from time import sleep
num  = int(input('Digite um número inteiro: '))
print('Agora digite qual será a forma de conversão:\n'
      '\033[1;33m-\033[m \033[1;34m1\033[m para \033[1;33mbinário\033[m\n'
      '\033[1;33m-\033[m \033[1;34m2\033[m para \033[1;33moctal\033[m\n'
      '\033[1;33m-\033[m \033[1;34m3\033[m para \033[1;33mhexadecimal\033[m')
opcao = int(input('Sua opção: '))
print('\033[1;31mPROCESSANDO....\033[m')
sleep(2)
binario = bin(num)[2:]
octal = oct(num)[2:]
hexadecimal = hex(num)[2:]
if opcao == 1:
      print('O número {}{}{} em Binário é {}{}{}'.format('\033[1;33m',num,'\033[m','\033[1;33m',binario,'\033[m'))
elif opcao == 2:
      print('O número {}{}{} em Octal é {}{}{}'.format('\033[1;33m',num,'\033[m','\033[1;33m',octal,'\033[m'))
elif opcao == 3:
      print('O número {}{}{} em hexadecimal é {}{}{}'.format('\033[1;33m',num,'\033[m','\033[1;33m',(hexadecimal),'\033m'))
else:
      print('Opção invalida. Tente novamente!')