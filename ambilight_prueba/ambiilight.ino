#include <Adafruit_NeoPixel.h>

const int pin = 2;  // Pin de la tira de LEDs (ajusta según lo que uses)
const int numLEDs = 30;  // Número de LEDs en la tira

Adafruit_NeoPixel strip(numLEDs, pin, NEO_GRB + NEO_KHZ800);

void setup() {
  Serial.begin(9600);
  strip.begin();
  strip.show();  // Inicializar todos los LEDs como apagados
}

void loop() {
  if (Serial.available() >= numLEDs * 3) {  // Cada LED usa 3 bytes (RGB)
    for (int i = 0; i < numLEDs; i++) {
      byte r = Serial.read();
      byte g = Serial.read();
      byte b = Serial.read();
      strip.setPixelColor(i, strip.Color(r, g, b));
    }
    strip.show();  // Actualizar la tira de LEDs
  }
}
