# exercicio 07:
# crie uma funcao para imprimir a sequencia de fiboacci com ate N termos definido pelo usuario

termos=int(input("Digite quantos termos deseja: "))

def fiboacci():
    lista= []
    a, b = 0, 1
    while len(lista) < termos: 
        lista.append(a)
        a, b = b, a + b

    print(lista)

fiboacci(termos)