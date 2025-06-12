from libcpp.vector cimport vector

cdef extern from "functions.cc":
    
    cdef vector[int] prim(int n)
    cdef vector[int] fib(int n)

