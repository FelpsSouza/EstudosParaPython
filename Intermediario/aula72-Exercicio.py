# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos.
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


x_mult = multiplica(10, 2, 3, 4, 5)
print(x_mult)

# Crie uma função fala se o número é par ou impar
# Retorne se o número é par ou impar. [V]


def impar_par(x):
    if x % 2 == 0:
        return f'{x} é par'
    return f'{x} é impar'


#x_str = input('Insira um numero: ')
#x_int = int(x_str)
# print(impar_par(x_int))

print(impar_par(2))
print(impar_par(5))
print(impar_par(6))
print(impar_par(9))
print(impar_par(10))
