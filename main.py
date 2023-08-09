from Server import *

if __name__ == '__main__':
    from elsa import cli
    Server = Server()
    # cli(Server.getApp(), base_url='https://example.com')
    cli(Server, base_url='https://giuseppepitruzzella.github.io/mindful-abstract/')