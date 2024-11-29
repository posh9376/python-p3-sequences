#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_sequence = [0, 1]
    if length == 0:
        return print('[]')
    elif length == 1:
        return print('[0]')
    elif length == 2:
        return print(fibonacci_sequence)
    while len(fibonacci_sequence) < length:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return print(fibonacci_sequence)

print_fibonacci(5)

