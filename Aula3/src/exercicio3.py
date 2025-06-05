# exercicio 03:
# some os valores do intervalo definido pelo usuario
# utilize funcao e range

def somar_intervalo(comeco, fim):
    soma = 0
    for numero in range(comeco, fim + 1):
        soma += numero
    return soma

comeco=int(input("Digite o número de começo: "))
fim=int(input("Digite o número do fim: "))

resultado= somar_intervalo(comeco, fim)
print(f"O resultado dos intervalos entre {comeco} e {fim} é: {resultado}")