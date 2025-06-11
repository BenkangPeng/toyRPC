# This file is used to register methods and instances.
# All the Server instance should import this module.
# e.g.
# import registerFactory
# _server = Server.instance()
# _server.run()

import psutil
from src.register import registerMethod, registerInstance
from src.server import Server


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


@registerInstance
class systemMonitor:
    def get_cpu_usage(self) -> str:
        return str(psutil.cpu_percent(interval=1)) + '%'

    def get_memory_usage(self) -> str:
        return str(psutil.virtual_memory().percent) + '%'

    def get_disk_usage(self, path: str = '/') -> str:
        disk = psutil.disk_usage(path)
        return str(disk.percent) + '%'


@registerMethod
def listAllMethods():
    res = []
    for name, func in Server.instance().getMethods().items():
        res.append(f'{name} : {func}')

    return res
