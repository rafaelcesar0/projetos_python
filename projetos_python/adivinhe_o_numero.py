import os, random, time

numero_maximo = 10  # Até onde a máquina pode escolher um número.
maximo_de_tentativas = 4
placar_pc = 0
placar_voce = 0

while True:
    n = int(random.randint(1,numero_maximo))
    t = 0
    while t < maximo_de_tentativas :
        os.system('cls')
        print(f'Pc: Melhor de 3!\nPensei num número entre 1 e {numero_maximo}. Tente adivinhar.\nVocê tem {maximo_de_tentativas-t} tentativas')
        try:
            p = int(input('Seu palpite: '))
            if p == n:
                print('Parabéns, você ACERTOU :)')
                placar_voce += 1
                os.system('pause')
                break
            elif t == maximo_de_tentativas-1:
                print('Acabaram suas tentativas :(')
                placar_pc += 1
                os.system('pause')
                break
            elif p < n:
                print('Chute um valor maior')
                os.system('pause')
            elif p > n:
                print('Chute um valor menor')
                os.system('pause')
            t += 1
        except:
            print('Digite apenas números...')
            time.sleep(1)
    
    if placar_pc == 3 or placar_voce == 3:
        os.system('cls')
        print(f'Placar:\nVocê [{placar_voce}] / Pc [{placar_pc}]')
        if placar_pc > placar_voce:
            print('Você PERDEU :(')
        elif placar_pc < placar_voce:
            print('Você VENCEU :)')
        elif placar_pc == placar_voce:
            print('EMPATE :O')
        break
    else:
        while True: 
            os.system('cls')
            print(f'Placar:\nVocê [{placar_voce}] / Pc [{placar_pc}]')
            op = input('Jogar de novo? [s/n]\n⇨ ')
            op = op.lower()
            if op == 's':
                break
            elif op == 'n':
                if placar_pc > placar_voce:
                    print('Você PERDEU :(')
                elif placar_pc < placar_voce:
                    print('Você VENCEU :)')
                elif placar_pc == placar_voce:
                    print('EMPATE :O')
                os._exit(0)






