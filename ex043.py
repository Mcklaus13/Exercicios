from datetime import date
date = date.today().year
ano = int(input('Qual o ano do nascimento do atleta? '))
categoria = date - ano

if categoria <= 9:
    print(f'Esse atleta tem {categoria} anos.É da categoria até \033[1;33m9 anos\033[m:\033[1;34mMIRIM\033[m')
elif categoria <= 14:
    print(f'Esse atleta tem {categoria} anos.É da categoria até \033[1;33m14 anos\033[m:\033[1;34mINFANTIL\033[m')
elif categoria <= 19:
    print(f'Esse atleta tem {categoria} anos.É da categoria até \033[1;33m19 anos\033[m:\033[1;34mJUNIOR\033[m')
elif categoria <= 25:
    print(f'Esse atleta tem {categoria} anos.É da categoria até \033[1;33m25 anos\033[m:\033[1;34mSÊNIOR\033[m')
else:
    print(f'Esse atleta tem {categoria} anos.É da categoria acima de \033[1;33m25 anos\033[m:\033[1;34mMASTER\033[m')