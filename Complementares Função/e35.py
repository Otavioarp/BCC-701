'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
def custo(v,t,r,p):
        return ( v * t / r ) * p


vel_med = float(input('Custo do combustível em uma viagem\nVelocidade média (km/h): '))
temp_p = float(input('Tempo previsto (h): '))
rend_g = float(input('Rendimento com gasolina (km/litro): '))
p_gas = float(input('Preço do litro de gasolina       (R$): '))
p_alc = float(input('Preço do litro do álcool         (R$): '))

x = custo(vel_med, temp_p, rend_g,p_gas)
y = custo(vel_med, temp_p, rend_g*0.7,p_alc)

print(f'Custo usando gasolina (R$): {x:.2f}')
print(f'Custo usando álcool   (R$): {y:.2f}')
