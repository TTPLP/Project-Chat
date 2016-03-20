import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QAction, QApplication, QMainWindow, QMenu, QMessageBox, QWidget
                             , QTextBrowser, QPushButton, QLineEdit, QHBoxLayout
                             ,QVBoxLayout, QLabel)

class Chat(QMainWindow):
    def __init__(self):
        super(Chat, self).__init__()
        self.setWindowTitle('chat')

        self.createActions()
        self.createQWidget()
        self.createAboutQWidget()

    def about(self):
        self.bar.showMessage('about')
        self.aboutArea.show()

    def logout(self):
        self.outputArea.clear()
        self.loginArea.show()
        self.hide()

    def set_thing(self):
        self.bar.showMessage('set')
        
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

    def createQWidget(self):
        self.talkArea = QWidget()
        self.setCentralWidget(self.talkArea)   #let QWidget in QMainWindwos

        #qtextbrowser and qpushbutton and qlineedit of self is self.talkArea
        self.outputArea = QTextBrowser(self.talkArea)
        self.pushButton = QPushButton("push", self.talkArea)
        self.inputtext = QLineEdit(self.talkArea)
        self.hbox = QHBoxLayout()

        self.hbox.addWidget(self.inputtext)
        self.hbox.addWidget(self.pushButton)

        #because qwidget only have setlayout, so use self.talkArea to set
        self.talkArea.setLayout(QVBoxLayout())
        self.talkArea.layout().addWidget(self.outputArea)
        self.talkArea.layout().addLayout(self.hbox)

        self.pushButton.clicked.connect(self.push)

        
        self.talkArea.show()

    def push(self):
        self.outputArea.append(self.inputtext.text())
        self.bar.showMessage(self.inputtext.text())
        self.inputtext.clear()

    def loginQWidget(self):
        self.loginArea = QWidget()
        self.loginArea.setWindowTitle('login')

        self.label = QLabel('輸入ip:', self.loginArea)
        self.ip_input = QLineEdit(self.loginArea)
        self.login_button = QPushButton('login', self.loginArea)

        self.loginArea.setLayout(QVBoxLayout())
        self.loginArea.layout().addWidget(self.label)
        self.loginArea.layout().addWidget(self.ip_input)
        self.loginArea.layout().addWidget(self.login_button)

        self.login_button.clicked.connect(self.login)

        self.loginArea.show()

    def login(self):
        self.show()
        self.ip_input.clear()
        self.loginArea.hide()

    def createAboutQWidget(self):
        self.aboutArea = QWidget()
        self.aboutArea.setWindowTitle('about')

        self.about_label = QLabel('這是我在工程獅計劃中的作品之一', self.aboutArea)

        self.aboutArea.setLayout(QVBoxLayout())
        self.aboutArea.layout().addWidget(self.about_label)
        

if __name__ == '__main__':

    app = QApplication(sys.argv)
    chat1 = Chat()
    chat1.loginQWidget()
    sys.exit(app.exec_())
