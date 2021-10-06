vh = float(input('Valor hora:R$ '))
ht = int(input('Horas trabalhadas: '))
sb = vh * ht
print('Salario bruto:')
if sb <= 900:
    print('Isento')
elif sb <= 1500:
    por = sb - (sb * 5 / 100)
    ir = sb - por
    sid = sb - (sb * 10 /100)
    inss = sb - sid
    fgts = sb - (sb * 11 / 100)
    tf = sb - fgts
    td = inss + ir
    print(f'R$ {sb:.2f}')
    print(f'(-) IR R$ {ir:.2f}')
    print(f'(-) INSS R$ {inss:.2f}')
    print(f'FGTS R$ {tf:.2f}')
    print(f'Total de descontos\n'
          f'R$ {td:.2f}')
    print('Salário Liquido\n'
          f'R$ {sb - td:.2f}')
elif sb <= 2500:
    print(f'R$ {sb:.2f}')
    por = sb - (sb * 10 / 100)
    ir = sb - por
    sid = sb - (sb * 3 /100)
    inss = sb - sid
    fgts = sb - (sb * 11 / 100)
    tf = sb - fgts
    td = inss + ir
    print(f'(-) IR R$ {ir:.2f}')
    print(f'(-) INSS R$ {inss:.2f}')
    print(f'FGTS R$ {tf:.2f}')
    print(f'Total de descontos\n'
          f'R$ {td:.2f}')
    print('Salário Liquido\n'
          f'R$ {sb - td:.2f}')

elif sb > 2500:
    print(f'R$ {sb:.2f}')
    por = sb - (sb * 20 / 100)
    ir = sb - por
    sid = sb - (sb * 3 /100)
    inss = sb - sid
    fgts = sb - (sb * 11 / 100)
    tf = sb - fgts
    td = inss + ir
    print(f'(-) IR R$ {ir:.2f}')
    print(f'(-) INSS R$ {inss:.2f}')
    print(f'FGTS R$ {tf:.2f}')
    print(f'Total de descontos\n'
          f'R$ {td:.2f}')
    print('Salário Liquido\n'
          f'R$ {sb - td:.2f}')

