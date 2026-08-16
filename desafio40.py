#Esse aqui quero passar rápido
while True:
    try:
        nota = int(input('Digite sua primeira nota: '))
        nota1 = int(input('Digite sua segunda nota: '))
        media = (nota+nota1)/2
        if media < 5:
            print(f'\033[31mReprovado\033[m')
        elif media<6.9:
            print(f'\033[33mReprovado\033[m')
        else:
            print(f'\033[31mAprovado\033[m')
    except ValueError:
        print('Valor errado')
'https://www.instagram.com/reel/DcHmpwLzSKC/?utm_source=ig_web_button_share_sheet&igsh=MzRlODBiNWFlZA=='