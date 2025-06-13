from libcpp.vector cimport vector

cdef extern from "functions.cc":
    
    cdef vector[int] prim(int n)
    cdef vector[int] fib(int n)
    cdef vector[vector[int]] matmul(vector[vector[int]] A, vector[vector[int]] B)

    cdef cppclass matrix:
        matrix()
        vector[vector[int]] mul(vector[vector[int]] A, vector[vector[int]] B)
        vector[vector[int]] transpose(vector[vector[int]] A)
