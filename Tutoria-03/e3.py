'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
crp = float(input('CONTROLE DE QUALIDADE – COMPRESSÃO\nValor padrão da carga de compressão (kg/cm2): '))
na = int(input('Número de amostras: '))
print()
x = 5000000
for i in range(1 , na + 1):
    a = float(input(f'Área da amostra {i} (cm2): '))
    p = float(input(f'Peso da amostra {i} (kg):  '))

    if p / a < x:
        x = p / a
print(f'\nCARGA DE RUPTURA MÍNIMA = {x}')
print('CIMENTO APROVADO.') if x >= crp else print('CIMENTO REPROVADO.')
