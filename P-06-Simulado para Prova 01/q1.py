vc = float(input('Defina o valor total da compra: R$ '))


if vc <= 0:
    print('Erro: Valor total inválido. ')
else:
    if vc <= 250:
        d = 3/100
    elif vc <= 550:
        d = 6/100
    elif vc <= 750:
        d = 8/100
    else:
        d = 10/100
    print(f'Desconto de {d* 100:.0f}%.\nValor com desconto: R$ {vc-d*vc:.2f}')
