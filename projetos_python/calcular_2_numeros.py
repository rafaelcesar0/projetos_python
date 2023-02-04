from os import _exit, system
from time import *

def soma():
    while True:
        while True:
            system('cls')
            try:
                
                n1 = int(input('◇ _ + _ =\n\n⇨ '))
                break  
            except:
                print('Digite apenas números...')
                sleep(1)
        while True:
            system('cls')
            try:
                
                n2 = int(input(f'◇ {n1} + _ =\n\n⇨ '))  
                break
            except:
                print('Digite apenas números...')
                sleep(1)
        system('cls')    
        r = n1 + n2
        print(f'◇ {n1} + {n2} = {r}\n')
        system('pause')
        while True:
            system('cls')
            op = input('Deseja continuar? [s/n]\n⇨ ')
            op = op.lower()
            if op == 's':
                break
            elif op == 'n':
                return r

def subtração():
    while True:
        while True:
            system('cls')
            try:
                n1 = int(input('◇ _ - _ =\n\n⇨ '))
                break  
            except:
                print('Digite apenas números...')
                sleep(1)
        while True:
            system('cls')
            try:
                n2 = int(input(f'◇ {n1} + _ =\n\n⇨ '))  
                break
            except:
                print('Digite apenas números...')
                sleep(1)
        system('cls')    
        r = n1 - n2
        print(f'◇ {n1} - {n2} = {r}\n')
        system('pause')
        while True:
            system('cls')
            op = input('Deseja continuar? [s/n]\n⇨ ')
            op = op.lower()
            if op == 's':
                break
            elif op == 'n':
                return r

def divisão():
    while True:
        while True:
            system('cls')
            try:
                n1 = int(input('◇ _ ÷ _ =\n\n⇨ '))
                break  
            except:
                print('Digite apenas números...')
                sleep(1)
        while True:
            system('cls')
            try:
                n2 = int(input(f'◇ {n1} ÷ _ =\n\n⇨ '))   
                break
            except:
                print('Digite apenas números...')
                sleep(1)
        system('cls')    
        r = n1 / n2
        print(f'◇ {n1} ÷ {n2} = {r:.1f}\n')
        system('pause')
        while True:
            system('cls')
            op = input('Deseja continuar? [s/n]\n⇨ ')
            op = op.lower()
            if op == 's':
                break
            elif op == 'n':
                return r

def multiplicação():
    while True:
        while True:
            system('cls')
            try:
                n1 = int(input('◇ _ x _ =\n\n⇨ '))
                break  
            except:
                print('Digite apenas números...')
                sleep(1)
        while True:
            system('cls')
            try:
                n2 = int(input(f'◇ {n1} x _ =\n\n⇨ '))  
                break
            except:
                print('Digite apenas números...')
                sleep(1)
        system('cls')    
        r = n1 * n2
        print(f'◇ {n1} x {n2} = {r}\n')
        system('pause')
        while True:
            system('cls')
            op = input('Deseja continuar? [s/n]\n⇨ ')
            op = op.lower()
            if op == 's':
                break
            elif op == 'n':
                return r

def switch(opção):
    if opção == 1:
        soma()
    elif opção == 2:
        subtração()
    elif opção == 3:
        divisão()
    elif opção == 4:
        multiplicação()
    else:
        print('Opção invalida...')
        sleep(1)

while True:
    system('cls')
    print('''
[1] Somar       2 valores
[2] Subtrair    2 valores
[3] Dividir     2 valores
[4] Multiplicar 2 valores
[0] Sair''')

    try:
        opção = int(input('⇨ '))
        if 0 < opção < 5:
            switch(opção)
        elif opção == 0: 
            _exit(0)
        else:
            print('Opção invalida...')
            sleep(1)  
    except:
        print('Digite apenas números...')
        sleep(1)