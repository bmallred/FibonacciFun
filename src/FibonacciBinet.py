from math import log

phi = (1 + 5 ** 0.5) / 2

def fib(n):
    '''
    Find the Fibonacci number using Binet's formula.
    '''
    
    return int(round((phi ** n - (1 - phi) ** n) / 5 ** 0.5))

def fibinv(f):
    '''
    Inverse Fibonacci function using Binet's formula.
    '''
    
    if f < 2:
        return
    
    return int(round(log(f * 5 ** 0.5) / log(phi)))