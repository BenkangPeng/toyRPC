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

print(consumer.getNPrimes(30))
print(consumer.getNFibonacci(30))
consumer.disconnect()