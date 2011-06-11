def powLF(n):
    if n == 1:
        return (1, 1)
    
    L, F = powLF(n // 2)
    L, F = (L ** 2 + 5 * F ** 2) >> 1, L*F
    
    if n & 1:
        return ((L + 5 * F) >> 1, (L + F) >> 1)
    
    return (L, F)

def fib(n):
    '''
    Find the Fibonacci number using Lucas numbers.
    '''
    
    if n & 1:
        return powLF(n)[1]
    else:
        L, F = powLF(n // 2)
        return L * F 