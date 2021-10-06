nome = str(input('Qual é seu nome? '))
if nome == 'Victor':  # Condição simples
    print(f'Que nome bonito!')
elif nome == 'Pedro' or nome == 'Joao' or nome == 'Mcklaus':  # Condicional aninhada
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Victor Julia Daniel Karai':
    print(f'Seu nome é lindo .')
else:
    print('Seu nome é bem normal.')  # Condicional composta
print(f'Tenha um bom dia, \033[35m{nome}\033[m!')
