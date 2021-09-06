'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
vtc=float(input('Qual o Valor Total da Compra? '))
  
  
if vtc > 0:
    if 0 < vtc <= 300:
        d=98/100
    elif 300 < vtc <= 600:
        d=96/100
    elif 600 < vtc <= 900:
        d=94/100
    else:
        d=92/100
    print(f'Valor do pagamento: R$ {vtc*d:.2f} ')
    
else:
    print('ERRO: Valor de compra inválida! ')
      
      
      
      