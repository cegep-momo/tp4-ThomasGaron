from view.platine import Platine
from model.mesure import mesure
from model.model import model
import time
from view.view import view

class Controler():
    
    def __init__(self):
        self.platine = Platine()
        self.vue = view()
        
        
    def start(self):
        # Bouton démarrer
        self.platine.bouton_Start.wait_for_press()
        print("Systeme demarre")
        
        self.platine.bouton_Mesurer.wait_for_press()
        
            
        while True:
            if self.platine.bouton_Start.is_pressed:
                print("FIN")
                self.vue.ecran_lcd.clear()
                self.vue.ecran_lcd.write(0, 0, "FIN")
                break
            
            self.mesurer()
            time.sleep(5)
            
        
            
    def mesurer(self):
        dst, volt, adc = self.platine.lesMesures()
        print(f"Distance: {dst} cm, Voltage : {volt} V, ADC : {adc}")
        
        x = mesure(dst, volt, adc)
        self.vue.afficher(x)
        model.sauvegarde_json(x)
            
            