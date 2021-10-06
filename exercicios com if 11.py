dia = int(input('Digite um número: '))
#lista = '1 - Domingo','2 - Segunda','3- Terça','4 - Quarta','5 Quinta','6 - Sexta','7 - Sabado'
domingo = 1
segunda = 2
terca = 3 
quarta = 4 
quinta = 5 
sexta = 6 
sabado = 7
if dia == domingo:
    print('1 - Domingo')
elif dia == segunda:
    print('2 - Segunda')
elif dia == terca:
    print('3 - Terça')
elif dia == quarta:
    print('4 - Quarta')
elif dia == quinta:
    print('5 - Quinta')
elif dia == sexta:
    print('6 - Sexta')
elif dia == sabado:
    print('7 - Sábado')
else:
    print('Valor inválido')