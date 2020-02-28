import threading
from PySide2 import QtWidgets

class MsgRec (threading.Thread):
    def __init__(self, client, msg_list):
        threading.Thread.__init__(self)
        self.csocket   = client
        self.quit      = False
        self.msg_list  = msg_list

    def run(self):
        while not self.quit:
            try:
                msg = self.csocket.recv(4096)
            except:
                self.close()
            QtWidgets.QListWidgetItem(msg.decode(), self.msg_list)
            
    def close(self):
        self.quit = True
