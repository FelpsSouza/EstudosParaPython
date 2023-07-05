"""
Iterando strings com while
"""
#       0123456789...

nome = 'Felipe Souza'  # Iteráveis
#      -123456789...

tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)

# print(nome[4])

nova_string = ''
i = 0

while tamanho_nome > i:
    nova_string += '*' + nome[i]
    i += 1

nova_string += '*'
print(nova_string)

# Resolução professor

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)
