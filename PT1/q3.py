
def Efetividade(v1,v,p1,p):
    return (1-v*p1/(p*v1))*100


print('Ministério da Saúde da Argentina ')
print('Efetividade de Vacinas ')
nome_vac = input('Defina o nome da vacina: ')
x ,n_max = 0 ,1
while nome_vac != '':
    vg = int(input('- Defina V: '))
    vp = int(input('- Defina v: '))
    pg = int(input('- Defina P: '))
    pp = int(input('- Defina p: '))
    efet = Efetividade(vg,vp,pg,pp)
    print(f'- Efetividade (E) de {nome_vac}: {efet:.2f}% ')

    if efet > x:
        nome_max = nome_vac
        e_max = efet
        x = efet
    nome_vac = input('Defina o nome da vacina: ')
print(f'Vacina {nome_max} possui a maior efetividade (E): {e_max:.2f}%' )
