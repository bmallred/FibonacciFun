fibs = {0: 0, 1: 1}

def fib(n):
    '''
    Find the Fibonacci number using the Djikstra method.
    '''
    
    if n in fibs:
        return fibs[n]
    elif n % 2 == 0:
        fibs[n] = ((2 * fib((n / 2) - 1)) + fib(n / 2)) * fib(n / 2)
        return fibs[n]
    else:
        fibs[n] = (fib((n - 1) / 2) ** 2) + (fib((n + 1) / 2) ** 2)
        return fibs[n]