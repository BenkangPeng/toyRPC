from src.server import Server

s1 = Server.instance()
s2 = Server.instance()
print(s1 is s2)

s3 = Server('1.0.0.0',22)
print(s3 is s1)