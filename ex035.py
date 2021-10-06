'''num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
num3 = int(input('Terceiro valor: '))
if (num1 > num2  and num1 > num3 ):
    print(f'O maior valor digitado foi {num1} ')
if (num2 >  num3 and num2 > num1):
    print(f'O maior valor digitado foi {num2} ')
if (num3 > num2 and num3 > num1):
    print(f'O maior valor digitado foi o {num3}')

if (num1 < num2 and num1 < num3):
    print(f'O menor valor digitado foi {num1}')
if (num2 < num1 and num2 < num3):
    print(f'O menor valor digitado foi {num2}')
if (num3 < num2 and num3 < num1):
    print(f'O menor valor digitado foi {num3}')'''

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')
