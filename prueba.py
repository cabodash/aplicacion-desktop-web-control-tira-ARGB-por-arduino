import eel
import time
import json

# Inicializa eel con la carpeta web donde se encuentra index.html
eel.init('web')

NUM_LEDS = 8  # Número de LEDs
ANIMATION_SPEED = 0.1  # Velocidad de actualización (segundos)

def generate_rainbow_json(frame):
    """Genera un JSON con un efecto arcoíris en movimiento usando RGB normal."""
    leds = []
    r = (frame * 5) % 256
    g = (frame * 3) % 256
    b = (frame * 7) % 256

    for i in range(NUM_LEDS):
        # Los colores se incrementan para crear el efecto arcoíris
        leds.append({"r": r, "g": g, "b": b})
        # Desplazar los colores ligeramente para el efecto arcoíris en movimiento
        r = (r + 20) % 256
        g = (g + 10) % 256
        b = (b + 15) % 256

    return {
        "numLeds": NUM_LEDS,
        "leds": leds
    }

@eel.expose
def start_simulation():
    frame = 0
    while True:
        # Generar el JSON de arcoíris
        data = generate_rainbow_json(frame)
        
        # Mostrar el JSON en la consola antes de enviarlo
        print("Datos enviados al frontend:", json.dumps(data, indent=4))
        
        # Enviar el JSON al frontend
        json_data = json.dumps(data)
        eel.handleData(json_data)  # Enviar datos al frontend
        
        frame += 5  # Incrementar el fotograma para avanzar el arcoíris
        time.sleep(ANIMATION_SPEED)
# Iniciar aplicación
eel.start('prueba.html', size=(600, 600), block=True, port=8080)
start_simulation()
