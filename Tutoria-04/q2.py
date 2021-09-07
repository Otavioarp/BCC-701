'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
ling_ap, peso_med, m_max = 0, 0, 0
for i in range(0,5):
    m_ling = float(input(f'Digite a massa do lingote {i+1}: '))
    if m_ling > 24.9:
        ling_ap += 1
        peso_med += m_ling
        if m_ling > m_max:
            m_max = m_ling
print(f'''
Número de lingotes aproveitados:{ling_ap}
Peso médio dos lingotes aproveitados: {peso_med/ling_ap:.1f} kg
Maior peso de um lingote aproveitado: {m_max:.1f} kg''')
