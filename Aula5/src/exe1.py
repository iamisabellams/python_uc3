# Funções -  Manipulaçã de arquivos
# OBJETIVO: Criar uma função que cria e adiciona um texto no arquivo


# COMEÇO CRIAR ARQUIVO
def criar_arquivo(nome_arquivo: str, conteudo: str):
     """Cria um arquivo com o nome e conteúdo fornecidos."""
     with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(conteudo)
        print('Criado com Sucesso!')

nome = input('Digite o nome do arquivo: ')
criar_arquivo(f'./Aula5/arquivos/{nome}.txt', '3\n5\n9')
# FINAL CRIAR ARQUIVO


# COMEÇO LER ARQUIVO
def ler_arquivo(nome_arquivo: str):
    """Retorna o conteúdo de um arquivo."""
    with open(nome_arquivo, 'r') as arquivo:
        return arquivo.read()

nome = input('Digite o nome do arquivo: ')
print(ler_arquivo (f'./Aula5/arquivos/{nome}.txt'))
# FINAL LER ARQUIVO


# COMEÇO ADICIONAR ARQUIVO
def add_conteudo(nome_arquivo: str, conteudo: str):
     """Adiciona um novo conteúdo ao arquivo já existente."""
     with open(nome_arquivo, 'a') as arquivo:
        arquivo.write('\n' + conteudo)
        print('Conteúdo adicionado com Sucesso!')

nome = input('Digite o nome do arquivo: ')
conteudo = input('Digite o novo conteúdo: ')
add_conteudo(f'./Aula5/arquivos/{nome}.txt', conteudo)
# FINAL ADICIONAR ARQUIVO


# COMEÇAR REMOVER ARQUIVO
import os

def remover_arquivo(nome_arquivo: str):
    """Exclui o arquivo se existir"""
    if os.path.exists(nome_arquivo):
        os.remove(nome_arquivo)
        print('Arquivo removido com Sucesso!')
    else:
        print('Arquivo não existe/encontrado. DIGITE NOVAMENTE.')

nome = input('Digite o nome do arquivo: ')
remover_arquivo(f'./Aula5/arquivos/{nome}.txt')
# FINAL REMOVER ARQUIVO


# COMEÇO CONTAR LINHAS ARQUIVO
def contar_linhas(nome_arquivo: str) -> int:
    """Retorna a quantidade de linhas de um arquivo."""
    with open(nome_arquivo, 'r') as arquivo:
        return len(arquivo.readlines())

nome = input('Digite o nome do arquivo: ')
print(contar_linhas (f'./Aula5/arquivos/{nome}.txt'))
# FINAL CONTAR LINHAS ARQUIVO


# COMEÇO VERIFICAR SE PALAVRA EXISTE NO CONTEÚDO DO ARQUIVO
def verificar_palavra(nome_arquivo: str, palavra: str) -> bool:
    """Retorna a verificação de uma palavra dentro de um arquivo."""
    with open(nome_arquivo, 'r') as arquivo:
        return palavra in arquivo.read()

nome = input('Digite o nome do arquivo: ')
print(verificar_palavra (f'./Aula5/arquivos/{nome}.txt', 'Flamengo'))
# FINAL VERIFICAR SE PALAVRA EXISTE NO CONTEÚDO DO ARQUIVO


# COMEÇO SOMAR NUMEROS DO ARQUIVO
def somar_numeros(nome_arquivo: str) -> int:
    """Retorna a soma dos números de um arquivo."""
    with open(nome_arquivo, 'r') as arquivo:
        return sum(int(linha.strip()) for linha in arquivo)

nome = input('Digite o nome do arquivo: ')
print(somar_numeros (f'./Aula5/arquivos/{nome}.txt'))
# FINAL SOMAR NUMEROS DO ARQUIVO    


# # COMEÇO ATT LINHA DO ARQUIVO
def att_linha(nome_arquivo: str, novo_conteudo: str, linha_alvo):
    """Atualiza a linha de um arquivo."""
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        if 0 < linha_alvo < len(linhas):
            linhas [linha_alvo] = novo_conteudo + '\n'

    with open(nome_arquivo, 'w') as arq:
        arq.writelines(linhas)

nome = input('Digite o nome do arquivo: ')
conteudo = input('Digite o conteudo do arquivo: ')
linha = input('Digite a linha do arquivo: ')
print(att_linha (f'./Aula5/arquivos/{nome}.txt', 'conteudo', 'linha'))
# # FINAL ATT LINHA DO ARQUIVO    