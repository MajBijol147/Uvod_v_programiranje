def multiples_3_5(upper_limit):
    multiples_3 = list(range(0,upper_limit,3))
    multiples_5 = list(range(0,upper_limit,5))
    multiples_both = list(dict.fromkeys(multiples_3 + multiples_5))
    for n in multiples_both:
        if multiples_both.count(n) > 1:
            multiples_both.pop(n)
    
    multiples_sum = sum(multiples_both)
    
    return multiples_sum

#NAPAKA: številke v listih se ponavljajo (npr. 15 je v obeh listih in se zato sešteje dvakrat)

        