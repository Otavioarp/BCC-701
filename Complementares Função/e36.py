'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
import math

def A():
    return math.sin(3.1415) * math.cos ( 2 * math.pi + 1.34 ** 1.789)


def B():
    return 1 / (78.99 / 45.9 ** 0.248) ** (1/2)


def C():
    return 1 / (2.567 + 0.876 ** 2) ** 3

a , b , c = A () , B() , C()

e = (a + b) ** (1/3) * (2.789 / (b ** (c+a)))

print(f'{a:.5f}')
print(f'{b:1.5f}')
print(f'{c:1.5f}')
print(f'{e:1.5f}')
