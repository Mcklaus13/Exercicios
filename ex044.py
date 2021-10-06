a = float(input('Primeiro valor: '))
b = float(input('Segundo valor: '))
c = float(input('Terceiro valor: '))

if a < b + c and b < a + c and c < a + b:
     print('Os segmentos acima PODEM formar um triângulo' ,end=' ')
     if a == b == c:
          print('EQUILÁTERO')
     elif a != b != c != a :
          print('ESCALENO')
     else:
          print('ISÓCELES')
else:
     print('Os segmentos acima NÃO PODEM formar um triângulo')
