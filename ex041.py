from datetime import date
date = date.today().year
ano = int(input('Me diga o ano do seu nascimento: '))
alis = (date - ano)
tempo = 18 - alis
tem = tempo + date
tempo1 = alis - 18
tem1 = date - tempo1
print(f'Quem nasceu em {ano} tem {alis} anos em {date}.')
if alis < 18:
    tempo = 18 - alis
    print(f'Faltam {tempo} anos para o seu alistamento.\n'
          f'Seu alistamento será em {tem}.')
elif alis == 18:
    print('Está na hora de se alistar!')
else:
    print(f'Passou do tempo para o alistamento.\n'
    f'Você deveria ter se alistado há {tempo1} anos.\n'
    f'Seu alistamento foi em {tem1}.')
