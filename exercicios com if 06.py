from time import sleep
print('Me informa o valor de 3 produtos')
sleep(1)
prod_1 = int(input('Digite o primeiro:R$ '))
prod_2 = int(input('Digite o segundo:R$ '))
prod_3 = int(input('Digite o terceiro:R$ '))

if prod_1 <= prod_2 and prod_1 <= prod_3:
    print('Compre o primeiro produto.')
elif prod_2 <= prod_3:
    print('Compre o segundo produto.')
else:
    print('Compre o terceiro produto')