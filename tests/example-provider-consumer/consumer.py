from src.client import Client

consumer = Client('localhost', 8080)
consumer.connect()

print(consumer.add(2,2))

consumer.disconnect()