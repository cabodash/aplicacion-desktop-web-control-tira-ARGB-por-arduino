from controllers.LedController import LedController
import eel
import ctypes
import threading
NUM_LEDS = 8

# Obtiene la resolución de la pantalla
user32 = ctypes.windll.user32
window_width, window_height = user32.GetSystemMetrics(0) // 2, user32.GetSystemMetrics(1) // 2

# Inicializa Eel con el tamaño de la ventana
eel.init('web', allowed_extensions=['.js', '.html', '.css'])

@eel.expose
def say_hello_py(name):
    print(f"Hola desde {name}")

# Crea una instancia del controlador de LEDs
controller = LedController(num_leds=NUM_LEDS)

# Evento para controlar el ciclo de arcoíris
stop_event = threading.Event()

def run_rainbow_cycle():
    while not stop_event.is_set():  # Verifica si se debe detener
        controller.rainbow_cycle(wait=0.006)
        if stop_event.is_set():  # Verifica nuevamente si se debe detener
            break  # Sale del bucle si se ha establecido el evento

@eel.expose
def start_rainbow_cycle():
    stop_event.clear()  # Asegúrate de que el evento esté limpio
    threading.Thread(target=run_rainbow_cycle, daemon=True).start()

@eel.expose
def stop_rainbow_cycle():
    stop_event.set()  # Establece el evento para detener el ciclo
    
    
@eel.expose
def setCycleFalse():
    controller.turn_off()

eel.start('app.html', size=(window_width, window_height), title="Led Control v1.0", mode='chrome')