"""
Time complexity of Fibonacci
Answer: O(2^n)

                        fib(n)                      => 1 = 2^0
                      /       \
                 fib(n-1)     fib(n-2)              => 2 = 2^1
                /    \         /     \
        fib(n-2) fib(n-3)  fib(n-3)  fib(n-4)       => 4 = 2^2
                    ....................

    => fib(n) = 2^0 + 2^1 + ... + 2^n => 2^(n+1)-2 => O(2^n)
"""


def fib(n):
    if n <= 0:
        return 0

    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)


print(fib(5))
