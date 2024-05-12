# 1016

distancia = int(input())
tempo = distancia * 2

print(f'{tempo:.0f} minutos')


# 1153

import math

num = int(input())
resultado = math.factorial(num)

print(resultado)


# 1281

n = int(input())
for _ in range(n):
    m = int(input())
    produtos = {}
    for _ in range(m):
        produto, preco = input().split()
        produtos[produto] = float(preco)
    p = int(input())
    total = 0
    for _ in range(p):
        produto, quantidade = input().split()
        total += produtos[produto] * int(quantidade)
    print(f"R$ {total:.2f}")


# 2006

t = int(input())
responses = list(map(int, input().split()))
correct_responses = 0
for response in responses:
    if response == t:
        correct_responses += 1
print(correct_responses)


# 2339

c, p, f = map(int, input().split())
if c * f <= p:
    print("S")
else:
    print("N")


# 2388

n = int(input())
distancia = 0
for _ in range(n):
    t, v = map(int, input().split())
    distancia += t * v
print(distancia)


# 2413

num_pessoas = int(input())
quantidade = num_pessoas * 4
print(quantidade)


# 3048

def num_maximo_marcado(N, V):
    marcado = 1
    marca_anterior = V[0]

    for i in range(1, N):
        if V[i] != marca_anterior:
            marcado += 1
            marca_anterior = V[i]

    return marcado

N = int(input())
V = [int(input()) for _ in range(N)]

print(num_maximo_marcado(N, V))