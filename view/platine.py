from gpiozero import Button

class Platine:
    def __init__(self):
        
        self.bouton_Start = Button(5)
        self.bouton_Mesurer = Button(13)