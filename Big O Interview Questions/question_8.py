"""
What is the time complexity of the below code
Answer:
    Assume T(n) is the time complexity of the factorial function
    T(0) = 0(1)
    T(n) = O(1) + T(n - 1)
         = 1 + T(n - 1) (O(1) is constant, so we can also replace it with 1)
         = 1 + [1 + T((n - 1) - 1] (spread out T(n - 1))
         = 2 + T(n - 2)
            ....
         = k + T(n - k) (k is a number <= n)

         For k = n, we have
         k + T(n - k) = n + T(n - n) = n + T(0) = n + O(1) = n (drop O(1) because it's constant)

    => Time complexity of the below function is O(n)
"""


def factorial(n):
    if n < 0:
        return -1

    if n == 0:
        return 1

    return n * factorial(n - 1)


print(factorial(3))
