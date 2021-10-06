aux = str(input("Diga uma frase: ")).strip().upper()
palavras = aux.split()
frase = ''.join(palavras)
tamanho = len(frase)-1
inverso = ''

for c in range(tamanho, -1, -1):
    inverso += frase[c]

print("O inverso de {} é {}".format(frase, inverso))

if frase == inverso:
    print("Forma um palíndromo")
else:
    print("Não forma um palíndromo")