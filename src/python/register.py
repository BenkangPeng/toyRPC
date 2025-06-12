from python.server import Server

def registerMethod(func):
    Server.instance().registerMethod(func)
    return func

def registerInstance(cls):
    Server.instance().registerInstance(cls())
    return cls