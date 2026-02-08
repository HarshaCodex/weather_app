from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import sys
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Weather App')
        self.setGeometry(400, 400, 800, 1200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.search_button = QPushButton('Search')
        self.search_button.setFixedHeight(40)
        self.search_button.setFixedWidth(100)

        self.search_button.clicked.connect(self.hello)

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText('Enter Location')
        self.search_bar.setFixedHeight(30)
        self.search_bar.setFixedWidth(200)

        self.search_row = QHBoxLayout()
        self.search_row.addWidget(self.search_bar)
        self.search_row.addWidget(self.search_button)

        layout.addLayout(self.search_row)
        
        layout.setAlignment(Qt.AlignCenter)
    
    def hello(self):
        print('Hello World!')

def window():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
