import psutil
from src.server import Server
from src.register import registerInstance

@registerInstance
class systemMonitor:
    def get_cpu_usage(self) -> str:
        return str(psutil.cpu_percent(interval=1)) + '%'
    
    def get_memory_usage(self) -> str:
        return str(psutil.virtual_memory().percent)  + '%'
    
    def get_disk_usage(self,path: str = '/') -> str:
        disk = psutil.disk_usage(path)
        return str(disk.percent) + '%'
    
_server = Server.instance()
_server.run()