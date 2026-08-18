while True:
    try:
        lado1 = int(input('Qual é o comprimento do primeiro lado: '))
        lado2 = int(input('Qual é o comprimento do segundo lado: '))
        lado3 = int(input('Qual é o comprimento do terceiro lado: '))
        if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2:
            if lado1 == lado2 == lado3:
                print('É um \033[33mTRIANGULO Equilatero!')
            elif lado1 != lado2 != lado3 != lado1:
                print('É um \033[34MTRIANGULO Escaleno!')
            else:
                print('É um \033[35mTRIANGULO Isoceles!')
        else:
            print('Não é um TRIANGULO!')
        break
    except ValueError:
        print('Ocorreu um erro')