#seznam.append doda element na konec seznama. seznama lahko spreminjaš, saj so objekt v spominu računalnika za razliko od nizov,
#ki so fiksni in z vsako spremembo ustvariš nov seznam.
#Enako lahko spreminjaš posamezne elemente v seznamu v spominu ali pa cele rezine

#funkcija sorted() vrne nov seznam, metoda seznam.sort() pa spremeni seznam v spominu.

# == in <,> primerjajo seznama leksikografsko. /is/ preveri če dve spremenljivki kažeta na isto pozicijo v spominu, 
#kar bi pomenilo, da sta spremenljivki isti objekt
#block formater, flake8

mat = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

def matrika_nicel(n, m):
    matrika = []
    
    for i in range(n):
        vrstica = m * [0]
        matrika.append(vrstica)
        
    return matrika