memory = {0: 0, 1: 1}

def fib(n):
    '''
    Find the Fibonacci number with the help of cached results.
    '''
    
    if not n in memory:
        memory[n] = fib(n - 1) + fib(n - 2)
    
    return memory[n]