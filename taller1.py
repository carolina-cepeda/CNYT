#Carolina Cepeda
import  math

def sumacplx(a,b):
    return (a[0]+b[0],a[1]+b[1])

def multplx(a,b):
    return ((a[0]*b[0])-(b[1]*a[1]),(a[0]*b[1])+(a[1]*b[0]))

def restacplx(a,b):
    return ((a[0]-b[0],a[1]-b[1]))

def divcplx(a,b): #a/b
    div_1 = ((a[0]*b[0])+(a[1]*b[1])) / (b[0]**2 + b[1]**2)
    div_2 = ((b[0]*a[1])-(a[0]*b[1])) / (b[0]**2 + b[1]**2)
    return (div_1,div_2)

def conjugado(a):
    con = (a[0],int(a[1]) * int(-1))
    return con

def modu(a):
    modulo = float(math.sqrt((a[0]**2) + (a[1]**2)))
    return modulo

def fas(a): #angulo
    real= int(a[0])
    imag= int(a[1])
    fas = math.atan(real/imag)

    return fas

def a_polar(a):
    x = a[0]
    y= a[1]
    fase = fas(a)
    if x < 0 and y < 0:
        fase += math.pi

    elif x < 0 and  y >0 :
        fase -=  math.pi

    return (modu(a),fase)

def a_cartesiana(a):
    return ( a[0] * math.cos(a[1]),a[0] * math.sin(a[1]) )

if __name__ == '__main__':
    print(a_cartesiana((4,5)))
