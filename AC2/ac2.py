"""
Exercício 1: revisitar um AC1
"""

def eq_seg_grau(a, b, c):
    delta = b ** 2 - (4 * a * c)
    return (- b + (delta ** 0.5)) / (2 * a), (- b - (delta ** 0.5)) / (2 * a)

def bissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        return True
    return False


"""
Exercício 2: salário
"""

def calcula_salario(valor_hora, num_hora):
    return (valor_hora * num_hora) * 0.275
