from python.client import Client

consumer = Client('localhost', 8080)
consumer.connect()

print(consumer.add(20,20))
print(consumer.sub(40,20))
print(consumer.mul(20,20))
print(consumer.div(40,20))

print(consumer.listAllMethods())

print(consumer.getPrimes(10))

consumer.disconnect()