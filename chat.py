import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QAction, QApplication, QMainWindow, QMenu, QMessageBox, QWidget
                             , QTextBrowser, QPushButton, QLineEdit, QHBoxLayout
                             ,QVBoxLayout)

class Chat(QMainWindow):
    def __init__(self):
        super(Chat, self).__init__()
        self.setWindowTitle('chat')

        self.talkArea = QWidget()

        self.outputArea = QTextBrowser()
        self.pushButton = QPushButton("push")
        self.inputtext = QLineEdit()
        self.hbox = QHBoxLayout()

        self.hbox.addWidget(self.inputtext)
        self.hbox.addWidget(self.pushButton)
        
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.outputArea)
        self.layout().addLayout(self.hbox)

        self.pushButton.clicked.connect(self.push)
        
        self.setCentralWidget(self.talkArea)

        self.createActions()

    def about(self):
        #QMessageBox.about("this is my work")
        self.bar.showMessage('about')

    def logout(self):
        pass

    def set_thing(self):
        pass
        
    def createActions(self):
        aboutAct = QAction("&about", self)
        aboutAct.triggered.connect(self.about)


        setAct = QAction("&set", self)
        setAct.triggered.connect(self.set_thing)


        logoutAct = QAction("&logout", self)
        logoutAct.triggered.connect(self.logout)

        self.bar = self.statusBar()
        self.bar.showMessage('hello')


        self.aboutmenu = self.menuBar()
        self.aboutmenu.addMenu('&about').addAction(aboutAct)
        self.aboutmenu.addMenu('&set').addAction(setAct)
        self.aboutmenu.addMenu('&logout').addAction(logoutAct)
        
        # this is ubuntu special thing, so you should input this to stop origin ubuntu menubar
        self.aboutmenu.setNativeMenuBar(False)

    def push(self):
        self.outputArea.append(self.inputtext.text())
        Chat().statusBar().showMessage(self.inputtext.text())
        self.inputtext.clear()
        

if __name__ == '__main__':

    app = QApplication(sys.argv)
    chat1 = Chat()
    chat1.show()
    sys.exit(app.exec_())
