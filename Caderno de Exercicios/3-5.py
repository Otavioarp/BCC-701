'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''


v = int(input('Velocidade média (km/h):'))
t = int(input('Tempo de percurso (h):'))
rg = float(input('Rendimento com gasolina(Km/litro):'))
pg = float(input('Preço do litro de Gasolina(R$):'))
pa = float(input('preço do litro de álcool (R$):'))

ra=rg * 0.7

print(f'Custo usando gasolina = R${((v*t)/rg )* pg:.2f}')
print(f'Custo usando ácool =  R${((v*t)/ra )* pa:.2f} ')
