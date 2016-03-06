from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class TalkArea(QWidget):
    def __init__(self, parent = None ):
        super(TalkArea, self).__init__(parent)
        
        self.outputArea = QTextBrowser(self)
        self.pushButton = QPushButton("push", self)
        self.inputtext = QLineEdit(self)
        self.hbox = QHBoxLayout()

        self.hbox.addWidget(self.inputtext)
        self.hbox.addWidget(self.pushButton)
        
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.outputArea)
        self.layout().addLayout(self.hbox)

        self.pushButton.clicked.connect(self.push)

    def push(self):
        self.outputArea.append(self.inputtext.text())
        

class Chat(QMainWindow):
    def __init__(self):
        super(Chat, self).__init__()
        self.setWindowTitle('chat')

        self.talkArea = TalkArea()
        self.setCentralWidget(self.talkArea)

        self.createActions()

    def about(self):
        QMessageBox.about(self, "this is my work")

    def logout(self):
        pass

    def set_thing(self):
        pass
        
    def createActions(self):
        aboutAct = QAction("about", self)
        aboutAct.triggered.connect(self.about)


        setAct = QAction("set", self)
        setAct.triggered.connect(self.set_thing)


        logoutAct = QAction("logout", self)
        logoutAct.triggered.connect(self.logout)


        self.menuBar().addMenu('about').addAction(aboutAct)
        self.menuBar().addMenu('set').addAction(setAct)
        self.menuBar().addMenu('logout').addAction(logoutAct)
        
        

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    chat = Chat()
    chat.show()
    sys.exit(app.exec_())
