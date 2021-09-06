

def preencherVetor(valores, tipo):
    vetor = []
    valores = valores.split(',')
    for i in range(len(valores)):
        if tipo == 'int' :
            valor = int(valores[i].strip())
        elif tipo == 'float':
            valor = float(valores[i].strip())
        else:
            valor = valores[i].strip()
        vetor.append(valor)
    return vetor


def estatNotas(vetor):
    med = 0
    for i in range(len(vetor)):
        med += vetor[i]
        if vetor[i] < menor
    x = min(vetor)
    y = max(vetor)
    return y , x , med/len(vetor)


notas = input('Notas: ')
vec = preencherVetor(notas ,'float')
max , min , media = estatNotas(vec)

print(f'Maior nota: {max:.1f}')
print(f'Menor nota: {min:.1f}')
print(f'Nota média: {media:.1f}')
