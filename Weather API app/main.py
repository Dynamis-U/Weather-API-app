import sys
# sys is a built-in Python module that provides functions and variables related to the Python interpreter and the system.
import requests 
#Requests is used to communicate with websites/APIs over HTTP
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                       QLineEdit, QPushButton, QVBoxLayout)
#QApplication : This is responsible for managing your GUI application.Think of it as the engine running your application.

#A QWidget is a basic GUI component. It can represent things such as:

# a window
# a button
# a label
# a text box
# etc.

# A QLabel displays text or images.

# QLineEdit

# This creates a text input box.

# QVBoxLayout

# This controls how widgets are arranged vertically.





from PyQt5.QtCore import Qt

# you're importing something called Qt from PyQt5.

# Qt provides many constants and options used for GUI behavior.

class WeatherApp(QWidget): # Creating WeatherApp class and WeatherApp gets the functionality of QWidget
    def __init__(self): #__init__ is a special Python method.It runs automatically when you create an object from your class
        super().__init__()
        # super() allows you to access the parent class, which is QWidget.

        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI();

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri;
            }
            QLabel#city_label{
                font-size: 40px;
                font-style: itatic;
            }
            QLineEdit#city_input{
                font-size: 40px;
            }
            QPushButton#get_weather_button{
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label{
                font-size: 75px;
            }
            QLabel#emoji_label{
                font-size: 100px;
                font-family: Segoe UI emoji;
            }
            QLabel#description_label{
                font-size: 50px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

        

    def get_weather(self):
        api_key = "ff841a5af1eb625246029e7b280e8e66"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad request\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized Access\nInvalid API key")
                    
                case 403:
                    self.display_error("Forbidden\nAccess is denied")
                       
                case 404:
                    self.display_error("Not Found\nCity not found")
                
                case 500:
                    self.display_error("Internal Server Error\nPlease try again later")
        
                case 503:
                    self.display_error("Bad Gateway\nInvalid response from the server")
                    
                case 504:
                    self.display_error("Gateway Timeout\nNo reponse from the server")
                case _:
                    self.display_error("HTTP error occured\n{http_error}")
                    

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection")
            
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")
            
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects:\nThe request timed out")
            
        except requests.exceptions.RequestException as req_error:
            self.display_error("Request Error:\n{req_error}")
                                
                
                
        except requests.exceptions.RequestException:
            pass

            

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self,data):
        self.temperature_label.setStyleSheet("font-size: 75px;")
        self.description_label.setStyleSheet("font-size: 30px;")
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        temperature_f = (temperature_k * 9/5) - 459.67
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]

        print(data)

        self.temperature_label.setText(f"{temperature_c:.0f}℃")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)

    @staticmethod
    def get_weather_emoji(weather_id):

        if 200 <= weather_id <= 232:
            return "⛈️"

        elif 300 <= weather_id <= 321:
            return "⛅"

        elif 500 <= weather_id <= 531:
            return "🌧️"

        elif 600 <= weather_id <= 622:
            return "🌨️"

        elif 701 <= weather_id <= 741:
            return "🌫️"

        elif weather_id == 762:
            return "🌋"

        elif weather_id == 771:
            return "💨"

        elif weather_id == 781:
            return "🌪️"

        elif weather_id == 800:
            return "☀️"

        elif 801 <= weather_id <= 804:
            return "💭"

        else:
            return ""
if __name__ == "__main__":
    #Suppose another Python file does:

    # import main

    # Then the code inside:

    # if __name__ == "__main__":

    # doesn't automatically execute.

    #This allows a Python file to be both:

    # run directly
    # imported as a module


    app = QApplication(sys.argv) #sys.argv contains the arguments given when you start your Python program from the terminal
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())