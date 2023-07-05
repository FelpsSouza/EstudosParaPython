"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

lista = ['Maria', 'Helena', 'Luiz', 'Mario', 'Felipe', 'Joao', 'Milena']
i = 0
indices = range(len(lista))  # Solução do professor usando range

for nome in lista:
    print(i, nome)
    i += 1
