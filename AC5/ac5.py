import random

def main():
    aventureiro_vida = 100
    aventureiro_defesa = random.randint(1, 5)
    aventureiro_ataque = random.randint(10, 20)
    monstro_vida = random.randint(60,80)
    monstro_ataque = random.randint(20, 30)

    print(f"Aventureiro: Vida = {aventureiro_vida} - Ataque = {aventureiro_ataque} - Defesa = {aventureiro_defesa}")
    print(f"Monstro: Vida = {monstro_vida} - Ataque = {monstro_ataque}")

    rodada = 1

    while aventureiro_vida > 0 and monstro_vida > 0:
        print(f"RODADA {rodada}:")

        dano = random.randint(1, aventureiro_ataque)
        monstro_vida -= dano

        dano = random.randint(1, monstro_ataque) - aventureiro_defesa
        if dano > 0:
           aventureiro_vida -= dano

        print(f" Aventureiro: Vida = {aventureiro_vida}, Ataque = {aventureiro_ataque}, Defesa = {aventureiro_defesa}")
        print(f" Monstro: Vida = {monstro_vida}, Ataque = {monstro_ataque}")

        if monstro_vida <= 0:
            print(f"O Monstro morreu!")
        if aventureiro_vida <= 0:
            print(f"Você morreu!")

        rodada += 1

if __name__ == "__main__":
    main()
