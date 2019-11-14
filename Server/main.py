from Server import *
from settings import *

if __name__ == '__main__':
    server = Server(ServerADDR, ServerPort)
    server.start()
