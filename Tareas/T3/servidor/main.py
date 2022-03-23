from server import Server
from utils import get_json_data

if __name__ == "__main__":
    host = get_json_data("server_host")
    port = get_json_data("server_port")
    server = Server(host, port)