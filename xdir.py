# -*- coding:utf-8 -*-

import os
import os.path
import shutil
import glob

caminhoPAI = '/Users/proce/Desktop/explorer2/'
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


def ver_dir(diretorio):
    if not os.path.exists(diretorio):
        os.mkdir(diretorio)  # Se não existir, cria diretório
        print('Diretório criado com sucesso!')
    else:
        print('Diretório já existe!')


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
    # with os.scandir(caminho) as it:
    #    for entrar in it:
    #        if not entrar.name.startswith('.') and entrar.is_file():
    #            print('\t', entrar.name)


def listar_dir():
    for filename in glob.iglob('', recursive=True):
        print('_' * 80)
        print('Pasta acessada: ', end='')
        print(filename)


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
        exit(1)
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


print(menu_diretorios())
