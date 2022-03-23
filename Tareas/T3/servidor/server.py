import socket
import json
import threading
from game_logic import GameLogic

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected_players = {}
        self.game_logic = GameLogic()

        self.bind_and_listen()
        self.accept_connections()

    #Bind the socket to a host and port and listen to messages from clients
    def bind_and_listen(self):
        self.socket_server.bind((self.host, self.port))
        self.socket_server.listen()
        print(f"Servidor escuchando en {self.host}:{self.port}...")

    #Creates a thread for every accepted client
    def accept_connections(self):
        thread = threading.Thread(target=self.accept_connections_thread)
        thread.start()

    #Thread for accepted clients
    def accept_connections_thread(self):
        while True:
            client_socket, _ = self.socket_server.accept()
            listening_client_thread = threading.Thread(
                target=self.listen_client_thread,
                args=(client_socket, ),
                daemon=True)
            listening_client_thread.start()
    
    #Listen and decrypt messages coming from a client and send a response
    def listen_client_thread(self, client_socket):
        print(f"Server connected to client ...")

        while True:
            response_bytes_length = client_socket.recv(4)
            response_length = int.from_bytes(
                response_bytes_length, byteorder='little')
            response = bytearray()

            while len(response) < response_length:
                read_length = 4096
                response.extend(client_socket.recv(read_length))

            received = self.decode_custom_msg(response, response_length)
        
            if received != "":
                try:
                    decrypted_received = self.decrypt_msg(received)
                    received_dict = json.loads(decrypted_received)
                    response_to_client = self.handle_command(received_dict, client_socket)
                    self.send(response_to_client, client_socket)
                except json.JSONDecodeError or IndexError as err:
                    print("ERROR: The message could not be encoded")

    #Recives a dictionary and send encoded message to client
    def send(self, value, sock): 
        stringified_value = json.dumps(value)
        msg_length_bytes = len(stringified_value.encode("UTF-8")).to_bytes(4, byteorder='little')
        encrypted_msg_bytes = self.encrypt_msg(stringified_value)
        encoded_msg_bytes = self.encode_custom_msg(encrypted_msg_bytes)

        sock.send(msg_length_bytes + encoded_msg_bytes)

    #Calls a function from game_logic to handle the client response
    #Recives a dictionary, returns dictionary
    def handle_command(self, received_dict, client_socket):
        function_to_call = getattr(self.game_logic, received_dict["target_function"])
        response_to_client = function_to_call(**received_dict["data"])
        return response_to_client

    #Separate the message in blocks, add block numbers and add 0s
    #if the last block is less than 80 bytes long
    #Recives bytes and returns bytes
    def encode_custom_msg(self, msg_bytes):
        msg_ba = bytearray(msg_bytes)

        while len(msg_ba) % 80 != 0:
            msg_ba.extend(b"\x00")

        msg_blocks = []

        for i in range(0, len(msg_ba), 80):
            msg_blocks.append(msg_ba[i: i + 80])

        encoded_msg = bytearray()

        for (index, chunk) in enumerate(msg_blocks):
            block_number = index.to_bytes(4, byteorder='big')
            encoded_msg.extend(block_number)
            encoded_msg.extend(bytes(chunk))

        return bytes(encoded_msg)

    #Decode the message, eliminates block numbers and 0s at the end
    #Recives bytes and int, returns bytes
    def decode_custom_msg(self, response_msg_bytes, msg_length):
        response_msg_bytes_list = [bytes(response_msg_bytes[i:i+1])
                        for i in range(len(response_msg_bytes))]
        msg_bytes_length = len(response_msg_bytes_list)
        msg_bytes_list = []

        for i in range(0, msg_bytes_length, 84):
            block_data = response_msg_bytes_list[i + 4:i + 84]
            msg_bytes_list.extend(block_data)

        msg_bytes = bytearray(b"".join(msg_bytes_list[:msg_length + 1]))

        return bytes(msg_bytes)

    #Encrypt the message
    #Recives a JSON string, returns bytes
    def encrypt_msg(self, msg_data): #Recives a JSON string
        msg_bytes = msg_data.encode("UTF-8")
        bytes_list = [msg_bytes[i:i+1] for i in range(len(msg_bytes))]
        a, b, c =  [], [], []

        for i in range(len(bytes_list)): 
            if i % 3 == 0:
                try:
                    a.append(bytes_list[i]) 
                    b.append(bytes_list[i + 1])  
                    c.append(bytes_list[i + 2])
                except IndexError:
                    pass
        
        if b[0] > c[0]:
            abcn = [*a, *b, *c, b"\x00"]
            changed_bytes_list = []
            for byte in abcn:
                if byte == b"\x03":
                    changed_bytes_list.append(b"\x05")
                elif byte == b"\x05":
                    changed_bytes_list.append(b"\x03")
                else:
                    changed_bytes_list.append(byte)
            encrypted_msg = bytearray(b"".join(changed_bytes_list))    
        else:
            bacn = [*b, *a, *c, b"\x01"]
            encrypted_msg = bytearray(b"".join(bacn))

        return bytes(encrypted_msg)

    #Decrypt the message
    #Recives bytes, returns string
    def decrypt_msg(self, msg_data):
        bytes_list = [msg_data[i:i+1] for i in range(len(msg_data))][:-1]
        a_length, b_length, c_length = self.get_bytes_length(len(bytes_list))
        a, b, c =  [], [], []

        if (bytearray(msg_data))[-1] == 0:
            changed_bytes_list = []
            for byte in bytes_list:
                if byte == b"\x03":
                    changed_bytes_list.append(b"\x05")
                elif byte == b"\x05":
                    changed_bytes_list.append(b"\x03")
                else:
                    changed_bytes_list.append(byte)
            a = changed_bytes_list[:a_length]
            b = changed_bytes_list[a_length:a_length + b_length]
            c = changed_bytes_list[a_length + b_length:]
        else:
            b = bytes_list[:b_length]
            a = bytes_list[b_length:b_length + a_length]
            c = bytes_list[b_length + a_length:]

        msg_bytes_list = []
        for i in range(len(a)):
            try:
                msg_bytes_list.append(a[i])
                msg_bytes_list.append(b[i])
                msg_bytes_list.append(c[i])
            except IndexError:
                pass
        decrypted_message = bytes(bytearray(b"".join(msg_bytes_list)))
        return decrypted_message.decode("UTF-8")

    #Recives int, returns the length of the parts of the encrypted message
    def get_bytes_length(self, msg_length):
        a, b, c = 0, 0, 0
        remainder = msg_length // 3
        if msg_length % 3 == 0:
            a, b, c = remainder, remainder, remainder
        elif msg_length % 3 == 1:
            a, b, c = remainder + 1, remainder, remainder 
        else:
            a, b, c = remainder, remainder, remainder - 1
        return (a, b, c)