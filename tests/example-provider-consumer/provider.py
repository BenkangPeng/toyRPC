from src.server import Server

def add(x,y):
    return x+y

provider = Server.instance()
provider.registerMethod(add)

provider.run()
