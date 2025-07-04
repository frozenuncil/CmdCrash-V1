import sys
import os
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QTimer, QUrl  

class IntroWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Intro")
        self.resize(800, 600)
        self.setStyleSheet("background-color: black;")

        self.center_on_screen() 

        webview = QWebEngineView(self)
        html_path = os.path.abspath("index.html")
        webview.load(QUrl.fromLocalFile(html_path))
        self.setCentralWidget(webview)

        QTimer.singleShot(11000, self.start_main)

    def center_on_screen(self):
        frame_geo = self.frameGeometry()
        screen = QApplication.primaryScreen().availableGeometry().center()
        frame_geo.moveCenter(screen)
        self.move(frame_geo.topLeft())

    def start_main(self):
        self.close()
        main_path = os.path.abspath(os.path.join("main.py"))
        subprocess.Popen(["python", main_path])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IntroWindow()
    window.show()
    sys.exit(app.exec_())
