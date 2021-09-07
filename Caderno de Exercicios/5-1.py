'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
qp=int(input('Quantidade de pacientes: '))
i,a,b = 0,0,0
while i < qp:
    p=float(input('Peso: '))
    h=float(input('Altura: '))
    imc=p/h**2
    i+=1
    if imc < 16:
        x = 'Magreza grave'
        a+=1
    elif imc < 18.5:
        x = 'Abaixo do peso'
    elif imc < 25:
        x = 'Saudável'
    elif imc < 30:
        x = 'Sobrepeso'
    elif imc < 40:
        x = 'Obesidade'
    else:
        x = 'Obesidade extrema'
        b += 1
    print(f'O IMC é {imc:.2f} ==> {x}')
print(f'Percentual para Magreza grave: {a*100/qp:.2f}%.\nPercentual para Obesidade extrema: {b*100/qp:.2f}%.')
