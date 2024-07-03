#Jet Fighter

import random
import time

class Plane():
    def __init__(self):
        pass
        
    def move():     #lewa/prawa: obrót o np. 10 st.// przytrzymanie klawisza - "płynny obrót" 
        pass
    
    def shoot():
        pass
    
    def speed():    #czy potrzebne tutaj?
        pass
    
class Bullet():
    def __init__(self):
        pass
    
    def move():    
        pass
        
    def speed():
        pass
        
    def hit():   #zzderzenie z samolotem - puntk; z przeskzodą - zero pkt
        pass

class Blok():     #klasa przeszkody (chmurki, bloczki i takie tam); randomizowane miejsca? wolniej się poruszają
    def move():
        pass
             
#na początku gry: komunikat --> wybór rodzaju gracza (pierogi, szynka etc.); wybór ilości strzałów; 
#zliczanie punktów
#setup/plansza
      

# plansza
def setup():
    size(900, 900)
    textSize(100)

def draw():
    text('JET FIGHTER', width/2-280, height/2)                    #wyświetlanie nazwy gry na początku
    textSize(20)
    text('press ENTER to continue', width/2-120, height/2+100)
    textSize(100)
    if key == '\n':                                               #po kliknięciu enter przechodzimy dalej/zaczynamy grę (tło się zamalowuje)
        background(150)
        
    
    

        
