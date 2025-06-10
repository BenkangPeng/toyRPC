import json
import socket
import inspect
from threading import Thread


class Server:
    def __init__(self, host: str = '0.0.0.0', port: int = 8080):
        self.host = host
        self.port = port
        self.SIZE = 1024
        self.address = (host, port)
        self.method = {}

    def registerMethod(self, function) -> None:
        try:
            self.methods.update({function.__name__: function})
        except:
            raise Exception(
                'A non function object has been passed into RPCServer.registerMethod(self, function)')

    def registerInstance(self, instance=None) -> None:
        try:
            # Regestring the instance's methods
            for functionName, function in inspect.getmembers(instance, predicate=inspect.ismethod):
                if not functionName.startswith('__'):
                    self.methods.update({functionName: function})
        except:
            raise Exception(
                'A non class object has been passed into RPCServer.registerInstance(self, instance)')

    def __handle__(self, client: socket.socket, address: tuple) -> None:
        print(f'Managing requests from {address}.')
        while True:
            try:
                functionName, args, kwargs = json.loads(
                    client.recv(self.SIZE).decode())
            except:
                print(f'! Client {address} disconnected.')
                break

            # Showing request Type
            print(f'> {address} : {functionName}({args})')

            try:
                response = self.methods[functionName](*args, **kwargs)
            except Exception as e:
                # Send back exeption if function called by client is not registred
                client.sendall(json.dumps(str(e)).encode())
            else:
                client.sendall(json.dumps(response).encode())

        print(f'Completed requests from {address}.')
        client.close()

    def run(self) -> None:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind(self.address)
            sock.listen()

            print(f'+ Server {self.address} running')
            while True:
                try:
                    client, address = sock.accept()
                    Thread(target=self.__handle__, args=[
                           client, address]).start()

                except KeyboardInterrupt:
                    print(f'- Server {self.address} interrupted')
                    break

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
