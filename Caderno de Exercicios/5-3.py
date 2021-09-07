'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
v = input('Chapa: ')
ca,cb,cc,n = 0,0,0,0
while (v != 'q') :
    if v == 'a':
        ca +=1
    elif v == 'b':
        cb +=1
    elif v == 'c':
        cc += 1
    else:
        n +=1
    v = input('Chapa: ')
print(f'''Resultado:
− Chapa a: {ca} voto(s)
− Chapa b: {cb} voto(s)
− Chapa c: {cc} voto(s)
− Nulos  : {n} voto(s)''')
