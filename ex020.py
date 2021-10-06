'''import math
angulo = int(input('Informe um ângulo: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print(f'O seno de {angulo}° é de {sen:.2f}\n'
      f'O cosseno de {angulo}° é de {cos:.2f}\n'
      f'O tangente de {angulo}° é de {tan:.2f}')'''

from math import radians,sin,cos,tan
angulo = float(input('Informe um ângulo: '))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print(f'O ângulo de {angulo}° tem o seno de {sen:.2f}\n'
      f'O ângulo de {angulo}° tem o cosseno de {cos:.2f}\n'
      f'O ângulo de {angulo}° tem a tangente de  {tan:.2f}')