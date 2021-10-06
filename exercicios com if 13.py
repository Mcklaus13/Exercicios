l1 = float(input('Digite o primeiro segmento: '))
l2 = float(input('Digite o segundo segmento: '))
l3 = float(input('Digite o terceiro segmento: '))

if l1<l2+l3 and l2<l3+l1 and l3<l2+l1:
    print('É um triangulo',end=' ')
    if l1==l2==l3:
        print('Equilátero: três lados iguais.')
    elif l1==l2!=l3 or l2==l3!=l1 or l3==l1!=l2:
        print('Isóceles: Quaisquer dois lados iguais')
    else:
        print('Escaleno : três lados diferentes')
else:
    print('Estes segmentos não podem formar um triângulo')