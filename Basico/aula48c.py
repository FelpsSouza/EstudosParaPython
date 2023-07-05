"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append -> Adiciona um item ao final
    insert -> Adiciona um item ao índice escolhido
    pop -> Remove do final ou do índice escolhido
    del -> Apaga um índice
    clear -> limpa a lista
    extend -> estende a lista
    + -> concatena listas
Create Read Update   Delete
Cria,  Ler, Alterar, Apagar = lista[i] (CRUD)
"""
#         0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Felipe')
nome = lista.pop()
print(lista, nome)
lista.append(1233)
del lista[-1]
# lista.clear()
lista.insert(100, 5)
print(lista[4])
