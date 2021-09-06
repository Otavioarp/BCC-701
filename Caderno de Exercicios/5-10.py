'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
n = int(input('Número de espécies: '))

while:
    n0 = int(input(f'Entre com os dados da Espécie {i}\nPopulação Inicial: '))
    r  = float(input('Taxa de crescimento: '))
    k = int(input('Nível de saturação: '))


    x += n*(1+r)
    print(f'São necessárias 7 gerações.')
    print(f'População final: {x}')
'''N0 = N i−1 ∗ (1 + r)
 N 0 = N i−1 ∗ (1 + r), ou seja, o
número de indivíduo da próxima geração (i) é igual ao número de indivíduos da geração atual (n-1)
acrescido dos “novos” indivíduos, escreva um programa para:'''
