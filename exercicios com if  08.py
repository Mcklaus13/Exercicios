print('[M] MATUTINO\n'
      '[V] VESPERTINO\n'
      '[N] NOTURNO')
turno = input('Em qual turno voce estuda? ')
if turno.lower() == 'm':
    print('Bom Dia!')
elif turno.lower() == 'v':
    print('Boa Tarde!')
elif turno.lower() == 'n':
    print('Boa Noite!')
else:
    print('Valor Inválido')