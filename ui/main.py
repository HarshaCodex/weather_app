from util.weather_util import display_weather
from client.weather_client import WeatherClient
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QGridLayout
import sys
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Weather App')
        self.setGeometry(400, 400, 800, 1200)
        
        self.setStyleSheet("""
            QPushButton {
                background-color: #2b5b84;
                color: white;
                border-radius: 20px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #3d7fb5;
            }
            QLineEdit {
                border: 2px solid #2b5b84;
                border-radius: 15px;
                padding: 0 10px;
                font-size: 14px;
            }
        """)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.title_label = QLabel("Weather App")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold; margin-bottom: 20px; color: #2b5b84;")
        layout.addWidget(self.title_label)

        self.search_button = QPushButton('Search')
        self.search_button.setFixedHeight(40)
        self.search_button.setFixedWidth(100)

        self.search_button.clicked.connect(self.get_weather_by_location)

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText('Enter Location')
        self.search_bar.setFixedHeight(30)
        self.search_bar.setFixedWidth(200)

        self.search_row = QHBoxLayout()
        self.search_row.addWidget(self.search_bar)
        self.search_row.addWidget(self.search_button)

        layout.addLayout(self.search_row)
        


        self.info_layout = QGridLayout()
        
        self.location_label = QLabel("Location: -")
        self.elevation_label = QLabel("Elevation: -")
        self.timezone_label = QLabel("Timezone: -")
        self.temp_label = QLabel("Current Temperature: -")
        self.temp_range_label = QLabel("Temperature Range: -")
        self.temp_range_f_label = QLabel("Temperature Range (F): -")

        self.info_layout.addWidget(self.location_label, 0, 0)
        self.info_layout.addWidget(self.elevation_label, 1, 0)
        self.info_layout.addWidget(self.timezone_label, 2, 0)
        self.info_layout.addWidget(self.temp_label, 3, 0)
        self.info_layout.addWidget(self.temp_range_label, 4, 0)
        self.info_layout.addWidget(self.temp_range_f_label, 5, 0)

        layout.addLayout(self.info_layout)
        
        layout.setAlignment(Qt.AlignCenter)
    
    def get_weather_by_location(self):
        location = self.search_bar.text()
        weather = WeatherClient().get_weather_by_city(location)
        display_weather(weather)
        
        self.location_label.setText(f"Location: {weather.latitude}, {weather.longitude}")
        self.elevation_label.setText(f"Elevation: {weather.elevation}m")
        self.timezone_label.setText(f"Timezone: {weather.timezone}")
        self.temp_label.setText(f"Current Temperature: {weather.get_current_temperature()}°C")
        
        min_temp, max_temp = weather.get_temperature_range()
        self.temp_range_label.setText(f"Temperature Range: {min_temp}°C to {max_temp}°C")
        self.temp_range_f_label.setText(f"Temperature Range (F): {weather.celsius_to_fahrenheit(min_temp):.1f}°F to {weather.celsius_to_fahrenheit(max_temp):.1f}°F")

def window():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
