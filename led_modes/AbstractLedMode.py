from abc import ABC, abstractmethod
import model.Led as Led
import utils.ArduinoUtils as ArduinoUtils
import json

class AbstractLedMode(ABC):

    #configuration and control vars
    num_leds = 0
    leds = []
    effect_on = False
    config = []

    def __init__(self, num_leds, effect_on, config):
        self.num_leds = num_leds
        self.leds = [Led([0, 0, 0]) for _ in range(num_leds)]  # Inicializa los LEDs en negro
        self.effect_on = effect_on
        self.config = config

    #Method for implementing the effect's logic
    @abstractmethod
    def run_effect(self):
        """Implements the logic for the led effect. \n
           This method must be implemented by the subclasses."""
        pass

    def send_json(self):
        pass
