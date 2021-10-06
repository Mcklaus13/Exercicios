print('[M] Masculino\n'
      '[F] Feminino')
letra = str(input('Qual é o seu sexo: '))
if letra.lower() == 'm':
    print('Você é do sexo Masculino')
elif letra.lower() == 'f':
    print('Você é do sexo Feminino')
else:
    print('Sexo Inválido')

