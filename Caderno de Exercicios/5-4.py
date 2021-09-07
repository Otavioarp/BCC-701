'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
n = int(input('Quantidade de provas: '))
i,p2,p1,e = 1,0,0,0
while i <= n :

    a = float(input(f'=== Prova {i} ===\nPontuação da equipe 1: '))
    b = float(input('Pontuação da equipe 2: '))
    if a > b:
        p1 += 1
    elif b > a:
        p2 += 1
    else:
        e += 1
    i += 1
print(f'=== Resultados ===\nA equipe 1 venceu {p1} prova(s)\nA equipe 2 venceu {p2} prova(s)\nHouve {e} empate(s) entre as equipes')
if p1 > p2:
    x = 1
elif p2 > p1:
    x = 2
if p1 == p2:
    print('Houve empate entre as equipes!')
else:
    print(f'Equipe {x} é a vencedora ')
