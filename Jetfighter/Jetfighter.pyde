#Jet Fighter
#na początku gry: komunikat --> wybór rodzaju gracza (pierogi, szynka etc.); wybór ilości strzałów; 
#zliczanie punktów
#setup/plansza

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

class Chmury():     #klasa przeszkody (chmurka)
    global iteracja
    
    def __init__(self):
        self.d = random.randint(20, 100)                          #średnica lewego kółka chmury
        self.x = random.randint(0+3*self.d, 900)                  #wpółrzędna x lewego kółka chmury
        self.y = random.randint(0+self.d, 900-self.d)             #wpółrzędna y lewego kółka chmury
        
    def drawing(self):
        #rysuje jedną chmurkę (złożoną z 3 kółek i prostokąta) o losowym rozmiarze i lokalizacji, która przesuwa się w prawo z każdą iteracją programu
        fill(250)
        noStroke()
        circle(-self.x + self.d + iteracja % (900+self.x), self.y, self.d)                                 #lewe małe kółko
        circle(-self.x + 2*self.d + iteracja % (900+self.x), self.y, self.d)                               #prawe małe kółko
        circle(-self.x + 1.5*self.d + iteracja % (900+self.x), self.y - 0.5*self.d, 1.2*self.d)            #duże kółko
        rect(-self.x + self.d + iteracja % (900+self.x), self.y, self.d, 0.5*self.d)                       #prostokąt
      

def setup():
    size(900, 900)
    textSize(100)
    fill(150)
    global start, chmura, chmura2, chmura3, chmura4, x, y, d, iteracja
    start = None
    iteracja = 0
    chmura = Chmury()
    chmura2 = Chmury()
    chmura3 = Chmury()
    chmura4 = Chmury()

def draw():
    global start, iteracja
    if start == None:
        text('JET FIGHTER', width/2-280, height/2)                    #wyświetlanie nazwy gry na początku
        textSize(20)
        text('press ENTER to continue', width/2-120, height/2+100)
        textSize(100)
    if key == '\n':                                                   #po kliknięciu enter przechodzimy dalej/zaczynamy grę (tło się zamalowuje)
        start = True                                                  #bez tej zmiennej (start) po naciśnięciu innego klawisza niż enter pojawiają się te wcześniejsze napisy
        background(150)                                               #wszystko, co ma się wyświetlić/zrobić dopiero po naciśnięciu enter musi być w tym bloku 'if'
        chmura.drawing()
        chmura2.drawing()
        chmura3.drawing()
        chmura4.drawing()
    iteracja += 1
    

        
