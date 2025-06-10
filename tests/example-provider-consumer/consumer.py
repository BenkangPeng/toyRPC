from src.client import Client

consumer = Client('localhost', 8080)
consumer.connect()

print(consumer.add(20,20))
print(consumer.sub(40,20))

consumer.disconnect()