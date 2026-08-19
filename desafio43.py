print('\033[33m-'*60,'IMC','-'*60,'\033[m')
while True:
    nome = input('Digite o seu nome: ')
    print('-'*60,f'Bem vindo,{nome}', '-'*60)
    try:
        altura = float(input('Digite a sua altura em metros: '))
        # Eu tinha botado um parêntese a mais.
        massa = float(input('Digite quantos quilos você tem: '))
        imc = massa/ altura**2

        if imc < 0:
            print('Algo errado, não deviria existir IMC negativo')
        elif imc < 18.5:
            print(f'{nome}, você está Abaixo do peso, com um IMC de {imc:.2f}.')
        elif imc < 25:
            print(f'\033[35m{nome}, você está com o Peso ideal, com um IMC de {imc:.2f}\033[m')
        elif imc < 30:
            print(f'{nome}, você tem Sobrepeso, com um IMC de {imc:.2f}.')
        elif imc < 40:
            print(f'{nome},você tem Obesidade, com um IMC de {imc:.2f}')
        else:
            print(f'{nome}, você tem Obesidade Mórbida, com um IMC de {imc:.2f}.')
        #nessas condicionais, eu quis botar uns negócios a mais.

        break
    except ValueError:
        print('Valor digitado incorretamente.')
    # Valeu