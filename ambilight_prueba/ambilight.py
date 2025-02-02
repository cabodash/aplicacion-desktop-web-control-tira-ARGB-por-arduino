import serial
import mss
import numpy as np
import time

# Configuración de la comunicación serial
arduino = serial.Serial('COM4', 9600, timeout=1)  # Ajusta el puerto COM si es necesario

def capture_screen():
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        screenshot = sct.grab(monitor)
        return np.array(screenshot)

def extract_colors(image, num_leds, led_width):
    led_colors = []
    height, width, _ = image.shape
    for i in range(num_leds):
        x_start = i * led_width
        x_end = (i + 1) * led_width
        led_section = image[:, x_start:x_end]
        avg_color = np.mean(led_section, axis=(0, 1))
        led_colors.append(avg_color)
    return led_colors

def send_colors_to_arduino(colors):
    for color in colors:
        r, g, b = int(color[0]), int(color[1]), int(color[2])
        arduino.write(bytes([r, g, b]))

def run_led_system(num_leds, led_width):
    while True:
        screen_image = capture_screen()
        colors = extract_colors(screen_image, num_leds, led_width)
        send_colors_to_arduino(colors)
        time.sleep(0.02)  # Ajusta la frecuencia de actualización

# Ejecutar el sistema con 30 LEDs y un ancho de sección adecuado
run_led_system(30, 16)  # Ajusta led_width si es necesario
