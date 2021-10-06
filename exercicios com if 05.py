n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
elif n3 > n2 and n3 > n1:
    maior = n3
print(f'O maior número entres os três é o {maior}')
menor = n1
if n2 < n3 and n2 > n1:
    menor = n2
elif n3 < n2 and n3 < n2:
    menor = n3
print(f'O menor número entre os três é o {menor}')