#5 * 6
#
#5 ** 6
#
#5/6
#
#5 % 6
#
#5 // 3
#
#a = 7
#Število_ljudi = 15
#Število_ljudi
#
#import math
#math.sin(math.pi)
##programski jeziki delajo numerično, torej poda približek 0 in ne 0, ker ima samo končno mnogo decimalk pija
#
#3e-5 * 100000
#xe-n, kjer je x iz realnih in n naravno število je krašji zapis za x*10^n

#PRIMER: izračun na tetraedru
a = 1
b = 1
c = 1
d = 2
e = 2
f = 2

def ploscina_trikotnika(a, b, c):
    """Izračuna ploščina trikotnika iz stranic"""
    #uporabimo hrenovo formulo
    s = (1/2) * (a + b + c)
    ploscina = (s * (s - a) * (s - b) * (s - c)) ** (1/2)

    return ploscina

def povrsina_tetraedra(a, b, c, e, f):
    abc = ploscina_trikotnika(a, b, c)
    cef = ploscina_trikotnika(c, e, f)
    ebd = ploscina_trikotnika(e, b, d)
    fda = ploscina_trikotnika(f, d, a)

    povrsina = abc + cef + ebd + fda

    return povrsina


