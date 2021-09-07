'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
sexo = int(input('Sexo: '))
tc = int(input('Tempo de contribuição em 2019: '))
i = int(input('Idade em 2019: '))
ano , pm , po = 2019 , 0 , 0
po = tc + i
if sexo == 1:
    pm = 86
else:
    pm = 96
    print('Ano | Pont. Min. | Pont. Obtida')
for i in range(2019,2040):

    print(f'{ano}|        {pm}|       {po}')
    ano += 1
    po += 2
    if pm < 105:
        pm += 1
    else :
        pm == 105
