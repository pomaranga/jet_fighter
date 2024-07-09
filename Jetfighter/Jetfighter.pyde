#Jet Fighter
#na początku gry: komunikat --> wybór rodzaju gracza (pierogi, szynka etc.); wybór ilości strzałów; 
#zliczanie punktów
#setup/plansza

import random
import time

bullets = []
planes = []
iteracja = 0

class Plane():
    def init(self, x, y):
        
        self.x = x
        self.y = y
        self.speed = 2  #tu musimy sprawdzić czy ta szybkość wystarczy
        self.angle = 0  #samolot bedzie sie obracal, a nie zmienial kierunek
        
    def move(self):
        self.x += self.speed * cos(radians(self.angle))
        self.y += self.speed * sin(radians(self.angle))
        if self.x < 0:
            self.x = width
        elif self.x > width:
            self.x = 0
        if self.y < 0:
            self.y = height
        elif self.y > height:
            self.y = 0
            
    def turn_left(self):
        self.angle -= 15

    def turn_right(self):
        self.angle += 15
            
    def shoot(self, is_player_one):
        bullet_x = self.x + 40 * cos(radians(self.angle))
        bullet_y = self.y + 40 * sin(radians(self.angle))
        bullets.append(Bullet(bullet_x, bullet_y, self.angle, is_player_one))
        
    def display(self):
        fill(49, 120, 115) if self == planes[0] else fill(202, 224, 13)
        noStroke()
        with pushMatrix():
            translate(self.x, self.y)
            rotate(radians(self.angle))
            triangle(-50, 40, 50, 0, -50, -40)
            

    
    

    
class Bullet():
    def init(self, x, y, angle, is_player_one):
        self.x = x
        self.y = y
        self.speed = 10
        self.angle = angle
        self.is_player_one = is_player_one
    
    def move(self):
        self.x += self.speed * cos(radians(self.angle))
        self.y += self.speed * sin(radians(self.angle))
        
    def display(self):
        fill(245, 195, 194)
        noStroke()
        circle(self.x, self.y, 11)

    def is_off_screen(self):
        return self.x < 0 or self.x > width or self.y < 0 or self.y > height
        
    def hit():   #zzderzenie z samolotem - puntk; z przeskzodą - zero pkt
        pass

class Chmury():     #klasa przeszkody (chmurka)
    global iteracja
    
    def init(self):
        self.d = random.randint(20, 100)                          #średnica lewego kółka chmury
        self.x = random.randint(0+3*self.d, 900)                  #wpółrzędna x lewego kółka chmury
        self.y = random.randint(0+self.d, 900-self.d)             #wpółrzędna y lewego kółka chmury
        
    def drawing(self):
        #rysuje jedną chmurkę (złożoną z 3 kółek i prostokąta) o losowym rozmiarze i lokalizacji, która przesuwa się w prawo z każdą iteracją programu
        fill(250)
        noStroke()
        circle(-self.x + self.d + iteracja % (width+self.x), self.y, self.d)                                 #lewe małe kółko
        circle(-self.x + 2*self.d + iteracja % (width+self.x), self.y, self.d)                               #prawe małe kółko
        circle(-self.x + 1.5*self.d + iteracja % (width+self.x), self.y - 0.5*self.d, 1.2*self.d)            #duże kółko
        rect(-self.x + self.d + iteracja % (width+self.x), self.y, self.d, 0.5*self.d)                       #prostokąt
      

def setup():
    size(1280, 897)
    textSize(100)
    global start, chmura, chmura2, chmura3, chmura4, iteracja, planes
    start = None
    iteracja = 0
    chmura = Chmury()
    chmura2 = Chmury()
    chmura3 = Chmury()
    chmura4 = Chmury()
    planes.append(Plane(width // 4, height - 50))
    planes.append(Plane(3 * width // 4, 50))

def draw():
    global start, iteracja, img, planes
    if start == None:
        background(150)
        img = loadImage("sky.jpg")
        background(img)
        text('JET FIGHTER', width / 2 - 280, height / 2)
        textSize(20)
        text('press g to continue', width / 2 - 120, height / 2 + 100)
        textSize(100)
    elif start == True:
        background(img)
        chmura.drawing()
        chmura2.drawing()
        chmura3.drawing()
        chmura4.drawing()

        for plane in planes:
            plane.move()
            plane.display()

        for bullet in bullets[:]:
            bullet.move()
            bullet.display()
            if bullet.is_off_screen():
                bullets.remove(bullet)

    iteracja += 1

def keyPressed():
    if key == 'g':
        global start
        start = True

    if keyCode == RIGHT:
        planes[0].turn_right()
    elif keyCode == LEFT:
        planes[0].turn_left()
    elif key == '\n':
        planes[0].shoot(True)

    if key == 'd':
        planes[1].turn_right()
    elif key == 'a':
        planes[1].turn_left()
    elif key == ' ':
        planes[1].shoot(True)