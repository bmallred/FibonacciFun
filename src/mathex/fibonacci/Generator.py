def fib():
    '''
    Generate each Fibonacci number in an infinite loop.
    '''
    
    a, b = 0, 1
    
    while 1:
        yield a
        a, b = b, a + b