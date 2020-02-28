from chatWindow import ChatWindow

import sys
from PySide2 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    chat = ChatWindow()

    sys.exit(app.exec_())
