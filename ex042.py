n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
resultado = (n1 + n2) / 2

if resultado < 5.0:
    print(f'\033[1;34mREPROVADO\033[m. A média é 7.0 e você tirou {resultado:.1f}.')
elif  resultado < 6.9:
    print(F'\033[1;34mRECUPERAÇÃO\033[m. A média é 7.0 e você tirou {resultado:.1f}.')
elif resultado >= 7.0:
    print(f'\033[1;34mAPROVADO\033[m.Passou de ano com a média {resultado:.1f}!')