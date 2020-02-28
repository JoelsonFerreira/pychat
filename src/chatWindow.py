import sys
from PySide2 import QtCore, QtWidgets, QtGui
from loginWindow import LoginWindow

class ChatWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        # aux windows
        self.login = LoginWindow(self)
        self.login.show()

        # widgets
        self.msg_list         = QtWidgets.QListWidget()
        self.msg_to_send      = QtWidgets.QLineEdit()
        self.send_button      = QtWidgets.QPushButton("send")


        # layout 
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.msg_list)
        self.layout.addWidget(self.msg_to_send)
        self.layout.addWidget(self.send_button)
        
        self.setLayout(self.layout)

        #signals and slots
        self.send_button.connect(self.send_button, QtCore.SIGNAL('clicked()'), self.send)
        
    def send(self):
        self.login.client.send(bytes(self.login.user_name.text() + ": " + self.msg_to_send.text(), 'UTF - 8'))
        self.msg_to_send.setText("")

    def closeEvent(self, event):
        self.login.client.send(bytes("bye", 'UTF - 8'))
        self.login.rec.close()
        self.login.client.close()
        self.close()

