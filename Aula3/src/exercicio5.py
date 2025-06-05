# exercicio 5:
# conte quantas vezes o usuario interagiu ate digitar a opçao sair
# utilize funcao, while e crie um menu com 3 opcoes

def mostrar_menu():
    print(f"\n ------ MENU ------ \n")
    print("[1] - Meu Perfil")
    print("[2] - Configurações")
    print("[3] - Sair")

interacoes = 0
opcao = ""

while opcao != "3":
    mostrar_menu()
    opcao = input("\nEscolha uma opção: ")
    interacoes += 1

    if opcao == "3":
        print(f"\nVocê interagiu {interacoes} vezes até sair.\n")
        break