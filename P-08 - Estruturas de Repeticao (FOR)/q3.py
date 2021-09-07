'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
def realizaVotacao(qnt_ele):
    global num_1 , num_2
    invalidos ,candidato1 , candidato2= 0 , 0 , 0
    print('\n## Votação Iniciada')
    for i in range (0,qnt_ele):
        voto = int(input('Digite o número do candidato que você deseja votar: '))
        if voto == num_1:
            candidato1 += 1
        elif voto == num_2:
            candidato2 += 1
        else:
            invalidos += 1
    print('## Votação Encerrada')
    return candidato1 + candidato2 , invalidos , candidato1 , candidato2


cand_1 = input('Digite o nome do candidato 1: ')
num_1 = int(input('Digite o número do candidato 1: '))
cand_2 = input('Digite o nome do candidato 2: ')
num_2 = int(input('Digite o número do candidato 2 '))

qnt_e = int(input('Digite a quantidade de eleitores: '))
while qnt_e < 3:
    qnt_e = int(input('A quantidade de eleitores é inferior a 3\nDigite a quantidade de eleitores: '))

votos_v , votos_i , can_1 , can_2 = realizaVotacao(qnt_e )

print(f'''
Votos válidos: {votos_v  / qnt_e* 100:.2f}% ({votos_v} votos)
Votos inválidos: {votos_i / qnt_e* 100 :.2f}% ({votos_i} votos)''')
if votos_v == 0:
    votos_v = 1
print(f'''Votos para {cand_1}: {can_1  / votos_v* 100:.2f}% ({can_1} votos)
Votos para {cand_2}: {can_2  / votos_v* 100:.2f}% ({can_2} votos)''')
