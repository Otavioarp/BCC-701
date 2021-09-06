
print('Caixa aberto! ')

val ,cont , val_t= 'naõ' , 0 , 0

while val != 'sim' :
    preco_f = 0
    qnt_p = int(input('\nQuantidade de itens do pedido: '))
    for i in range (0,qnt_p):
        preco = float(input(f'. Preço do item {i+1}: '))
        preco_f += preco
    dely = input('. Cobrar delivery? ')
    if dely == 'sim':
        preco_f += 15
    print(f'. Valor do pedido: R$ {preco_f:.2f}.')
    cont += 1
    val_t += preco_f
    val = input('Fechar o caixa? ')
print('\nCaixa fechado! ')
print(f'Número de pedidos: {cont}.')
print(f'Valor total vendido: R$ {val_t:.2f}.')
