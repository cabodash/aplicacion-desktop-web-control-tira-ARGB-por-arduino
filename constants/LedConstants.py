# Constantes para los colores de los LEDs
FULL = 255
OFF = 0
class Colors:
    RED = (FULL, OFF, OFF)
    GREEN = (OFF, FULL, OFF)
    BLUE = (OFF, OFF, FULL)
    YELLOW = (FULL, FULL, OFF)
    CYAN = (OFF, FULL, FULL)
    MAGENTA = (FULL, OFF, FULL)
    WHITE = (FULL, FULL, FULL)
    OFF = (OFF, OFF, OFF)

#Constantes para la posicion de los colores de los LEDs
class ColorPosition:
    R_POS = 0
    G_POS = 1
    B_POS = 2

# Constantes para los modos de operación de los LEDs
class Modes:
    MODE_OFF = 0
    MODE_ON = 1
    MODE_BLINK = 2
    MODE_BREATHE = 3

