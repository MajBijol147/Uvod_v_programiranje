#rekurzija

def fakulteta_med(n, m):
    """"Vrne m * (m - 1) * ... * n."""
    if n==m:
        return m
    
    return m * fakulteta_med(n, m - 1)

def posploseni_fibonacci(n,a=1 ,b=1):
    """Vrne n-ti člen Fibonaccijevega zaporedja"""
    if n==0:
        return a
    if n==1:
        return b
    
    rezultat = posploseni_fibonacci(n - 1, b, a + b)
    
    return rezultat