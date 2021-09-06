'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''

def validaEntradas(ma,mo):
    if ma<0 or mo<0:
        return  False
    return True
    

def calculaCustos(mo,ma):
    pma=ma*1.8
    if ma>5:
        pma=ma*1.5    
    pmo=mo*2.5
    if mo>5:
        pmo=mo*2.2
    return pmo,pma
        

wkg=float(input('Quantidade de Morangos (em kg): '))
akg=float(input('Quantidade de Maçãs (em kg): '))

if  validaEntradas(wkg,akg):
    a,b =calculaCustos(wkg,akg)
    print(f'O valor pago pelos morangos é R$ {a:.2f}\nO valor pago pelas maçãs é R$ {b:.2f}\nO valor total da sua compra é R$ {a+b:.2f}')
else:
    print('Entrada inválida ')

   


