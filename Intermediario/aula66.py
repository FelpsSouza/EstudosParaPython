"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nomo com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def soma(x, y, z):
    # Definição
    print(f'{x=} + y={y} {z=}', '|', 'x + y + z = ', x + y + z)


soma(1, 2, 3)
soma(1, y=2, z=5)

#soma(y=2, x=1, z=3)

print(1, 2, 3, sep='-')
