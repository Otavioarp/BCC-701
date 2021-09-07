'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
t = str(input('Tipo: '))
while t != 'fim' :
    pa = float(input('Preço atual: '))
    while pa <= 0:
        pa = float(input('Preço Inválido!\nPreço atual: '))
    if t == 'Alimentos' :
        if pa <= 50:
            a = 110/100
        elif pa <= 100:
            a = 112/100
        else:
            a = 115/100
        pf = pa * a
    elif t == 'Limpeza' :
        if pa <= 50:
            l = 109/100
        elif pa <= 100:
            l = 110/100
        else:
            l = 111/100
        pf = pa * l
    elif t == 'Transporte' :
        pf = pa * 106/100
    else: 
        pf = pa * 104/100

    print(f'Preço reajustado: R$ {pf:.2f}')
    t = str(input('Tipo: '))
