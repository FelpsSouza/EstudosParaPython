"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-24
"""

hora_str = input('Insira o horário do dia: ')

try:

    hora_int = float(hora_str)
    #bom_dia = 11
    #boa_tarde = 17
    #boa_noite = 24

    if hora_str.isdigit():
        if hora_int <= 11:
            print('Bom dia')
        elif hora_int <= 17:
            print('Boa Tarde')
        elif hora_int <= 24:
            print('Boa Noite')
        else:
            print('Digite um horário válido.')
except:
    print('Digite um horário válido.')
