import random
print('Vamos jogar Jokenpô')
lista = ['pedra', 'papel', 'tesoura']
while True:
    try:
        pergunta = input('Fale qual você vai jogar: ').lower().strip()
        if pergunta in lista:
            a = random.randint(1, 3)
            if pergunta == 'pedra':
                if a == 1:
                    print('Empate')
                elif a == 2:
                    print('Você perdeu')
                else:
                    print('Você ganhou')
            elif pergunta == 'papel':
                if a == 1:
                    print('Você ganhou')
                elif a == 2:
                    print('Empate')
                else:
                    print('Você perdeu')
            else:
                if a == 1:
                    print('Você perdeu')
                elif a == 2:
                    print('Você ganhou')
                else:
                    print('Empate')
            break
        else:
            print('Algo errado')
    except ValueError:
        print('Erro')
