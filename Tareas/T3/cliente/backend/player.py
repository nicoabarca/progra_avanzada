import socket
import threading
import json

from utils import get_json_data

class Player:

    def __init__(self, user_name, birth_date):
        self.user_name = user_name
        self.birth_date = birth_date
        self.server_host = get_json_data("server_host") 
        self.server_port = get_json_data("server_port") 
        self.socket_player = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_last_response = ""

        try:
            self.connect_to_server()
            self.listen()
        except ConnectionError:
            print("Connection Fail")
            self.socket_player.close()
            exit()

    #Connect client to server
    def connect_to_server(self):
        self.socket_player.connect((self.server_host, self.server_port))
        print("Connected to Server")

    #Creates and start thread to listen to server messages
    def listen(self):
        thread = threading.Thread(target=self.listen_thread, daemon=True)
        thread.start()

    #Thread to listen server messages, also decrypt the message 
    def listen_thread(self):
        while True:
            response_bytes_length = self.socket_player.recv(4)
            response_length = int.from_bytes(
                    response_bytes_length, byteorder='little')
            response = bytearray()

            while len(response) < response_length:
                read_length = 4096
                response.extend(self.socket_player.recv(read_length))

            received = self.decode_custom_msg(response, response_length)
            print("MENSAJE RECIBIDO", received)

            try:
                decrypted_received = self.decrypt_msg(received)
                response_dict = json.loads(decrypted_received)
                self.server_last_response = response_dict
            except json.JSONDecodeError or IndexError as err:
                print("ERROR: The message could not be encoded")
                print(err)

    #Send message to server, receives a dictionary and send encrypted bytes
    def send(self, msg): 
        stringified_msg = json.dumps(msg)
        msg_length_bytes = len(stringified_msg.encode("UTF-8")).to_bytes(4, byteorder='little')
        encrypted_msg_bytes = self.encrypt_msg(stringified_msg)
        encoded_msg_bytes = self.encode_custom_msg(encrypted_msg_bytes)

        self.socket_player.sendall(msg_length_bytes + encoded_msg_bytes)

    #Send data to the server to autheticate the user
    def send_login_verification_to_server(self, user_name, birth_date):
        dict_data_str = {
            'target_function': "verify_user", 
            'data': {
                'user_name' : user_name,
                'birth_date' : birth_date
            }
        }
        self.send(dict_data_str)

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
    def encrypt_msg(self, msg_data): 
        msg_bytes = msg_data.encode("UTF-8")
        bytes_list = [msg_bytes[i:i+1] for i in range(len(msg_bytes))]
        a = bytes_list[0:len(bytes_list):3]
        b = bytes_list[1:len(bytes_list):3]
        c = bytes_list[2:len(bytes_list):3]
        
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
    #Recives bytes, returns a string
    def decrypt_msg(self, msg_data): 
        bytes_list = [msg_data[i:i+1] for i in range(len(msg_data))][:-1]
        a_length, b_length, c_length = self.get_bytes_length(len(bytes_list))
        a, b, c =  [], [], []

        if bytearray(msg_data)[-1] == 0:
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