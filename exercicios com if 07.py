'''a = int(input('Digite o primeiro '))
b = int(input('Digite o segundo: '))
c = int(input('Digite o terceiro: '))

if a < c:
    a, c = c, a

if a < b:
    a, b = b, a

if b < c:
    b, c = c, b

print(f'A ordem decrescente é {a}, {b} e {c}')'''

lista = []
for i in range(3):
    elemento = int(input('Digite um numero: '))
    lista.append(elemento)

lista.sort(reverse = True) #ordena os elementos
print(lista)