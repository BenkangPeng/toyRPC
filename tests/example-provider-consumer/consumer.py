from python.client import Client

consumer = Client('localhost', 8080)
consumer.connect()

print(consumer.add(20,20))
print(consumer.sub(40,20))
print(consumer.mul(20,20))
print(consumer.div(40,20))

# BUG : listAllMethods() is not working
# print(consumer.listAllMethods())

print(consumer.getPrimes(10))

print(consumer.getNPrimes(10))
print(consumer.getNFibonacci(10))

A = [[1,2],[3,4]]
B = [[5,6],[7,8]]
print(consumer.matMul(A,B))
consumer.disconnect()