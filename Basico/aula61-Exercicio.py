"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
#      12345678901
#     -10987654321
cpf = '74682489070'
numeros = []
cont = 10

for nmr in cpf:
    if nmr and cont >= 2:
        resultado = cont * int(nmr)
        print(cont, nmr, resultado)
        cont -= 1
        numeros.append(resultado)

cpf_total = sum(numeros) * 10

print(cpf_total)

digito_1 = cpf_total % 11

print(f'Digito: {0 if digito_1 > 9 else digito_1}')
