'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
n = int(input('Digite o valor de N: '))

soma_par , soma_impar = 0 , 0
for i in range (1 ,n+1,2):
    soma_impar += i
for j in range(0,n+1,2):
    soma_par += j

print(f'A soma dos valores pares é: {soma_par}')
print(f'A soma dos valores impares é: {soma_impar}')
