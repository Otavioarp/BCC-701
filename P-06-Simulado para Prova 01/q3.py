

def avaliaApresentacao(qjf ):
    gd = float(input('\t. Grau de dificuldade: '))
    i , soma = 1 , 0
    while i <= qjf:
        nt = float(input(f' \t. Nota do juiz {i}: '))
        soma += nt
        i += 1
        pont = soma * gd
    print(f'\t. Pontuação da apresentação: {pont:.2f}')


qa = int(input('Defina a quantidade de apresentações: '))
jc = int(input('Defina a quantidade de juízes: '))
i = 1
while i <= qa:
        print(f'. Apresentação {i}: ')
        avaliaApresentacao(jc)
        i += 1
