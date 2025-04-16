from view.platine import Platine
# from model.mesure import mesure
# from model.model import model

class Controler():
    
    def __init__(self):
        self.platine = Platine()
        
    def start(self):
        # Bouton démarrer
        self.platine.bouton_Start.wait_for_press()
        self.platine.start()
        
        while True:
            print("Cliquez sur le bouton mesurer.")
            self.platine.bouton_Mesurer.wait_for_press()