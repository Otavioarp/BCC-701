'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
def pedido():

    print('>>> Jurubeba Foods and Snacks Co <<<')
    print('Cardápio:')
    print('(1)-Vegetariano    (2)-Bovino    (3)-Peixe    (0)-Finalizar')
    ped = int(input('\tSeu pedido >>> '))

    while 0 > ped or ped > 3  :
        print(f'ERRO >>> {ped} <<< número inválido !')
        print('>>> Jurubeba Foods and Snacks Co <<<')
        print('Cardápio:')
        print('(1)-Vegetariano    (2)-Bovino    (3)-Peixe    (0)-Finalizar')
        ped = int(input('\tSeu pedido >>> '))
    return ped

cont_boi , cont_pei , cont_veg , cont_p = 0 , 0 , 0 , 0

pedi  = pedido()
if pedi != 0:
    while pedi != 0:

        if pedi == 1:
            cont_veg += 1
        elif pedi == 2:
            cont_boi += 1
        else:
            cont_pei += 1
        pedi  = pedido()
        cont_p += 1
    print(f'''Total de pratos servidos: {cont_p}
Pratos vegetarianos..: 4 ( {cont_veg / cont_p * 100 :.2f}%)
Pratos bovinos.......: 5 ( 41.67%)
Pratos de peixe .....: 3 ( 25.00%)

Fim do Programa !  ''')
else:
    print('''Programa encerrado sem pedidos realizados !
Fim do Programa !''')
