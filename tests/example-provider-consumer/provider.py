from src.server import Server
import src.registerFactory

provider = Server.instance()

provider.run()
