# exercicio 04: 
# imprima uma tabuada escolhida pelo usuario
# utilize time funcao e for

import time

def tabuada(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
        time.sleep(0.5)

numero= int(input("Digite o número que deseja ver a sua tabuada completa: "))

tabuada(numero)