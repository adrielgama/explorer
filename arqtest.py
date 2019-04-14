# ============================================================================== #
#                                                                                #
# Instituto Federal de Ciencia Educacao e Tecnologia da Bahia - Campus Salvador  #
#                                                                                #
#                    Curso: Análise e Desenvolvimento de Sistemas                #
#                         Disciplina: Estrutura de Dados                         #
#                            Professor: Marcelo Diniz                            #
#                                                                                #
# ============================================================================== #
#                                                                                #
#                                       Alunos:                                  #
#                                     Adriel Gama                                #
#                                      Ítalo Luiz                                #
#                                   Tamires Manhães                              #
#                                                                                #
#                   ==============================================               #
#                   #    Sistema de Gerenciamento de Arquivos    #               #
#                   ==============================================               #
#                                       :)                                       #
# ============================================================================== #

# -*- coding:utf-8 -*-

import os
from time import sleep
import os.path
import shutil
from pathlib import Path

# clear = lambda: os.system('cls')

caminhoPAI = 'C:\\Users\\proce\\Desktop\\Explorer'


def title(tl):
    print('=' * 80)
    print(f'{tl:^80}'.upper())
    print('=' * 80)
    print()


# ------------------------------ #
#  Acessar o diretório arquivos  #
# ------------------------------ #
def acess_dir():
    print(os.listdir(caminhoPAI))


# ------------------------------- #
#  Verifica o diretório arquivos  #
# ------------------------------- #
def ver_dir(diretorio):
    if not os.path.exists(diretorio):
        # Se não existir, cria diretório
        # Diretório é criado na mesma pasta onde está o arquivo .py
        os.mkdir(diretorio)
        print('Diretório criado com sucesso!')
    else:
        print('Diretório já existe!')


# ---------------------------- #
#  Função para criar arquivos  #
# ---------------------------- #
def cria_arq(nome_arquivo, extensao='txt'):
    file = '.'.join([nome_arquivo, extensao])
    if not os.path.exists(file):
        Path(file).touch()
    else:
        print('Já existe um arquivo com este nome!!')


# ----------------------------------- #
# Menu para ler conteudo dos arquivos #
# ----------------------------------- #
def ler_arq(nome_arquivo, extensao='txt'):
    arq = '.'.join([nome_arquivo, extensao])
    abrir = open(arq, 'r+')
    conteudo = abrir.readlines()
    verifica = os.stat(arq)
    if verifica.st_size == 0:
        print('Arquivo vazio!')
    else:
        print('Conteúdo do arquivo: ')
        print(conteudo)
    abrir.close()


# ----------------- #
# Busca o diretório #
# ----------------- #
def busca_diretorio(diretorio):
    caminho = "arquivo/".join([diretorio])
    # arq = '.'.join([nome_arq, extensao])
    j = 'S'
    while j == 'S':
        if not os.path.exists(caminho):
            print('Caminho invalido')
            j = str(input('Deseja tentar um novo caminho? [S/N]')).upper()
        else:
            j = 'N'
    return caminho


# --------------- #
# Editar arquivos #
# --------------- #
def edit_arq(nome_arquivo, extensao='txt'):
    arq = '.'.join([nome_arquivo, extensao])
    edit = open(arq, 'w+')
    diretorio = str(input('Informe o diretorio que deseja acessar o arquivo: '))
    busca_diretorio(diretorio)

    if not os.path.exists(arq):
        print('Arquivo não existe')
        j = str(input('Deseja criar o arquivo com este nome? [S/N]')).upper()
        if j == 'S':
            cria_arq(nome_arquivo)
        else:
            menu_arquivos()
    else:
        print(edit)

    edit.close()


