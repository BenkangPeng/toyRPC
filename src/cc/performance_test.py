import timeit
import random
# import matplotlib.pyplot as plt
# import numpy as np

# Performance of prime numbers generation

# Performance of getNPrimes()
pyPerf = []
ccPerf = []
for i in [10, 100, 1000, 10000]:
    pyPerf.append(1000 * timeit.timeit(
        f'pyGetNPrimes({i})', setup='from py_functions import pyGetNPrimes', number=1))
    ccPerf.append(
        1000 * timeit.timeit(f'getNPrimes({i})', setup='from functions import getNPrimes', number=1))

# unit: mileseconds
print(pyPerf)
print(ccPerf)


# Performance of getNFibonacci()
pyPerf2 = []
ccPerf2 = []
for i in [10, 100, 1000, 10000]:
    pyPerf2.append(1000 * timeit.timeit(
        f'pyGetNFibonacci({i})', setup='from py_functions import pyGetNFibonacci', number=1))
    ccPerf2.append(1000 * timeit.timeit(
        f'getNFibonacci({i})', setup='from functions import getNFibonacci', number=1))

print(pyPerf2)
print(ccPerf2)

# Performance of matrix multiplication
pyPerf3 = []
ccPerf3 = []
matrixSize = [64, 128, 256, 512]
for i in matrixSize:
    A = [[random.randint(0, 99) for _ in range(i)] for _ in range(i)]
    B = [[random.randint(0, 99) for _ in range(i)] for _ in range(i)]

    pyPerf3.append(1000 * timeit.timeit(
        f'M1.mul({A}, {B})', setup=f'from py_functions import matrix; M1 = matrix()', number=1))
    ccPerf3.append(1000 * timeit.timeit(
        f'M2.mul({A}, {B})', setup=f'from functions import PyMatrix; M2 = PyMatrix()', number=1))

print(pyPerf3)
print(ccPerf3)


# Create separate figures for each comparison
# plt.figure(figsize=(8, 5))
# n_values = [10, 100, 1000, 10000]
# x = np.arange(len(n_values))
# width = 0.35
# plt.bar(x - width/2, pyPerf, width, label='Python')
# plt.bar(x + width/2, ccPerf, width, label='C++')
# plt.xticks(x, n_values)
# plt.xlabel('N')
# plt.ylabel('Time (ms)')
# plt.title('Prime Numbers Generation Performance')
# plt.legend()
# plt.savefig('primes_performance.png')
# # plt.show()

# plt.figure(figsize=(8, 5))
# n_values = [10, 100, 1000, 10000]
# plt.bar(x - width/2, pyPerf2, width, label='Python')
# plt.bar(x + width/2, ccPerf2, width, label='C++')
# plt.xticks(x, n_values)
# plt.xlabel('N')
# plt.ylabel('Time (ms)')
# plt.title('Fibonacci Sequence Performance')
# plt.legend()
# plt.savefig('fibonacci_performance.png')
# # plt.show()

# plt.figure(figsize=(8, 5))
# x_mat = np.arange(len(matrixSize))
# plt.bar(x_mat - width/2, pyPerf3, width, label='Python')
# plt.bar(x_mat + width/2, ccPerf3, width, label='C++')
# plt.xticks(x_mat, matrixSize)
# plt.xlabel('Matrix Size (NxN)')
# plt.ylabel('Time (ms)')
# plt.title('Matrix Multiplication Performance')
# plt.legend()
# plt.savefig('matrix_performance.png')
# plt.show()