from view.platine import Platine

class Controler():
    
    def __init__(self):
        self.platine = Platine()
        
    def start(self):
        # Bouton démarrer
        self.platine.bouton_Start.wait_for_press()
        self.platine.start()