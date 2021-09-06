def efetividade(a, b, c, d):
    k = (1-((b*c)/(d*a)))*100
    return k

print('Ministerio de saude do Uruguai')
print('Efetividade de Vacinas')
i=0

nome = input('informe o nome da Vacina: ')
while nome != '':
    Vpe= int(input('Informe V: '))
    vcon= int(input('Informe v: '))
    pcon= int(input('Informe p: '))
    Pla= int(input('Informe P: '))
    k = efetividade(Vpe, vcon, Pla, pcon)
    print(f'{K}')
    if k > i:
        kmaior = k
        i= K
        nomemaior = nome
    nome = input('informe o nome da Vacina: ')

print(f'(Vacina{nomemaior} possiu a maior efetividade (K): {kmaior:.3f}%')
