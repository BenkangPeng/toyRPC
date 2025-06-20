import json
import socket
import inspect
from threading import Thread, Lock


class Server:

    # the singleton instance
    _instance = None
    _lock = Lock()

    def __init__(self, host: str = '0.0.0.0', port: int = 8080):
        self.host = host
        self.port = port
        self.SIZE = 1024
        self.address = (host, port)
        self.methods = {}

    # TODO @BenkangPeng Use decorator instead to register Method.
    def registerMethod(self, function) -> None:
        try:
            self.methods.update({function.__name__: function})
        except:
            raise Exception(
                'A non function object has been passed into Server.registerMethod(self, function)')

    # TODO @BenkangPeng Use decroate instead to register Instance.
    def registerInstance(self, instance=None) -> None:
        try:
            # Regestring the instance's methods
            for functionName, function in inspect.getmembers(instance, predicate=inspect.ismethod):
                # except for the non-special functions
                if not functionName.startswith('__'):
                    self.methods.update({functionName: function})
        except:
            raise Exception(
                'A non class object has been passed into RPCServer.registerInstance(self, instance)')

    def __handle__(self, client: socket.socket, address: tuple) -> None:
        print(f'🔗 Managing requests from {address}.')
        while True:
            try:
                functionName, args, kwargs = json.loads(
                    client.recv(self.SIZE).decode())
            except:
                print(f'❌ Client {address} disconnected.')
                break

            # Showing request Type
            print(f'➡️  {address} : {functionName}({args})')

            try:
                response = self.methods[functionName](*args, **kwargs)
            except Exception as e:
                # Send back exeption if function called by client is not registred
                client.sendall(json.dumps(str(e)).encode())
            else:
                client.sendall(json.dumps(response).encode())

        print(f'🎉 Completed requests from {address}.')
        client.close()

    def run(self) -> None:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind(self.address)
            sock.settimeout(0.2)
            sock.listen()

            print(f'🔍 Server {self.address} running')
            while True:
                try:
                    try:
                        client, address = sock.accept()
                    except socket.timeout:
                        continue

                    Thread(target=self.__handle__, args=[
                           client, address]).start()

                # BUG @BenkangPeng can't interrupt the process in fact.
                except KeyboardInterrupt:
                    print(f'❌ Server {self.address} interrupted')
                    break

    @classmethod
    def instance(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls()
        return cls._instance

    def getMethods(self):
        return self.methods
