import sys
from PySide2 import QtCore, QtWidgets, QtGui
import socket, msgRec

class LoginWindow(QtWidgets.QWidget):
    def __init__(self, chat):
        QtWidgets.QWidget.__init__(self)

        self.chat = chat

        self.connect_button = QtWidgets.QPushButton("connect")
        self.user_name      = QtWidgets.QLineEdit()
        self.ip_addr        = QtWidgets.QLineEdit()

        self.ip_addr.setText("181.223.113.85")

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.user_name)
        self.layout.addWidget(self.ip_addr)
        self.layout.addWidget(self.connect_button)

        self.setLayout(self.layout)

        self.connect_button.clicked.connect(self.connect)


    def connect(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.ip_addr.text(), 8080))
        
        self.nick = self.user_name.text()
        
        self.rec = msgRec.MsgRec(self.client, self.chat.msg_list)
        self.rec.start()

        self.close()
        self.chat.show()
