'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
si=float(input('Saldo inicial:  '))
op=int(input('Opção\n1. Saldo\n2. Depósito\n3. Retirada\n_'))
vd=int()
if(0<op<4):
    if(op==1):
        print(f'Seu saldo atual é R$ {si:.2f} ')
    elif(op==2):
        vd=float(input('Valor a ser depósitado  '))
        print(f'Seu saldo agora é R$ {si+vd:.2f}')
    elif(op==3):
        vr=float(input('Valor a ser retirado  '))
        if((si+vd)>=vr):
            print(f'Retirada com sucesso\nSeu saldo agora é R$ {si+vd-vr:.2f} ')
        else:
            print(f'Saldo insuficiente,seu saldo atual é R$ {si+vd:.2f}')
            
        
        
    
    
    
    
else:
    print('Opção inválida!')
print('Fim da operação!')