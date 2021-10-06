primeiro=int(input("Primeiro elemento: ") )
razao = int(input("Razao: ") )
n = int(input('Em quantas vezes quer ver: '))
dec = primeiro + (n-1)*razao
for c in range(primeiro,dec + razao,razao):
    print(f'{c}',end=' -> ')
print('ACABOU')