import socket, threading

connected = []                                                              # lista com todos os sockets conectados

class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):

        threading.Thread.__init__(self)

        self.csocket = clientsocket
        self.clientAddress = clientAddress

        print ("New connection added: ", clientAddress)

    def run(self):
        print ("Connection from: ", self.clientAddress)
        msg = ''

        while True:
            # espera nova msg do cliente
            data = self.csocket.recv(2048)
            msg = data.decode()
            
            if msg=='bye':  # close connection
                connected.remove(self.csocket)
                break

            print ("from client", self.clientAddress, msg)

            # envia mensagem recebida para todos
            for i in connected:
                print('Sendding to', self.clientAddress)
                i.send(bytes(msg, 'UTF-8'))

        print ("Client at", self.clientAddress, "disconnected...")


def main():
    PORT = 8080

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("0.0.0.0", PORT))

    print("Server started")
    print("Waiting for client request..")

    while True:
        server.listen(1)
        clientsock, clientAddress = server.accept()
        connected.append(clientsock)
        newthread = ClientThread(clientAddress, clientsock)
        newthread.start()

main()
