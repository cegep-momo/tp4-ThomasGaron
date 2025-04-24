from .LCD1602 import CharLCD1602

class view:
    def __init__(self):
        self.ecran_lcd = CharLCD1602()
        self.ecran_lcd.init_lcd(0x27, 1)
        
    def afficher(self, mesure):
        self.ecran_lcd.clear()
        self.ecran_lcd.write(0, 0, f"Dst: {mesure.distance} cm")
        self.ecran_lcd.write(1,0, f"ADC: {mesure.adc}")