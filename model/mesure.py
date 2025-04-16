from datetime import datetime

class mesure():
    def __init__(self, distance, volt, adc):
        self.distance = distance
        self.volt = volt
        self.adc = adc
    
    def retourner(self):
        return {
            "Date": str(datetime.now()),
            "Distance": f"{self.distance} cm",
            "Voltage": f"{self.volt}",
            "ADC": f"{self.adc}"
        }