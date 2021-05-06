# A code snippet to find the nth term in the fibonnaci sequence
# Mainly used to practice recursion

import sys

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)

num = int(sys.argv[1])
term = fib(num)
print(term)

