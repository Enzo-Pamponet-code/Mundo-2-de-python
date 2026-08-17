import datetime
import math
#Mais um desafio
print('\033[36m-'*60, 'Coferência Nacional de Notação', '-'*60,'\033[m')
name = input('Fale seu nome: ')
while True:
    try:
        print(
            'Padrão de formatação de data dia/mês/ano, Se for escrever em número no mês se for um mês um caracter a menos adicione um 0 a sua frente')
        data = input(f'{name}, Fale seu data de nascimento: ').strip().lower()
        # ---------------------------------------------------------------------
        a = data.replace('/', ' ')
        b = a.split()
        # -----------------------------------------------------------------------
        dia = int(datetime.datetime.now().strftime('%d'))
        mes = int(datetime.datetime.now().strftime('%m'))
        ano = int(datetime.datetime.now().strftime('%Y'))
        # -------------------------------------------------------------------------
        janeiro = ['janeiro', 'jan']
        fevereiro = ['fevereiro', 'fev']
        marco = ['março', 'mar', 'marco']
        abril = ['abril', 'abr']
        maio = ['maio', 'mai']
        junho = ['junho', 'jun']
        julho = ['julho', 'jul']
        agosto = ['agosto', 'ago']
        setembro = ['setembro', 'set']
        outubro = ['outubro', 'out']
        novembro = ['novembro', 'nov']
        dezembro = ['dezembro', 'dez']
        # --------------------------------------------------------------------------
        # -------------------------------------------------------------------------
        if b[1].isalpha():
            if b[1] in janeiro:
                c = dia - int(b[0])
                d = mes - 1
                e = ano - int(b[2])
            elif b[1] in fevereiro:
                c = dia - int(b[0])
                d = mes - 2
                e = ano - int(b[2])
            elif b[1] in marco:
                c = dia - int(b[0])
                d = mes - 3
                e = ano - int(b[2])
            elif b[1] in abril:
                c = dia - int(b[0])
                d = mes - 4
                e = ano - int(b[2])
            elif b[1] in maio:
                c = dia - int(b[0])
                d = mes - 5
                e = ano - int(b[2])
            elif b[1] in junho:
                c = dia - int(b[0])
                d = mes - 6
                e = ano - int(b[2])
            elif b[1] in julho:
                c = dia - int(b[0])
                d = mes - 7
                e = ano - int(b[2])
            elif b[1] in agosto:
                c = dia - int(b[0])
                d = mes - 8
                e = ano - int(b[2])
            elif b[1] in setembro:
                c = dia - int(b[0])
                d = mes - 9
                e = ano - int(b[2])
            elif b[1] in outubro:
                c = dia - int(b[0])
                d = mes - 10
                e = ano - int(b[2])
            elif b[1] in novembro:
                c = dia - int(b[0])
                d = mes - 11
                e = ano - int(b[2])
            elif b[1] in dezembro:
                c = dia - int(b[0])
                d = mes - 12
                e = ano - int(b[2])
            f = c + d * 30.42 + e * 365 + math.ceil(e / 4)
            if f < 3650:
                print('\033[32mVocê é MIRIM')
            elif f < 5475:
                print('\033[33mVocê é INFANTIL')
            elif f < 7300:
                print('\033[36mVocê é JUNIOR')
            else:
                print('\033[35mVocê é SENIOR')
            break
        #------------------------------------------------------------------------------------------------------------
        else:
            c = dia - int(b[0])
            d = mes - int(b[1])
            e = ano - int(b[2])
            f = c + d * 30.42 + e * 365 + math.ceil(e / 4)
            if f < 3650:
                print('\033[32mVocê é MIRIM')
            elif f < 5475:
                print('\033[33mVocê é INFANTIL')
            elif f < 7300:
                print('\033[36mVocê é JUNIOR')
            else:
                print('\033[35mVocê é SENIOR')
            break
    except ValueError:
        print('\033[31mInvalido\033[m')