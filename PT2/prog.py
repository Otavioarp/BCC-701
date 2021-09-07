
'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
qnt_mat = int(input('Digite a quantidade de materias : '))
car_total = int(input('Digite a carga horaria total do periodo : '))
soma = 0
for i in range(qnt_mat):
    mat = input('Digite a materia : ')
    car = int(input(f'Digite a carga horaria da materia {mat}: '))
    nota = float(input(f'Digite a nota da materia {mat}: '))
    soma += (nota * car)/car_total
print(f'cre = {soma}')