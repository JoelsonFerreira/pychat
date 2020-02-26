import socket, threading

class myThread (threading.Thread):
    def __init__(self, client):
        threading.Thread.__init__(self)
        self.csocket = client
        self.quit = False

    def run(self):
        while not self.quit:
            msg = self.csocket.recv(4096)
            print(msg.decode())

    def close(self):
        self.quit = True


def main():
    nick = input('Digite seu nome de usuario:       ')
    ip   = input('Digite o endereço ip do servidor: ')
    
    print('Lembre-se, antes de sair voce deve digitar "bye"')

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, 8080))
    
    rec = myThread(client)
    rec.start()

    data = ""
    
    while data != (nick + " -> " + "bye"):
        data = input()
        
        if data != 'bye':
            data = nick + " -> " + data

        client.send(bytes(data, 'UTF - 8'))
    
    rec.close()

    client.close()

main()