nome_p = input('Informe o nome do produto: ')

while nome_p != 'fim':
    vp = float(input('Valor do pedido: R$ '))
    d = 0
    if nome_p == 'Pão de queijo':
            if vp <= 50:
                d = 10/100
            elif vp <= 100:
                d = 12/100
            else:
                d = 15/100
    elif nome_p == 'Pastel de angu':
            if vp <= 50:
                d = 9/100
            elif vp <= 100:
                d = 10/100
            else:
                d = 11/100
    print(f'Percentual de desconto: {d*100:.2f}%')
    print(f'Valor com desconto: R$ {vp-vp*d:.2f}')
    nome_p = input('Informe o nome do produto: ')
