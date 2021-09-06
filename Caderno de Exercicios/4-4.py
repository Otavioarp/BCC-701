'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br

'''
vtc=float(input('Qual o valor total da cpmpra ? '))

if(vtc>0):
    if(0<vtc<=300):
        print(f'Valor do pagamento : R$ {vtc-2/100*vtc:.2f}')
    elif(300<vtc<=600):
        print(f'Valor do pagamento : R$ {vtc-4/100*vtc:.2f}')
    elif(600<vtc<=900):
        print(f'Valor do pagamento : R$ {vtc-6/100*vtc:.2f}')
    elif(vtc>=900):
        print(f'Valor do pagamento : R$ {vtc-8/100*vtc:.2f}')
else:
    print(f'ERRO: valor da compra inválida ! ')