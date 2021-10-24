from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import * 
from PyQt5.QtWebEngineWidgets import *
import sys
from PyQt5.QtWidgets import *

class main_Window(QMainWindow):
    def __init__(self):
        super(main_Window, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser) 
        self.showMaximized() 

        #NavBar
        navBar=QToolBar()
        self.addToolBar(navBar)

        back_button=QAction('Back',self)
        back_button.triggered.connect(self.browser.back)
        navBar.addAction(back_button)

        forward_button=QAction('Foward',self)
        forward_button.triggered.connect(self.browser.forward)
        navBar.addAction(forward_button) 

        Reload_button=QAction('Reload',self)
        Reload_button.triggered.connect(self.browser.reload)
        navBar.addAction(Reload_button) 

        Home_button=QAction('Home',self)
        Home_button.triggered.connect(self.navigate_home)
        navBar.addAction(Home_button) 

        self.url_bar= QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navBar.addWidget(self.url_bar) 
        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com')) 

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url)) 

    def update_url(self, q):
        self.url_bar.setText(q.toString()) 

app= QApplication(sys.argv)
QApplication.setApplicationName('Search SS')
window= main_Window()
app.exec_() 