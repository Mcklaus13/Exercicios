n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
s = (n1 + n2) / 2
if  s >= 9 and s <= 10:
    print(f'Suas notas foram {n1} e {n2}. Sua média foi {s}\n'
          f'O seu aproveitamento está entre 9.0 e 10.0\n'
          f'APROVADO ')
elif  s < 9 and s >= 7.5:
    print(f'Suas notas foram {n1} e {n2}. Sua média foi {s}\n'
          f'O seu aproveitamento está entre 7.5 e 9.0\n'
          f'APROVADO ')
elif  s < 7.5 and s >= 6.0:
    print(f'Suas notas foram {n1} e {n2}. Sua média foi {s}\n'
          f'O seu aproveitamento está entre 6.0 e 7.5\n'
          f'APROVADO ')
elif  s < 6  and s >= 4.0:
    print(f'Suas notas foram {n1} e {n2}. Sua média foi {s}\n'
          f'O seu aproveitamento está entre 4.0 e 6.0\n'
          f'REPROVADO ')
elif  s < 4 and s >= 0:
    print(f'Suas notas foram {n1} e {n2}. Sua média foi {s}\n'
          f'O seu aproveitamento está entre 4.0 e zero\n'
          f'REPROVADO')