# exercicio 01 :
# imprimr os numeros a partir de um input do usuario
# ate um limite definido, tambem pelo usuario
# utilize funcao definindo parametros


def imprimir(comeco, final):
    for numero in range (comeco, final):
        print(numero)

comeco=int(input("Digite o número de começo: "))
final=int(input("Digite o número final: "))

imprimir(comeco, final)