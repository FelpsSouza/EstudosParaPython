"""
Cuidados com dados mutáveis
= -> copiando o valor (imutáveis)
= -> aponta para o mesmo valor na memória (mutável)
"""
#nome = 'Felipe'
#noutra_variavel = nome
#nome = 'Souza'

# print(nome)
# print(noutra_variavel)

lista_a = ['Felipe', 'Milena', True, 1, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
