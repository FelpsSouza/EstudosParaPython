"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
  Exiba:
    Seu nome é {nome}
    Seu nome invertido é {nome invertido}
    Se nome contém (ou não) espaços
    Seu nome tem {n} letras
    A primeira letra do seu nome é {letra}
    A última letra do seu nome é {letra}
Se nada ofr digitado em nome ou idade:
  Exiba:
    "Desculpe, você deixou campos vazios."
"""
nome = input('Digite seu Nome: ')
idade = input('Digite sua Idade: ')
n = len(nome)

if nome != '' and idade != '':
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contem espaços')
    else:
        print('Seu nome NÃO contem espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[len(nome)-1]}')
else:
    print("Desculpe, você deixou campos vazios.")
