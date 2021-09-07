'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
def calculoIMC(p1,h1):
    return p1/h1**2

def difPeso(p1,imcd,h1):
    return p1-(imcd*h1**2)
    
    

p=float(input('Digite seu peso (em kg): '))
h=float(input('Digite sua altura (em metros): '))
s=input('Seu sexo é masculino (M) ou feminino (F)? ')

if s=='M':
    if calculoIMC(p,h) >25:
        imcd=25
        print(f'Você deve perder {difPeso(p,imcd,h):.2f}kg para ter IMC = 25 ')
        
    else:
        print('Você não precisa perder peso para ter IMC <= 25 ')
else:
    if s=='F':
        if calculoIMC(p,h) >24:
            imcd=24
            print(f'Você deve perder {difPeso(p,imcd,h):.2f}kg para ter IMC = 24 ')
            
        else:
            print('Você não precisa perder peso para ter IMC <= 24 ')
    else:
        print('A entrada contém dados não reconhecidos ')
