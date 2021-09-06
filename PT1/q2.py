
print('DECOM - Projeto de extensão ')
nome = input('Nome: ')

n512 = float(input('Nota em BCC512: '))
while n512 < 0 or n512 > 10:
    n512 = float(input('Nota em BCC512: '))

n552 = float(input('Nota em BCC552: '))
while n552 < 0 or n552 > 10:
    n552 = float(input('Nota em BCC552: '))

n760 = float(input('Nota em BCC760: '))
while n760 < 0 or n760 > 10:
    n760 = float(input('Nota em BCC760: '))
mp = (n512 + n552 * 2 + n760 * 3) / 6
print(f'{nome} tem média {mp:.2f}')
if mp >= 6:
    print('Pode participar como bolsista. ')
else:
    print('Não pode participar. ')
