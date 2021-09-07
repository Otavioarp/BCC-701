'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
def avaliapresentacao()


n = int(input('Saltos Ornamentais:\nInforme o número de competidores: '))
for i in range(0 , n ):
    nj = int(input('Informe o número de juízes: '))
    nome = str(input('Nome do competidor: '))
    g = float(input('Grau de dificuldade: '))

    for j in range(0 , nj):
        nt = float(input('Nota juiz: '))
        nmin , nmax , med = 11 , 0 , 0
        if nt < nmin:
            nmin = nt
            med += nmin

        elif nt > nmax:
            med += nmax
            nmax = nt
        else:
            med += nt

    print(f'A {nome} obteve {med * g :.2f} pontos.\n')
