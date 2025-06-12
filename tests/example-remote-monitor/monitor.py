from python.client import Client

consumer = Client('localhost', 8080)
consumer.connect()

print(consumer.get_cpu_usage())
print(consumer.get_memory_usage())
print(consumer.get_disk_usage())

consumer.disconnect()