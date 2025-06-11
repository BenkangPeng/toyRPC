from src.server import Server
import src.registerFactory

_server = Server.instance()
_server.run()