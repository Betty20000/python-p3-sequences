#!/usr/bin/env python3

def print_fibonacci(length):
    fib_sequence = []
    first_num = 0
    second_num = 1
    for _ in range(length):
        fib_sequence.append(first_num)
        temp = first_num + second_num
        first_num = second_num
        second_num = temp
    print(fib_sequence)

print_fibonacci(9)
    
