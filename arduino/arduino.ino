#include <ArduinoJson.h>
#include <Adafruit_NeoPixel.h>

const int PIN = A0; // Pin donde está conectada la tira LED
const int MAX_LEDS = 10; // Número máximo de LEDs
Adafruit_NeoPixel strip = Adafruit_NeoPixel(MAX_LEDS, PIN, NEO_GRB + NEO_KHZ800);

const int RED_INDEX = 0;
const int GREEN_INDEX = 1;
const int BLUE_INDEX = 2;
const int LED_SIZE = 3;

class Led {
  public:
    int red;
    int green;
    int blue;
    
    Led() { // Constructor por defecto
      red = 0;
      green = 0;
      blue = 0;
    }

    Led(int red, int green, int blue) { 
      red = red;
      green = green;
      blue = blue;
    }

    Led(int rgb[]) {
      red = rgb[RED_INDEX];
      green = rgb[GREEN_INDEX];
      blue = rgb[BLUE_INDEX];
    }
};

Led ledArray[MAX_LEDS]; // Array para almacenar objetos Led

void setup() {
  Serial.begin(250000);
  strip.begin(); // Inicializa la tira LED
  strip.show();  // Apaga todos los LEDs al inicio
}

void loop() {
  if (Serial.available() > 0) {
    String jsonString = Serial.readStringUntil('\n'); // Leer la cadena JSON
    processJson(jsonString); // Procesar el JSON
  }
}

void processJson(String jsonString) {
  StaticJsonDocument<200> doc; // Crear un documento JSON
  DeserializationError error = deserializeJson(doc, jsonString); // Deserializar JSON

  if (!error) {
    int numLeds = doc["numLeds"];
    updateLedArray(numLeds, doc); // Actualizar el array de LEDs
    updateStrip(); // Actualiza la tira LED con los nuevos valores
  } else {
    Serial.println("Error al deserializar JSON");
  }
}

void updateLedArray(int numLeds, StaticJsonDocument<200>& doc) {
  for (int i = 0; i < numLeds && i < MAX_LEDS; i++) {
    int rgb[3]; // Declarar el array rgb con tamaño fijo de 3
    rgb[RED_INDEX] = doc["leds"][i]["r"];
    rgb[GREEN_INDEX] = doc["leds"][i]["g"];
    rgb[BLUE_INDEX] = doc["leds"][i]["b"];
    
    ledArray[i] = Led(rgb); // Crear un nuevo objeto Led y almacenarlo en el array
  }
}

void updateStrip() {
  for (int i = 0; i < MAX_LEDS; i++) {
    strip.setPixelColor(i, strip.Color(ledArray[i].red, ledArray[i].green, ledArray[i].blue));
  }
  strip.show(); // Muestra los cambios en la tira LED
}