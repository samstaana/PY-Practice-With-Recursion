# Write code for algorithm 3 below
def nth_fib(n):
    if n <= 0:
        print('NO')
    elif n ==1:
        return 0
    elif n ==2:
        return 1
    return nth_fib(n - 1) + nth_fib(n - 2)

print(f'The second fib number is {nth_fib(2)}')
print(f'The sixth fib number is {nth_fib(6)}')
print(f'The eighth fib number is {nth_fib(8)}')
print(f'The tenth fib number is {nth_fib(10)}')