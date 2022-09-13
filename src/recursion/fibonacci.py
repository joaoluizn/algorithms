""" 
Fibonacci Solution using Recursion
Complexity of Time: 2^N
Complexity of Space: N 
"""

def fibonacci(factor):
    if factor == 1 or factor == 2:
        return 1
    elif factor == 0:
        return 0
    else:
        return fibonacci(factor - 2) + fibonacci(factor - 1)
