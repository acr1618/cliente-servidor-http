#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys
import os

class Cliente():
    def __init__(self, ip, port, host, buffer_size):
        self.IP = ip
        self.PORT = port
        self.BUFFER_SIZE = buffer_size
        self.HOST = host
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.sock.connect((self.IP, self.PORT))

    def request(self, URL):
        HTTP_MSG_SEND = 'GET {0} HTTP/1.1\nHost: {1}'.format(URL, self.HOST)
        print(HTTP_MSG_SEND)
        self.sock.sendall(HTTP_MSG_SEND.encode('utf-8'))

        CODE_HTTP = self.sock.recv(self.BUFFER_SIZE)
        CODE_HTTP = CODE_HTTP.decode('utf-8')
        CODE_FRA = CODE_HTTP.split()

        if int(CODE_FRA[1]) == 200:
            print('\nResposta do servidor: {0} OK\n'.format(CODE_FRA[1]))


            FILE_PATH = URL.split("/")[-1]


            with open(FILE_PATH, 'wb') as f:
                while True:
                    data = self.sock.recv(self.BUFFER_SIZE)
                    if not data:
                        break
                    f.write(data)
                f.close()
                print('\nURL solicitada obtida com sucesso.')
        else:
            print('\nResposta do servidor:{0}\n'.format(CODE_HTTP))
            self.sock.close()

    def stop(self):
        self.sock.close()
        print('Conexão fechada.\n')

def main(argv):
    URL = argv[1]
    URL = URL.split('/', 1)
    HOST = URL[0]
    URL = URL[1]

    TCP_IP = "127.0.0.1"
    BUFFER_SIZE = 1024

    if len(argv) == 3:
        TCP_PORT = int(argv[2])
    else:
        TCP_PORT = 80

    cliente = Cliente(TCP_IP, TCP_PORT, HOST, BUFFER_SIZE)
    cliente.connect()
    cliente.request(URL)
    cliente.stop()
if __name__ == '__main__':
    main(sys.argv)
