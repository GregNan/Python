@log
def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', default = DEFAULT_PORT, type=int, nargs='?')
    parser.add_argument('-a', default='', nargs='?')
    namespace = parser.parse_args(sys.argv[1:])
    listen_address = namespace.a
    listen_port = namespace.p
    return listen_address, listen_port

class Server(metaclass=ServerMaker):
    port = Port()
    def __init__(self, listen_address, listen_port):
        self.addr = listen_address
        self.port = listen_port


