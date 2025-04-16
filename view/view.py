from LCD1602 import clear, init, write

class view:
    def __init__(self):
        init()
        
    def afficher(self, mesure):
        clear()
        write(0, 0, f"Dst: {mesure.distance} cm")
        write(1,0, f"ADC: {mesure.adc}")