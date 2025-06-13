# distutils: language=c++

from libcpp.vector cimport vector
from functions cimport prim, fib, matmul, matrix


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

def matMul(vector[vector[int]] A, vector[vector[int]] B):
    """
    Multiply two matrices.

    Parameters:
    A (vector[vector[int]]): The first matrix.
    B (vector[vector[int]]): The second matrix.

    Returns:
    vector[vector[int]]: The result of the matrix multiplication.
    """
    cdef vector[vector[int]] res = matmul(A, B)
    return res

cdef class PyMatrix:
    cdef matrix _matrix

    def __init__(self):
        self._matrix = matrix()

    def mul(self, vector[vector[int]] A, vector[vector[int]] B):
        return self._matrix.mul(A, B)
    
    def transpose(self, vector[vector[int]] A):
        return self._matrix.transpose(A)