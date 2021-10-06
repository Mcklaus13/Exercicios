dia=input('Dia = ')
mes=input('Mês = ')
ano=input('Ano = ')
cores = {'limpa':'\033[m',
         'verde':'\033[32m',
         'vermelho':'\033[31m',
         'amarelo':'\033[33m' }
print('Você nasceu no dia {}{}{} de {}{}{} de {}{}{}''. Correto?'
      .format(cores['verde'],dia,cores['limpa'],cores['vermelho'],mes,
              cores['limpa'],cores['amarelo'],ano,cores['limpa']))
