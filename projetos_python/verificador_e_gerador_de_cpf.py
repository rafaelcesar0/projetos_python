from os import system
from time import sleep
import re, random

def faixa_cpf(cpf:str):
    '''Retorna uma faixa com cpf(Apenas números) inserido'''
    cpf = 'CPF: ' + cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
    cpf_faixa = '-' * (len(cpf) + 4) + '\n' + cpf.center(len(cpf) + 4, ' ') + '\n'+ '-' * (len(cpf) + 4)

    return cpf_faixa

def validar_cpf(cpf:str):
    '''
    Essa função pega um cpf(Apenas números) 
    e verifica os últimos 2 dígitos verificadores 
    if is True mantém o cpf, else corrige os 2 últimos dígitos verificadores
    '''

    cpf_is = False
    a = 0
    b = 0

    for i, n in zip(range(9), range(10,1,-1)):
        a += int(cpf[i]) * n
    
    a = a * 10 % 11
    if a == 10:
        a = 0

    cpf_corrigido = cpf[:9] + str(a)

    for i, n in zip(range(10), range(11,1,-1)):
        b += int(cpf_corrigido[i]) * n

    b = b * 10 % 11
    if b == 10:
        b = 0

    cpf_corrigido = cpf_corrigido + str(b)

    if cpf_corrigido == cpf:
        cpf_is = True

    return cpf_is, cpf_corrigido

def main() -> None:
    while True:
        system('cls')
        cpf = ''
        gerar_cpf_automatico = input('Deseja gerar um CPF automático? [s/n] [e]xit\n↪ ').lower()

        if gerar_cpf_automatico.startswith('s'):
            for i in range(9):
                cpf += str(random.randint(0, 9))
            cpf_gerado = validar_cpf(cpf)[1]
            print(f'⇩ CPF gerado automático ⇩\n{faixa_cpf(cpf_gerado)}')
            system('pause')

        elif gerar_cpf_automatico.startswith('n'):
            cpf_digitado_usuario = input('Digite um CPF para teste de validação.\n↪ ')
            cpf = re.sub(r'[^0-9]', '', cpf_digitado_usuario)

            entrada_e_sequencial = cpf == cpf[0] * len(cpf)

            if not cpf.isnumeric() or len(cpf) != 11:
                print('Por favor digite apenas os 11 números do CPF.')
                system('pause')
                continue
            elif entrada_e_sequencial:
                system('cls')
                print(f'\nAVISO: Você enviou dados sequenciais\n{faixa_cpf(cpf)}\né invalido!')
                sair = input('\nDeseja validar outro CPF? [s/n]\n↪ ').lower().startswith('s')
                if not sair:
                    break
                else:
                    continue

            cpf_is = validar_cpf(cpf)[0]
            cpf_corrigido = validar_cpf(cpf)[1]
            
            
            system('cls')
            print(faixa_cpf(cpf))
            if cpf_is:
                print('É válido!')
            else:
                print('É invalido!')
                corrigir = input('\nDeseja corrigir os últimos 2 dígitos desse CPF? [s/n]\n↪ ').lower().startswith('s')
                if corrigir:
                    print(f'⇩ CPF Verdadeiro ⇩\n{faixa_cpf(cpf_corrigido)}')
            system('pause')

        elif gerar_cpf_automatico.startswith('e'):
            break

        else:
            print('Opção inválida', end='')
            for _ in range(3):
                print('.', end='')
                sleep(0.5)

main()