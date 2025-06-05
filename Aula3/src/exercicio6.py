# exercicio 06:
# crie uma funcao para verificar palindromo e retorne verdadeiro ou falso

def palindromo(texto):
    return texto == texto[::-1]

palavra = input("Digite uma palavra ou frase: ")

if palindromo(palavra):
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")
