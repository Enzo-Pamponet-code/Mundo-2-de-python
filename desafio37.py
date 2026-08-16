while True:
    try:
        numero = int(input('Digite um numero inteiro: '))
        int(numero)
        b = bin(numero)
        o = oct(numero)
        h = hex(numero)
        print(f'\033[36m{numero} em binario: {b[2:]}\n\033[33m{numero} em octal: {o[2:]}\n\033[36m{numero} em hexadecimal: {h[2:]}')
        break
    except ValueError:
        print('Valor invalido')