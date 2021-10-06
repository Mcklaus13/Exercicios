prod = float(input('Informe o valor do produto: R$'))
pag = int(input('\033[1;31m1\033[m - À vista em dinheiro ou cheque tem 10% de desconto.\n'
                '\033[1;31m2\033[m - À vista no cartão tem 5% de desconto.\n'
                '\033[1;31m3\033[m - Em até 2x no cartão preço normal.\n'
                '\033[1;31m4\033[m - 3x ou mais no cartão tem 20% de juros.\n'
                'Selecione uma das opções acima: '))

if pag == 1:
    print(f'O valor à vista em dinheiro ou cheque fica R$\033[1;31m{prod - (prod * 10 /100):.2f}\033[m')
elif pag == 2:
    print(f'O valor à vista no cartão fica R$\033[1;31m{prod - (prod * 5 /100):.2f}\033[m')
elif pag == 3:
    print(f'O valor em até 2x no cartão é o preço normal R$\033[1;31m{prod:.2f}\033[m')
elif pag == 4:
    parc = int(input('Quer dividir em quantas parcelas? '))
    print(f'Sua compra será parcelada  em  {parc}x de R$\033[1;31m{(prod + (prod * 20 /100))/ parc :.2f}\033[m COM JUROS ')
else:
    print('Opção inválida')
