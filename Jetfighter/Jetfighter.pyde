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

class Chmury():     #klasa przeszkody (chmurki); randomizowane miejsca? wolniej się poruszają
    def __init__(self, x, y, d):
        self.x = x              #wpółrzędna x lewego kółka chmury
        self.y = y              #wpółrzędna y lewego kółka chmury
        self.d = d              #średnica lewego kółka chmury
        
    def drawing(self, ):
        fill(250)
        noStroke()
        circle(100, 100, 50)
        circle(150, 100, 50)
        circle(125, 75, 60)
        rect(100, 100, 50, 25)
        
    def move():
        pass
             
#na początku gry: komunikat --> wybór rodzaju gracza (pierogi, szynka etc.); wybór ilości strzałów; 
#zliczanie punktów
#setup/plansza
      

# plansza
def setup():
    size(900, 900)
    textSize(100)
    fill(150)
    global start
    start = None

def draw():
    global start
    if start == None:
        text('JET FIGHTER', width/2-280, height/2)                    #wyświetlanie nazwy gry na początku
        textSize(20)
        text('press ENTER to continue', width/2-120, height/2+100)
        textSize(100)
    if key == '\n':                                               #po kliknięciu enter przechodzimy dalej/zaczynamy grę (tło się zamalowuje)
        start = True                                              #bez tej zmiennej po naciśnięciu innego klawisza niż enter pojawiają się te wcześniejsze napisy
        background(150)
    
    

        
