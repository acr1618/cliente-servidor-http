#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys

from threading import Thread


class Server():
    def __init__(self, url, ip, buffer_size, port):
        self.URL = url
        self.IP = ip
        self.BUFFER_SIZE = buffer_size
        self.PORT = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket de conexão tcp


    def connect(self):
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #recurso que resolve o problema de reutilização de porta
        self.sock.bind((self.IP, self.PORT))

        print('Servidor ouvindo (...)')
        while True:
            self.sock.listen(1)

            (con, (ip, port)) = self.sock.accept()  # Estabelece conexao com o cliente

            print('Conexao estabelecida com ', (ip, port))
            con.settimeout(60) #timeout depois de 60s
            Thread(target=self.run,args=(con,ip,port)).start()

    def run(self,con,ip,port):
        HTTP_MSG_RCV = con.recv(self.BUFFER_SIZE)
        HTTP_MSG_RCV = HTTP_MSG_RCV.decode('utf-8')

        HTTP_MSG_RCV = HTTP_MSG_RCV.split('\n')


        URL = HTTP_MSG_RCV[0].split(' ')[1]
        #print(URL)
        HOST = HTTP_MSG_RCV[1].split('Host: ', 1)[1]


        URL, HOST = URL.strip(), HOST.strip()
        print('\nMensagem recebida pelo cliente {0}:\n{1}\n'.format(self.IP, HTTP_MSG_RCV))

        FILE_PATH = self.URL + '/' + URL

        print(FILE_PATH)


        try:
            f = open(FILE_PATH, 'rb')
            l = f.read(self.BUFFER_SIZE)

            con.sendall('HTTP/1.1 200 OK\n\n'.encode('utf-8'))

            while l:
                con.sendall(l)
                l = f.read(self.BUFFER_SIZE)
                if not l:
                    f.close()
                    print('* Arquivo enviado *\n* Conexão fechada *\n')
                    break
            self.stop(con)
        except:
            print('Arquivo solicitado não encontrado. Enviando mensagem de erro ao cliente.\n')

            con.sendall('HTTP/1.1 404 Not Found\n'.encode('utf-8'))
            self.stop(con)
    def stop(self,con):
        con.close()

def main(argv):
    SERVER_URL = argv[1]
    SERVER_IP = "127.0.0.1"
    BUFFER_SIZE = 1024

    if len(argv) == 3:
        SERVER_PORT = int(argv[2]) # se user passar a porta use-a, se não use a 80.
    else:
        SERVER_PORT = 80

    server = Server(SERVER_URL, SERVER_IP, BUFFER_SIZE, SERVER_PORT)
    server.connect()


if __name__ == '__main__':
    main(sys.argv)
