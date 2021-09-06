'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
def realizaCalculos(n,r):
    pi = 0
    for i in range (0,n):
        sun = (-1) ** i * (4 / (2 * i +1 ))
        pi += sun
    v = (4 / 3) * pi * r ** 3
    return pi , v

n_termos = int(input('Número de termos: '))
raio = int(input('Raio da esfera: '))

pii , vol = realizaCalculos(n_termos,raio)

print(f'pi = {pii:.5f}.')
print(f'Volume da esfera = {vol:.5f}.')
