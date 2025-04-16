from LCD1602 import CharLCD1602

class view:
    def __init__(self):
        
        CharLCD1602.init()
        
    def afficher(self, mesure):
        CharLCD1602.clear()
        CharLCD1602.write(0, 0, f"Dst: {mesure.distance} cm")
        CharLCD1602.write(1,0, f"ADC: {mesure.adc}")