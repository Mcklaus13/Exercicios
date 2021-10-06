cont = 0
tab = int(input('Digite um número para ver sua tabuada: '))
for c in range(1,11):
    cont = cont + 1
    s = tab * cont
    print('{} x {:2} = {}'.format(tab,cont,s))