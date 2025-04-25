import time
from gpiozero import Button, DistanceSensor
from time import sleep
from view.ADCDevice import *

class Platine:
    def __init__(self):
        
        self.bouton_Start = Button(26)
        self.bouton_Mesurer = Button(19)
        
        self.capteur = DistanceSensor(echo=24, trigger=23, max_distance=3)
        time.sleep(2)
        
        self.adc = ADCDevice()
        if self.adc.detectI2C(0x4b):
            self.adc = ADS7830()
        else:
            print("Erreur : adresse I2C non trouvée")
            exit(-1)
        
    def mesurer_dst(self):
        while True:
            cm = self.capteur * 100
            print("Distance: " + str(cm) + " cm")
            sleep(1)
            
    def get_adc(self):
        return self.adc.analogRead(0)
    
    def mesurer_adc(self):   
        while True:
            valeurADC = self.adc.analogRead(0)
            voltage = valeurADC / 255.0 * 3.3
            print ('Valeur ADC : %d, Voltage : %.2f'%(valeurADC, voltage))
            time.sleep(0.03)
            
    def lesMesures(self):
        try:
            distance = round(self.capteur.distance * 100, 2)
        except:
            distance = -1

        adc_value = self.adc.analogRead(0)
        voltage = round(adc_value / 255.0 * 3.3, 2)

        return distance, voltage, adc_value