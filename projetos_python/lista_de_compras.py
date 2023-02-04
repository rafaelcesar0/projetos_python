# Faça uma lista de compras com listas.
# O usuário deve ter a possobilidade de
# inserir, apagar, e listar valores da sua lista.
# Não permitindo que o programa quebre com erros
# de indices inexistentes na lista.

from os import system
from time import sleep

lista_de_compras = []
system('cls')

while True:
    print(" MENU ".center(36,"#"))
    print('\nSelecione uma opção:\n[I]-Inserir\n[A]-Apagar\n[L]-Listar')
    opcao = input('↪ ').lower()
    

    if opcao.startswith('i'):
    
        system('cls')
        inserir = input('Insira algo a lista de compras: ').title().strip()
        if len(inserir) > 1 and not inserir.isspace():
            lista_de_compras.append(inserir)
        else:
            print('Você não adicionou nada a lista', end='')
            for _ in range(3):
                print('.', end='')
                sleep(0.5)
        system('cls')

    elif opcao.startswith('l'):
        if bool(lista_de_compras) is False:
            print('Lista de compras vazia...')
            system('pause')
            system('cls')
        else:
            system('cls')
            print(" LISTA DE COMPRAS ".center(36,"#"))
            for numero, nome in enumerate(lista_de_compras):
                print(numero+1, nome)

    elif opcao.startswith('a'):
        if bool(lista_de_compras) is False:
            print('Lista de compras vazia...')
            system('pause')
            system('cls')
            continue
        system('cls')
        print('Digite o nome ou o número do item que deseja apagar.')
        apagar = input('Apagar: ').title().strip()
        print('Buscando', end='')
        for _ in range(3):
            print('.', end='')
            sleep(0.5)
        print('\n')
        try:
            if apagar.isnumeric():
                lista_de_compras.pop(int(apagar)-1)
            else:
                del lista_de_compras[lista_de_compras.index(apagar)]
        except:
            print('Item não encontrado.')
        else:
            print('Item apagado com sucesso.')
        system('pause')
        system('cls')

    else:
        print('Opção inválida.')
        system('pause')
        system('cls')
