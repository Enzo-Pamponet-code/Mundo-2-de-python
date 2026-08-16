import datetime
print('\033[32m-'*60,'☠️Exercito☠️','-'*60,'\033[m')
t = str(datetime.datetime.now())
tp = t[:10]
ano = int(tp[:4])
mes = int(tp[5:7])
dia = int(tp[8:10])
name = input('Fale seu nome: ')
print('-'*60,f'Bem Vindo ao Exercito, {name}', '-'*60)
while True:
    try:
        data = input('Digite o dia de nascimento: ')
        if 0 < len(data) < 3:
            pmes = input('Em que mês você naceu?: ')
            if 0 < len(pmes) <= 2:
                panos = input('Em que ano você naceu?: ')
                if 0 < len(panos) <= 4:
                    s = abs(dia - int(data))
                    s1 = abs(mes - int(pmes))
                    s2 = abs(ano - int(panos))
                    d = s1*30
                    d1 = s2*365
                    q = 6570 - (d+d1)
                    print(f'Você tem {s2} anos, {s1} meses e {s} dias')
                    if q > 0:
                        print(f'\033[32mfaltam {q} dias para seu alistamento\033[m')
                    elif q == 0 :
                        print('Você precisa ir para o alistamento')
                    else:
                        print(f'\033[31mVocê precisa ir para o alistamento, se passaram {q} dias\033[m')
            break
        else:
            print('\033[31mDigite de novo\033[m')
    except ValueError:
        print('\033[31mDigite um numero inteiro\033[m')