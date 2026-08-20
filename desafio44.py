print('\033[35m-'*60, 'Bem Vindo', '-'*60,'\nA função de programa é pegar um valor e altera-lo em relação a forma de pagamento\033[m')
while True:
    try:
        valor = int(input('Digite o preço: '))
        cheque = input('Você deseja pagar a vista em dinheiro/cheque?: ').strip().lower()
        if cheque in ['s', 'sim']:
            print(f'Você teve um desconto de 10%, ficando {valor*0.9}')
            break
        elif cheque in ['não','nao','n']:
            cartao = input('Você deseja pagar a vista no cartão?: ')
            if cartao in ['s', 'sim']:
                print(f'Você teve um desconto de 5%, ficando {valor*0.95}')
                break
            elif cartao in ['n', 'nao','n']:
                cartao2 = input('Você deseja pagar no cartão dividindo em 2 vezes?: ')
                if cartao2 in ['s', 'sim']:
                    print(f'Você não teve desconto, ficando {valor}')
                    break
                elif cartao2 in ['n', 'nao','n']:
                    print(f'Você ficou com pagar no cartão dividindo em 3 vezes por falta de mais formas de pagamento, o valor ficou {valor*1.2}')
                    break
                else:
                    print('Errado')
                    continue
            else:
                print('Errado')
                continue
        else:
            print('Errado')
            continue
    except ValueError:
        print('Valor invalido')