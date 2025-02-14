#!/usr/bin/env python3

def print_fibonacci(n):
    if n <= 0:
        print([])
        return

    fibonacci = [0, 1] if n > 1 else [0]
    
    for i in range(2, n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    print(fibonacci)

# Example usage:
print_fibonacci(10)
