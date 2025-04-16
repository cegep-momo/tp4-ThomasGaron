from gpiozero import Button, DistanceSensor
from time import sleep

class Platine:
    def __init__(self):
        
        self.bouton_Start = Button(5)
        self.bouton_Mesurer = Button(13)
        
        self.capteur = DistanceSensor(echo = 23, trigger = 24, max_distance = 3)
        
    def mesurer_dst(self):
        while True:
            cm = self.capteur * 100
            print("Distance: " + str(cm) + " cm")
            sleep(1)