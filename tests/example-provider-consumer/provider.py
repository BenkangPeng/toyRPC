from src.server import Server
from src.register import registerMethod, registerInstance


@registerInstance
class Calculator:
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y
    
    def mul(self, x, y):
        return x * y
    
    def div(self, x, y):
        assert y != 0, "Division by zero"
        return x / y


provider = Server.instance()

provider.run()
