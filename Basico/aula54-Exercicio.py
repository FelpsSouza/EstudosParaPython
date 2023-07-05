"""
Faça uma lista de compas com 'listas'.
O usuário deve ter a possibilidade de inserir,
apagar e listar valores da sua da sua lista
Não permita que o programa quebre com erros de
índices inexistentes na lista.
"""
import os

lista = []

while True:
    op = input('Selecione uma opção:'
               '[i]nserir [a]pagar [l]istar\n').lower()
    try:
        if op == 'i':
            os.system('cls')
            item = input('Valor: ')
            lista.append(item)
        elif op == 'a':
            os.system('cls')
            indice = input('Indice que deseja apagar: ')
            lista.pop(int(indice))
        elif op == 'l':
            os.system('cls')
            if lista == []:
                print('Não há nada para listar')
            else:
                for indice, item in enumerate(lista):
                    print(indice, item)
        else:
            print('Insira um valor válido!')
    except ValueError:
        print('Insira um valor válido!')
    except IndexError:
        print('Não foi possivel apagar este indice.')
