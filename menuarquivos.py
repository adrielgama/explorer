# -*- coding:utf-8 -*-

import os
import os.path
from pathlib import Path

caminhoPAI = '/Users/proce/Desktop/Explorer'


def title(tl):
    print('=' * 80)
    print(f'{tl:^80}'.upper())
    print('=' * 80)
    print()


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


# ------------------------------- #
# Busca o diretório para arquivos #
# ------------------------------- #
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
        exit(1)
    elif op == 1:
        print('_' * 80)
        print('Por padrão os arquivos possuem extensão .txt')
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


print(menu_arquivos())
