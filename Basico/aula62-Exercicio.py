"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""
#cpf = '746.824.890-70'
cpf = '74682489070'
numeros = []
cont = 11

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
