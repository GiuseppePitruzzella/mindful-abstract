import sys
from flask_frozen import Freezer
from Server import *

server = Server()

if __name__ == "__main__":
    server.startServer()