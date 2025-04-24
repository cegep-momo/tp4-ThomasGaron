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
        print("Système démarré")
        
        while True:
            self.platine.bouton_Mesurer.wait_for_press()
            self.mesurer()
            
    def mesurer(self):
        dst, volt, adc = self.platine.mesure()
        print(f"Distance: {dst} cm, Voltage : {volt} V, ADC : {adc}")
        
        x = mesure(dst, volt, adc)
        self.vue.afficher(x)
        model.sauvegarde_json()
        time.sleep(5)
            
            