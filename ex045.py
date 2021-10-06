from time import sleep
peso = float(input('Digite o seu peso:KG '))
alt = float(input('Digite a sua altura:(m) '))
imc = peso / (alt ** 2)
print('\033[1;35mO IMC IDEAL ESTÁ ENTRE 18.5 E 25 ....\033[M')
sleep(1)
print('\033[1;31mCALCULANDO....\033[m')
sleep(2)
if imc < 18.5:
    print(f'De acordo com seu IMC de {imc:.2f},você está abaixo do peso!')
elif imc < 25:
    print(f'De acordo com seu IMC de {imc:.2f},você está no peso ideal. Parabéns!')
elif imc < 30:
    print(f'De acordo com seu IMC de {imc:.2f},voce está acima do peso ideal! ')
elif imc < 40:
    print(f'De acordo com seu IMC de {imc:.2f},ocê está com obesidade!')
else:
    print(f'De acordo com seu IMC de {imc:.2f},você está com obesidade morbida!')

