# geral

# armazene 5 frutas nas 4 estruturas (lista/set/tupla/dict)
# definir uma lista vazia
import random

lista = []

# criar uma estrutura de repetição para inserir os 5 elementos

def gerar_dados(qtd, valormin, valormax):
    return [random.randint(valormin, valormax) for  _ in range(qtd)]
lista = gerar_dados(8, 1, 50)

# criar uma variavel para cada estrutura e fazer a devida conversão
    
lista_final = list(lista)
set_final = set(lista)
tupla_final = tuple(lista)
dict_final = {j: lista for j, valor in enumerate(lista)}

# imprimir os 5 resultados 

print(f"Lista {lista_final}")
print(f"Lista {set_final}")
print(f"Lista {tupla_final}")
print(f"Lista {dict_final}")

# após o teste acima, aplique o random para inserir os valores na lista