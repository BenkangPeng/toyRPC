import functions

print(functions.getNPrimes(20))
print(functions.getNFibonacci(20))

A = [[1,2],[3,4]]
B = [[5,6],[7,8]]
print(functions.matMul(A,B))

M = functions.PyMatrix()
print(M.mul(A,B))
print(M.transpose(A))