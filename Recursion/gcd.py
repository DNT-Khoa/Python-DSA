"""
How to find the GCD (Greatest Common Divisor) of two numbers using recursion ?
Solution: We can use the Euclidean algorithm for finding GCD(A, B) as follow:
    If A = 0 then GCD(A,B)=B, since the GCD(0,B)=B, and we can stop.
    If B = 0 then GCD(A,B)=A, since the GCD(A,0)=A, and we can stop.
    Write A in quotient remainder form (A = B⋅Q + R)
    Find GCD(B,R) using the Euclidean Algorithm since GCD(A,B) = GCD(B,R)
"""


def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


print(gcd(-8, 4))
