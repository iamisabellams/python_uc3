# desafio
# crie uma funcao para imprimir um quadrado de asteristicos

tamanho = int(input("Digite o tamanho: "))

def parte01(tamanho):
    for i in range(tamanho):
        print('*' * tamanho)


def parte02(tamanho):
    meio = tamanho // 2
    for i in range(tamanho):
        linha=""
        for j in range (tamanho):
            if i == meio and j == meio:
                linha +=" "
            else:
                linha +="*" * tamanho
        print(linha)

def parte03(tamanho):
    altura = tamanho // 2
    for i in range(altura + 1):
        espacos = " " * (altura - i)
        asteristicos = "*" * (2 * i + 1)
        print(espacos + asteristicos + espacos)

parte03(tamanho)

