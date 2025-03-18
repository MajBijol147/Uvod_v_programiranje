def multiples_3_5(upper_limit):
    multiples_3 = list(range(0,upper_limit,3))
    multiples_5 = list(range(0,upper_limit,5))
    
    multiples_sum = sum(list(dict.fromkeys(multiples_3 + multiples_5)))
    
    return multiples_sum

#NAPAKA: številke v listih se ponavljajo (npr. 15 je v obeh listih in se zato sešteje dvakrat)

        