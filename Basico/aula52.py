"""
Tipo tupla -> Uma lista imutável
"""
nomes = 'Maria', 'Helena', 'Luiz'
#nomes[1] = 'outro'
_, _, nome, *_ = nomes
print(nomes)
print(nome)