# ---------------------------- #
# Menu para manipular arquivos #
# ---------------------------- #
def menu_arquivos():
    # clear()
    title('Navegando pelo Menu ARQUIVOS')
    print('Escolha sua opção: ')
    op = int(input('''
        [1] - Criar arquivos
        [2] - Ler arquivos
        [3] - Editar arquivos
        [4] - Apagar arquivos
        [0] - Retornar/Sair

        Opção: '''))

    if op == 0:
        menu()
    elif op == 1:
        # cria_arq(str(input('Nome do arquivo: ')))
        print('_' * 80)
        print('Por padrão os arquivos possuem extensão .txt')
        # print('Caso queira .doc ou .csv, especificar na entrada abaixo.')
        print('_' * 80)
        print()
        j = 'S'
        while j == 'S':
            cria_arq(str(input('Nome do arquivo: ')))
            j = str(input('Deseja criar um novo arquivo? [S/N]')).upper()
        menu_arquivos()
    elif op == 2:
        ler_arq(str(input('Nome do arquivo: ')))
        menu_arquivos()
    elif op == 3:
        edit_arq(str(input('Informe arquivo que deseja editar: ')))
        menu_arquivos()

    else:
        print("Este número não está nas alternativas, tente novamente.\n")
        menu_arquivos()


# def acessar_dir():


# -------------------------- #
# Menu para manipular pastas #
# -------------------------- #
def menu_diretorios():
    # clear()
    title('Navegando pelo Menu DIRETÓRIOS')
    print('Escolha sua opção: ')
    op = int(input('''
        [1] - Criar diretórios
        [2] - Apagar diretórios
        [3] - Acessar diretórios
        [0] - Retornar/Sair

        Opção: '''))

    if op == 0:
        menu()

    elif op == 1:  # CRIAR DIRETORIOS
        j = 'S'
        while j == 'S':
            ver_dir(str(input('Nome do diretório: ')))
            j = str(input('Deseja criar um novo diretório? [S/N]')).upper()
        menu_diretorios()

    elif op == 2:  # APAGAR DIRETORIOS
        tem = (str(input('Informe o nome da pasta a ser apagada: ')))
        dir_del = tem
        if not os.path.exists(dir_del):
            j = 'S'
            while j == 'S':
                j = str(input('Pasta inexistente. Deseja tentar outra? [S/N]')).upper()
        else:
            for caminho, pastas, arquivos in os.walk(caminhoPAI):
                for pasta in pastas[:]:
                    if pasta == dir_del:
                        pastas.remove(pasta)
                        shutil.rmtree(os.path.join(caminho, pasta))
                        print('Pasta removida!')
        menu_diretorios()

    elif op == 3:  # ACESSAR DIRETORIOS
        acess_dir()
        menu_diretorios()

    else:
        print("Este número não está nas alternativas, tente novamente.\n")
        menu_diretorios()


# ------------------------------------- #
# Menu para mover arquivos entre pastas #
# ------------------------------------- #
def menu_mover():
    # clear()
    title('Navegando pelo Menu MOVER')
    print('Escolha sua opção: ')
    op = int(input('''
        [1] - Criar diretórios
        [2] - Apagar diretórios
        [3] - Acessar diretórios
        [0] - Retornar/Sair

        Opção: '''))

    if op == 0:
        menu()
    else:
        print("Este número não está nas alternativas, tente novamente.\n")
        menu_mover()


# -------------- #
# Menu principal #
# -------------- #
def menu():
    title('Bem vindo ao Gerenciador de Arquivos')
    print('Escolha sua opção: ')
    op = int(input('''
    [1] - ARQUIVOS (Criar, ler, editar e apagar arquivos textos)
    [2] - DIRETÓRIOS (Criar, apagar e acessar diretórios)
    [3] - MOVER (Mover arquivos)
    [0] - Sair

    Opção: '''))

    if op == 0:

        print('_' * 80)
        print('\nAguarde, estou finalizando o programa...\n')
        for cont in range(3, 0, -1):
            sleep(1)
            print(f'Saindo em {cont}...')
        print('\nGerenciador finalizado com sucesso!')
        exit(1)
    elif op == 1:
        return menu_arquivos()
    elif op == 2:
        return menu_diretorios()
    elif op == 3:
        return menu_mover()
    else:
        print("Este número não está nas alternativas, tente novamente.\n")
        menu()
    return 0


print(menu())
