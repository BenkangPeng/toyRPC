# distutils: language=c++

from libcpp.vector cimport vector
from functions cimport prim
from functions cimport fib


def getNPrimes(int n):
    """
    Get the first n prime numbers.

    Parameters:
    n (int): The number of prime numbers to retrieve.

    Returns:
    list: A list containing the first n prime numbers.
    """
   
    cdef vector[int] primes = prim(n)
    return primes

def getNFibonacci(int n):
    """
    Get the first n Fibonacci numbers.
    """

    cdef vector[int] res = fib(n)
    return res