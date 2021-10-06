'''import random
pri = str(input('Primeiro aluno: '))
seg = str(input('Seguno aluno: '))
ter = str(input('Terceiro aluno: '))
qua = str(input('Quarto aluno: '))
lista  = [pri,seg,ter,qua]
print(f'O aluno escolhido foi {random.choice(lista)}')'''




from random import choice
pri = str(input('Primeiro aluno: '))
seg = str(input('Seguno aluno: '))
ter = str(input('Terceiro aluno: '))
qua = str(input('Quarto aluno: '))
lista  = [pri,seg,ter,qua]
print(f'O aluno escolhido foi {choice(lista)}')

