import sys
from flask_frozen import Freezer
from Server import *

server = Server()
freezer = Freezer(server.getApp()) # Added

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        server.startServer()