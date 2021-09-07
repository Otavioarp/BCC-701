'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
qnt_pa = int(input('Quantidade de pacientes: '))
p_oe, p_mg = 0, 0
for i in range(0, qnt_pa):
    peso = float(input('Peso: '))
    altura = float(input('Altura: '))
    imc = peso / altura ** 2

    if imc < 16:
        clas = 'Magreza grave'
        p_mg += 1
    elif imc < 18.8:
        clas = 'Abaixo do peso'
    elif imc < 25 :
        clas = 'Saudável'
    elif imc < 30:
        clas = 'Sobrepeso'
    elif imc < 40:
        clas = 'Obesidade'
    else:
        clas = 'Obesidade extrema'
        p_oe += 1
    print(f'O IMC é {imc:.2f} ==> {clas}\n')
print(f'''
Percentual para Magreza grave: {p_mg / qnt_pa * 100:.2f}%
Percentual para Obesidade extrema: {p_oe / qnt_pa * 100:.2f}%''')
