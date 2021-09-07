'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
print('Secretaria de Saúde de Elysium ')
ds = int(input('Dimensão da sala: '))

if ds > 0:
    if ds <= 10:
        qnt_mesas = int(ds/1.5)
    elif ds <= 30:
        qnt_mesas = int(ds/2.0)
    elif ds <= 70:
        qnt_mesas = int(ds/2.5)
    else:
        qnt_mesas = int(ds/3.0)
    print(f'- Sala: {ds:.1f} m**2')
    print(f'- Quantidade de mesas: {qnt_mesas}')

else:
    print('ERRO: dimensão nula ou negativa. ')
