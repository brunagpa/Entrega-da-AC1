# 1000

print("Hello World!")

# 1001

a = int(input())
b = int(input())
x = a + b
print("X =", x)

# 1010

peca1 = input().split()
peca2 = input().split()

cod_peca1 = int(peca1[0])
cod_peca2 = int(peca2[0])

num_peca1 = int(peca1[1])
num_peca2 = int(peca2[1])

valor_uni_peca1 = float(peca1[2])
valor_uni_peca2 = float(peca2[2])

valor_peca1 = num_peca1 * valor_uni_peca1
valor_peca2 = num_peca2 * valor_uni_peca2

total = valor_peca1 + valor_peca2

print(f"VALOR A PAGAR: R$ {total:.2f}")

# 1013

a, b, c = map(int, input().split())

maiorAB = (a + b + abs(a - b)) / 2
if maiorAB < c:
    maiorAB = c

print('{:.0f}'.format (maiorAB), 'eh o maior')

# 1015

x1, y1 = map(float, input().split())

x2, y2 = map(float, input().split())

distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print("{:.4f}".format(distancia))