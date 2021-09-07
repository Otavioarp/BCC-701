'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
id=int(input('Idade :  '))
c=float()
if(id>18):
    vb=float(input('Valor base:  '))
    s=int(input('Sexo:  '))
    ec=int(input('Estado civil:  '))
    if(ec==2):
        c+=5
    if(s==2):
        id=-5
    if(18<id<30):
        c+=0.8
    elif(31<id<55):
        c+=1.2
    elif(id>55):
        c+=1.6
       
    print(f'Com {c:.2f}% de acréscimo o valor final é R$ {c/100*vb+vb:.2f}')           
else:
    print('Idade inválida ')






