"""
Exercício 1: triângulos
"""

def determina_tipo_triangulo(l1, l2, l3):
    if l1 == l2 == l3:
        return "Equilatero"
    if l2 == l3:
        return "Isósceles"
    if l1 != l2 != l3:
        return "Escaleno"
    return "Não é um triângulo"

"""
Exercício 2: dia da semana
"""

def dia_semana(x):
    if x == 1:
        return "Domingo"
    if x == 2:
        return "Segunda-Feira"
    if x == 3:
        return "Terca-Feira"
    if x == 4:
        return "Quarta-Feira"
    if x == 5:
        return "Quinta-Feira"
    if x == 6:
        return "Sexta-Feira"
    if x == 7:
        return "Sábado"
    return "Dado inválido"

"""
Exercício 3: calculadora simples
"""

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def cli():
    a = float(input("Primeiro número: "))
    b = float(input("Segundo número: "))
    x = input("Escolha uma operação:")
    if x == "soma":
        resultado = a + b
        print("O resultado é:", resultado)
    if x == "subtracao":
        resultado = a - b
        print("O resultado é:", resultado)
    if x == "multiplicacao":
        resultado = a * b
        print("O resultado é:", resultado)
    if x == "divisao":
        resultado = a / b
        print("O resultado é:", resultado)
    else:
        print("Operação inválida!")

cli()
