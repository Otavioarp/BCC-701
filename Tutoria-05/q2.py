'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
def valida_input():
    i = input('Deseja calcular a Sequência de Collatz (s/S/n/N) ? ')
    x = i.lower()
    comp = x == 's' or x == 'n'
    while comp == False  :
        print(f'ERRO: Resposta inválida: {i} ')
        i = input('\nDeseja calcular a Sequência de Collatz (s/S/n/N) ? ')
        x = i.lower()
        comp = x == 's' or x == 'n'
    if x == 's' or x == 'S':
        comp = True
    else :
        comp = False
    return comp


controlx = valida_input()

while controlx == True:
    num = int(input('Digite um número inteiro positivo: '))
    print('Sequencia de Collatz:')
    print(f'{num} ',end='')
    while num != 1:
        if num % 3 == 0 :
            num = num/3
        elif num % 3 == 1 :
            num = (num * 4 + 2) / 3
        else:
            num = (2 * num -1) / 3
        print(f'{num:.0f} ',end='')
    print()
    print()
    controlx = valida_input()
else:
    print('Fim do Programa ! ')
