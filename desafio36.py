#primeiro desafio para aquecer
casa = input('Fale o valor da casa: ')
salario = input('Qual é o seu salário: ')
while True:
    try:
        perdicional = input(
            'Deseja falar apenas o ano ou falar o ano e os meses?\n\033[32mApenas\033[m o ano digite: 1\nO ano e o mês digite: 2\n').strip().lower()
        if perdicional == '1':
            anos = input('Quantos anos deseja pagar: ')
            if float(casa) / (float(anos) * 12) <= float(salario) * 1.3:
                print('Sua prestão mensal é de: {:.2f}'.format(float(casa) / (float(anos) * 12)))
            else:
                print('\033[31mO banco negou, pois é inviável fazer isso com a suas condições\033[m')
        elif perdicional == '2':
            anos = input('Quantos anos deseja pagar?: ')
            meses = input('Quantos meses deseja pagar?: ')
            ano = float(anos) * 12 + float(meses)
            if float(casa)/(float(ano) * 12) <= float(salario) * 1.3:
                print('Sua prestação mensal é de: {:.2f}'.format(float(casa)/float(ano)))
            else:
                print('\033[31mO banco negou, pois é inviável fazer isso com a suas condições\033[m')
        else:
            print('Algo digitado errado')
            continue
        break
    except ValueError:
        print('\033[31mValor incorreto\033[m')
# 1 anos == 12 meses, a prestação não pode passa 30% * salario == error.
print('Aperte ENTER para finalizar')