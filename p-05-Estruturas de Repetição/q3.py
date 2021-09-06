'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
def calculaJ(capital, meses):
    if capital <= 10000:
        taxa = 0.1
    else:
        taxa = 0.07
    return capital * taxa * meses , taxa
cap_p_emprestimo=float(input('Capital Total para empréstimo: '))
cap_emprestado=float(input('Capital emprestado: '))

while(cap_p_emprestimo >= cap_emprestado):
    meses_p_quitar = int(input('Quantidade de meses para quitação: '))
    juros_devido, taxa_j_aplic = calculaJ(cap_emprestado, meses_p_quitar)
    print(f'Taxa de juros aplicada: {taxa_j_aplic*100:.2f} %.\nJuros devido: {juros_devido:.2f}.\nValor total: {juros_devido+cap_emprestado:.2f}.')
    cap_emprestado = float(input('Capital emprestado: '))
    cap_p_emprestimo -= cap_emprestado

print(f'Empréstimo negado, capital total é de R$ {cap_p_emprestimo:.2f}.')
