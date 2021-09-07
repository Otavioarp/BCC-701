'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''







nome_j = input('Informe o nome do juiz: ')
qnt_p = int(input('Quantidade de partidas: '))
imp , f , t , c = 0 , 0 , 0 , 0
for i in range(0,qnt_p):
    print(f'\nPartida {i+1}:')
    imped = int(input('. Impedimentos.......: '))
    faltas = int(input('. Faltas.............: '))
    cart = int(input('. Cartões............: '))
    temp_a = float(input('. Tempo de acréscimo.: '))
    imp += imped
    f += faltas
    c += cart
    t += temp_a
print(f'''\n
Estatísticas do juiz {nome_j}:
. Impedimentos.......: {imp / qnt_p:.2f}.
. Faltas.............: {f / qnt_p:.2f}.
. Cartões............: {c / qnt_p:.2f}.
. Tempo de acréscimo.: {t / qnt_p:.2f}.''')
