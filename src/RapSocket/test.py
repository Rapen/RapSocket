from RapSocket import RapSocket

socket = RapSocket()


def callback(message):
    print(message)


socket.create()
socket.listen(callback)
