"""Calculadora com while"""
while True:

    op = input(
        f'Qual operação deseja realizar?\n[+]soma\n[-]subtração\n[*]multiplicação\n[/]divisão\n')
    numeros_validos = None
    v1 = input('Digite o primeiro valor: ')
    v2 = input('Digite o segundo valor: ')

    try:
        v1_float = float(v1)
        v2_float = float(v2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if op not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(op) > 1:
        print('Digite apenas um operador.')
        continue

    if op == '+':
        res = v1_float + v2_float
        print(f'Resultado: {res}')

    if op == '-':
        res = v1_float - v2_float
        print(f'Resultado: {res}')

    if op == '*':
        res = v1_float * v2_float
        print(f'Resultado: {res}')

    if op == '/':
        res = v1_float / v2_float
        print(f'Resultado: {res}')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is False:
        continue

    if sair is True:
        break

print('Fim')
