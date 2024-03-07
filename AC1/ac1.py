"""
Exercício 1: equações de segundo grau
"""

a = float(input('Informe o parâmetro a da equação: '))
b = float(input('Informe o parâmetro b da equação: '))
c = float(input('Informe o parâmetro c da equação: '))

delta = b ** 2 - (4 * a * c)

raiz_1 = (-b - delta ** 0.5) / (2 * a)
raiz_2 = (-b + delta ** 0.5) / (2 * a)

print('A primeira raiz é ', round(raiz_1, 2))
print('A segunda raiz é ', round(raiz_2, 2))

"""
Exercício 2: anos bissextos
"""

ano = int(input('Informe o ano: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(True)
else:
    print(False)