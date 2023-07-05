# Oeradores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  F e l i p e
# -6-5-4-3-2-1

#nome = 'Felipe'

# print(nome[2])
# print(nome[-4])

#print('ipe' in nome)
#print('zero' in nome)
#print('-' * 10)
#print('ipe' not in nome)
#print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não esta em {nome}')
