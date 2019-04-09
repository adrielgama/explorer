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
# import shutil
# from pathlib import Path

clear = lambda: os.system('cls')


def title(tl):
    print('=' * 80)
    print(f'{tl:^80}'.upper())
    print('=' * 80)
    print()


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
    else:
        print("Este número não está nas alternativas, tente novamente.\n")
        menu_arquivos()


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
