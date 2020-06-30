import socket


class RapSocket:
    def __init__(self):
        self.url = ''
        self.mySocket = None

    def create(self, port=1234, nbr_incoming_connection=1):
        self.mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mySocket.bind((socket.gethostname(), port))
        self.mySocket.listen(nbr_incoming_connection)

    def connect(self, url, port):
        self.mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mySocket.connect((socket.gethostname(), port))

    def disconnect(self):
        pass

    def message(self):
        pass

    def listen(self, __callback=None):
        while True:
            client_socket, address = self.mySocket.accept()
            __callback(f"Connection from {address} has been established")

    def __del__(self):
        self.disconnect()
