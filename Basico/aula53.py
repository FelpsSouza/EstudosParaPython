"""
enumerate - enumera iteráveis (índices)
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

lista_enumerada = list(enumerate(lista))

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

print('='*10)

for indice, nome in enumerate(lista):
    print(indice, nome)

print('='*10)

for tupla_enumerada in enumerate(lista):
    print('For da tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor}')
