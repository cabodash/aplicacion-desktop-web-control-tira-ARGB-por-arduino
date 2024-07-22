from model.Led import Led
import serial, json, time

class LedController:
    def __init__(self, num_leds):
        self.num_leds = num_leds
        self.leds = [Led([0, 0, 0]) for _ in range(num_leds)]  # Inicializa los LEDs en negro
        self.serial_port = serial.Serial('COM3', 250000)  # Cambia 'COM_PORT' por el puerto correcto

    def wheel(self, wheel_pos):
        wheel_pos = 255 - wheel_pos
        if wheel_pos < 85:
            return [255 - wheel_pos * 3, 0, wheel_pos * 3]
        elif wheel_pos < 170:
            wheel_pos -= 85
            return [0, wheel_pos * 3, 255 - wheel_pos * 3]
        else:
            wheel_pos -= 170
            return [wheel_pos * 3, 255 - wheel_pos * 3, 0]

    def rainbow_cycle(self, wait):
        for j in range(256 * 5):  # 2 ciclos de todos los colores para hacerlo más rápido
            for i in range(self.num_leds):
                # Invertir el cálculo del índice de color
                color = self.wheel(((self.num_leds - i - 1) * 256 // self.num_leds + j) & 255)
                self.leds[i].setColor(color)  # Asigna el color al LED usando la clase Led
            self.send_to_arduino()
            time.sleep(wait)  # Espera en milisegundos

    def turn_off(self):
        for led in self.leds:
            led.setColor([0, 0, 0])  # Apaga el LED
        self.send_to_arduino()

    def send_to_arduino(self):
        led_data = {
            "numLeds": self.num_leds,
            "leds": [{"r": led.red, "g": led.green, "b": led.blue} for led in self.leds]
        }
        json_message = json.dumps(led_data)
        print(json_message)  # Imprime el JSON por consola
        self.serial_port.write((json_message + '\n').encode())