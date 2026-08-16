while True:
    try:
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite outro numero: '))
        if n1 > n2:
            print('\033[36mO primeiro valor é maior')
        elif n2 > n1:
            print('\033[33mO segundo é maior')
        else:
            print('São iguais')
        break
    except ValueError:
        print('Valor incorreto')