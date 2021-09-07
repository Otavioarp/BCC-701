'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
import math
def F(xf,yf):
    if -math.inf<xf<=10:
        zf=xf**2+2*yf-3
    elif 10<xf<=40:
        zf= math.sin (2*xf) * math.cos (4*yf)
    elif 40<xf<=80:
        zf=1/xf**-2+yf**(1/2)
    elif 80<x<=100:
        zf=(xf+yf)/(xf-yf)
    elif 100<xf<math.inf:
        zf=math.pi
    return zf

print(f" x y f(x, y)")
for x in range(-30, (90+1), 30):
    for y in range(20, (60+1), 20):
        z = F(x, y)
        print(f"{x:8.2f} {y:8.2f} {z:8.2f}")