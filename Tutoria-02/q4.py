'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
def SalarioLiquido(a,b,c):
    return a*b*((100-c)/100)

vha=float(input('Cálculo do Salário Líquido\nValor da hora-aula (R$): '))
hm=int(input('Horas ministradas (h): '))
di=float(input('Desconto do INSS (%): '))
print(f'Salário líquido (R$): {SalarioLiquido(vha,hm,di):.2f} ')
