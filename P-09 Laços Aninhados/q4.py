
meta_nac = float(input('Meta nacional: R$ '))
total_nac , i = 0 , 1
while total_nac < meta_nac :
    total_est ,vendas_city , j =  0 , 0 , 1
    nome_est = input(f'. Nome do estado {i}: ')
    meta_est = float(input('. Meta estadual: R$ '))
    while total_est < meta_est :
        vendas_city = float(input(f'.. Vendas na cidade {j}: R$ '))
        total_est += vendas_city
        j += 1
    total_nac += total_est
    i += 1
    print(f'.. Meta no estado {nome_est} atingida, valor total: R$ {total_est:.2f}.')
print(f'Meta nacional cumprida, valor total: R$ {total_nac:.2f}.')
