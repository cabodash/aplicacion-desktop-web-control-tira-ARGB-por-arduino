import constants.ArduinoConstants as ac
import json, serial

class ArduinoUtils:

    serial.Serial(ac.COM, ac.SERIAL_PORT)

    @staticmethod
    def send_to_arduino(num_leds, leds):
        led_data = {
            "numLeds": num_leds,
            "leds": [{"r": led.red, "g": led.green, "b": led.blue} for led in leds]
        }
        json_message = json.dumps(led_data)
        print(json_message)  # Imprime el JSON por consola
        serial.write((json_message + '\n').encode())