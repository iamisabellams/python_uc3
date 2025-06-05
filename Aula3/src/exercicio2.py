# exercicio 02:
# imprima uma contagem regressiva com input de partida feito pelo usuario
# utilize while e funcao

import time


def contagem(comeco):
    while comeco >= 0:
        print(comeco)
        time.sleep(1)
        comeco -= 1

numero = int(input("Digite o número para começar a contagem: "))
contagem(numero)