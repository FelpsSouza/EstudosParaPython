"""
split e join com list e str
split -> divide uma string
join -> une uma string
"""

frase = '    Olha só que  ,     coisa interessante      '
lista_palavras_crua = frase.split(',')

lista_palavras = []
for i, frase in enumerate(lista_palavras_crua):
    lista_palavras.append(lista_palavras_crua[i].strip())

# print(lista_palavras_crua)
# print(lista_palavras)

frases_unidas = ', '.join(lista_palavras)
print(frases_unidas)
