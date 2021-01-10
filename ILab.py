import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile

class App(QWebEngineView):
    def __init__(self):
        super().__init__()
        QWebEngineProfile.defaultProfile().setHttpAcceptLanguage('en')

        self.titleChanged.connect(lambda: self.setWindowTitle('ILab - '+self.title()))
        self.iconChanged.connect(lambda: self.setWindowIcon(self.icon()))

        self.load(QUrl('http://Your-IP:Your-port'))
        self.setWindowTitle('ILab')

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName('ILab')
    window = App()
    sys.exit(app.exec_())
