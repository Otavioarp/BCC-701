'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''

def fun( j , a , b ):
    x , y , i , fat = 1 , 1 , 1 , 1
    if j == 1 :
        x , y = 1 , 1
    elif j == 2 :
        x = 3
        y = 7
    elif j > 2:
        x = a + 2
        y = b + 6
    while i <= j:
        fat = fat * i
        i += 1
    return fat , x , y

n = int(input('INFORME O NÚMERO DE PARCELAS:  '))
while n <= 0:
    n = int(input('VALOR INVÁLIDO PARA n !\nINFORME O NÚMERO DE PARCELAS:  '))
i , x , y , t = 1 , 1 , 1 , 0
while i <= n:
    fa , x , y = fun( i , x , y )
    if i % 2 == 0:
        t += (x * 50 - y * -80)  / fa
    elif i % 2 != 0:
        t += (x * 50 + y * -80)  / fa
    i += 1


print(f'VALOR DO SOMATÓRIO COM {n} PARCELAS: {t} ')
