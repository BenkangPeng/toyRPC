# This file is used to test the performance improvement of the C++ code.

import math

def pyGetNPrimes(n):
    if n <= 0:
        return []
    if n == 1:
        return [2]

    # Calculate the upper bound for the n-th prime
    upper = int(n * (math.log(n) + math.log(math.log(n)))) + 10

    # Sieve of Eratosthenes implementation
    sieve = [True] * (upper + 1)
    sieve[0] = sieve[1] = False

    for p in range(2, int(math.sqrt(upper)) + 1):
        if sieve[p]:
            for i in range(p*p, upper+1, p):
                sieve[i] = False

    # Collect primes
    primes = []
    for i in range(2, upper + 1):
        if sieve[i]:
            primes.append(i)
            if len(primes) == n:
                break

    return primes


def pyGetNFibonacci(n):
    if n <= 0:
        return []

    if n == 1:
        return [1]

    if n == 2:
        return [1, 1]

    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])

    return fib


class matrix:
    def mul(self, A, B):
        if len(A[0]) != len(B):
            raise Exception("Matrices cannot be multiplied")

        C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
        for i in range(0, len(A)):
            for j in range(0, len(B[0])):
                for k in range(0, len(B)):
                    C[i][j] += A[i][k] * B[k][j]
        return C

    def transpose(self, A):
        C = [[0 for _ in range(len(A))] for _ in range(len(A[0]))]
        for i in range(0, len(A)):
            for j in range(0, len(A[0])):
                C[j][i] = A[i][j]
        return C
