"""
Iterável -> str, range, etc (__iter__)
Iterador -> Quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
texto = iter('Felipe')  # __iter__()
# print(texto)
iteratador = iter(texto)

while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break
'''numeros = range(0,100,8)

for numero in numeros:
    print(numero)
'''
