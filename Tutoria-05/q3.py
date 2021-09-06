'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
import math
def valida_input():
    i = input('Deseja sair? (s/S/n/N): ')
    x = i.lower()
    comp = x == 's' or x == 'n'
    while comp == False  :
        print(f'ERRO: opção inválida ! {i} ')
        i = input('Deseja sair? (s/S/n/n): ')
        x = i.lower()
        comp = x == 's' or x == 'n'
    if x == 'n' or x == 'N':
        comp = True
    else :
        comp = False
    return comp


i0 = 2*10**-6
q = 1.602 * 10 ** -19
k = 1.38 * 10 ** -23
x = True
while x == True:
    temp_k = float(input('Informe a temperatura (em Kelvin): '))
    print('Tensão   |   Corrente ')
    tensao = -1
    while tensao <= 0.6:
        id  = i0 * (math.e**((q*tensao)/(k*temp_k))-1)
        print(f' {tensao:5.1f}   |   {id:1.1f}')
        tensao += 0.1
    x = valida_input()

else:
    print('Fim do Programa ! ')
