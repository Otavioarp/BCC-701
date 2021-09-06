'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
p=float(input('Digite seu peso (em kg): '))
h=float(input('Digite sua altura (em metros): '))
s=input('Seu sexo é masculino (M) ou feminino (F)? ')

imc=p/h**2

if s=='M':
    if imc>25 :
        print(f'Você deve perder {p-25*h**2:.2f}kg para ter IMC = 25  ')
    else:
        print('Você não precisa perder peso para ter IMC <= 25  ')
else:
    if s=='F':
        if imc>24 :
            print(f'Você deve perder {p-24*h**2:.2f}kg para ter IMC = 24  ')
        else:
            print('Você não precisa perder peso para ter IMC <= 24  ')
    else:
        print('ERROR: A entrada contém dados não reconhecidos  ')
