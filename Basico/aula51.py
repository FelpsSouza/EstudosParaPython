"""
Introdução ao descompactamento + tuples (tuplas)
"""
#nomes = ['Maria', 'Helena', 'Luiz']
#nome1, nome2, nome3 = nomes

#nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
# print(nome2)

#nome1, nome2 = ['Maria', 'Helena', 'Luiz']
# print(nome2)

nome1, *_ = ['Maria', 'Helena', 'Luiz']
print(nome1, _)

_, nome, *_ = ['Maria', 'Helena', 'Luiz']
print(nome)
