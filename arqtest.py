# -*- coding:utf-8 -*-
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

import os
from time import sleep
import os.path
import shutil
from pathlib import Path
import glob

# clear = lambda: os.system('cls')

# ATENÇÃO, MUDAR A PASTA ****PAI**** DO ARQUIVO AQUI
caminhoPAI = '/Users/proce/Desktop/explorer2/'  # ###
# ATENÇÃO, MUDAR A PASTA ****PAI**** DO ARQUIVO AQUI
caminhoAT = os.getcwd()


def title(tl):
    print('=' * 80)
    print(f'{tl:^80}'.upper())
    print('=' * 80)
    print()


def subtitle(tl):
    print('_' * 48)
    print(f'{tl:^48}'.upper())
    print('_' * 48)


# ------------------------------ #
#  Acessar o diretório arquivos  #
# ------------------------------ #
def acess_dir():
    subtitle(' Para acessar subpastas utilize: /nome_da_pasta \n       Para retornar pastas utilize: "."')
    print()
    acesso = os.getcwd()
    with os.scandir(acesso) as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_dir():
                print('\t', entry.name)
    os.chdir(acesso)
    if os.getcwd() == caminhoPAI:
        print(caminhoPAI)
    else:
        print(caminhoAT)
    tem = (str(input('\nInforme o nome da pasta a ser acessada: ')))
    new_acesso = tem
    if not os.path.exists(new_acesso):
        aux = 'S'
        while aux == 'S':
            aux = str(input('Pasta inexistente. Deseja tentar outra? [S/N]')).upper()
    else:
        caminho_atual = caminhoPAI + tem
        print(caminhoAT)
        print('Subpastas: ')
        with os.scandir(caminho_atual) as it:
            for entry in it:
                if not entry.name.startswith('.') and entry.is_dir():
                    print('\t', entry.name)
        print(os.chdir(caminho_atual))
        print('.' * 50)
        print(os.getcwd())
        print('.' * 50)


# ------------------------------- #
#  Verifica o diretório arquivos  #
# ------------------------------- #
def ver_dir(diretorio):
    if not os.path.exists(diretorio):
        os.mkdir(diretorio)  # Se não existir, cria diretório
        print('Diretório criado com sucesso!')
    else:
        print('Diretório já existe!')


# ----------------- #
#  LISTAR ARQUIVOS  #
# ----------------- #
def listar_arquivos():
    for filename in glob.iglob('', recursive=True):
        print('_' * 80)
        print('Pasta acessada: ', end='')
        print(filename)
    listname = glob.glob('*.txt')
    if not listname:
        with os.scandir() as it:
            for entry in it:
                if not entry.name.startswith('.') and entry.is_dir():
                    print('\t', entry.name)
        print('Nenhum arquivo de texto encontrado nesta pasta')
    else:
        print(listname)


# ------------------- #
#  LISTAR DIRETÓRIOS  #
# ------------------ #
def listar_dir():
    for filename in glob.iglob('', recursive=True):
        print('_' * 80)
        print('Pasta acessada: ', end='')
        print(filename)


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
    abrir = open(arq, 'r')
    verifica = os.stat(arq)
    if verifica.st_size == 0:
        print('Arquivo vazio!')
    else:
        subtitle('Conteúdo do arquivo: ')
        for linha in abrir:
            linha = linha.rstrip()
            print(linha)
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
    edit = open(arq, 'a')
    # conteudo = edit.read()

    if not os.path.exists(arq):
        print('Arquivo não existe')
        j = str(input('Deseja criar o arquivo com este nome? [S/N]')).upper()
        if j == 'S':
            cria_arq(nome_arquivo)
        else:
            menu_arquivos()
    else:
        texto = str(input('Informe o conteúdo a ser adicionado no documento: '))
        edit = open(arq, 'a')
        edit.writelines('\n' + texto)
    edit.close()
    print('Arquivo fechado.')


# --------------- #
# Editar arquivos #
# --------------- #
def apagar_arq(nome_arquivo, extensao='txt'):
    arq = '.'.join([nome_arquivo, extensao])
    path = os.getcwd()
    diretorio = os.listdir(path)
    escolha = arq
    if not os.path.exists(escolha):
        print('Não tem como excluir um arquivo inexistente.')
    else:
        for arq in diretorio:
            if arq == escolha:
                os.remove(arq)
        print('Arquivo deletado com sucesso!!')


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
        listar_arquivos()
        ler_arq(str(input('Nome do arquivo: ')))
        menu_arquivos()
    elif op == 3:
        listar_arquivos()
        arquivo = str(input('Informe arquivo que deseja editar: '))
        edit_arq(arquivo)
        menu_arquivos()
    elif op == 4:
        listar_arquivos()
        escolha = str(input('Informe o arquivo que deseja apagar: '))
        apagar_arq(escolha)
        menu_arquivos()
    else:
        print("Este número não está nas alternativas, tente novamente.\n")
        menu_arquivos()


# -------------------------- #
# Menu para manipular pastas #
# -------------------------- #
def menu_diretorios():
    title('Navegando pelo Menu DIRETÓRIOS')
    print('Escolha sua opção: ')
    op = str(input('''
        [mkdir] - Criar diretórios
        [rm] - Apagar diretórios
        [cd] - Acessar diretórios
        [ls] - Listar Arquivos
        [exit] - Retornar/Sair
        Opção: ''')).lower()

    if op == 'exit':
        menu()
# ------------------------------------------------------------------------------------------- #
    elif op == 'mkdir':  # CRIAR DIRETORIOS
        j = 'S'
        while j == 'S':
            print('Para criar subpastas utilize "/" ')
            ver_dir(str(input('Nome do diretório: ')))
            j = str(input('Deseja criar um novo diretório? [S/N]')).upper()
        menu_diretorios()
# ------------------------------------------------------------------------------------------- #
    elif op == 'rm':  # APAGAR DIRETORIOS
        listar_dir()
        tem = (str(input('Informe o nome da pasta a ser apagada: ')))
        dir_del = tem
        if not os.path.exists(dir_del):
            j = 'S'
            while j == 'S':
                j = str(input('Pasta inexistente. Deseja tentar outra? [S/N]')).upper()
        else:
            for caminho, pastas, arquivos in os.walk(os.getcwd()):
                # for caminho, pastas, arquivos in os.walk(caminhoPAI):
                for pasta in pastas[:]:
                    if pasta == dir_del:
                        pastas.remove(pasta)
                        shutil.rmtree(os.path.join(caminho, pasta))
                        print('Pasta removida!')
        menu_diretorios()
# ------------------------------------------------------------------------------------------- #
    elif op == 'cd':  # ACESSAR DIRETORIOS
        listar_dir()
        acess_dir()
        menu_diretorios()
# ------------------------------------------------------------------------------------------- #
    elif op == 'ls':  # LISTAR ARQUIVOS
        print(os.getcwd())
        listar_dir()
        listar_arquivos()
        menu_diretorios()

# ------------------------------------------------------------------------------------------- #
    else:
        print("Esta opção não está nas alternativas, tente novamente.\n")
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
            sleep(0.5)
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
