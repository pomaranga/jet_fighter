      #Jet Fighter
#na początku gry: komunikat --> wybór rodzaju gracza (pierogi, szynka etc.); wybór ilości strzałów; 
#zliczanie punktów
#setup/plansza

import random
import time

bullets = []
planes = []
iteracja = 0
player1_score = 0
player2_score = 0
player1_name = ""
player2_name = ""
max_hits = 0
game_state = "START" 
start_time = 0
current_time = 0

class Plane():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 10  #tu musimy sprawdzić czy ta szybkość wystarczy
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
    
    def check_collision(self, bullet):                            # Sprawdzenie, czy samolot został trafiony
        distance = dist(self.x, self.y, bullet.x, bullet.y)
        return distance < 40 

class Bullet():
    def __init__(self, x, y, angle, is_player_one):
        self.x = x
        self.y = y
        self.speed = 30
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

class Chmury():
    global iteracja
    
    def __init__(self):
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
    textAlign(CENTER, CENTER)
    global chmura, chmura2, chmura3, chmura4, iteracja, planes, game_state
    iteracja = 0
    chmura = Chmury()
    chmura2 = Chmury()
    chmura3 = Chmury()
    chmura4 = Chmury()
    planes.append(Plane(width // 4, height - 50))
    planes.append(Plane(3 * width // 4, 50))
    game_state = "START"                                           # Stan rozpoczęcia gry

def draw():
    global start, iteracja, img, planes, player1_score, player2_score, game_state, player1_name, player2_name, max_hits, start_time, current_time
    background(150)
    img = loadImage("sky.jpg")
    background(img)
    
    if game_state == "START":                                      # Wyświetlenie tytułu gry i prośba o podanie imienia gracza 1
        textSize(100)
        text('JET FIGHTER', width / 2, height / 3)
        textSize(30)
        text("Enter Player 1 name:", width / 2, height / 2)
        text(player1_name, width / 2, height / 2 + 50)
        text("Press ENTER to confirm", width / 2, height / 2 + 100)
        text("STRZALKI. SHOOT: ENTER", width / 2, height / 2 + 200)
    
    elif game_state == "INPUT_NAME2":                              # Prośba o podanie imienia gracza 2
        textSize(100)
        text('JET FIGHTER', width / 2, height / 3)
        textSize(30)
        text("Enter Player 2 name:", width / 2, height / 2)
        text(player2_name, width / 2, height / 2 + 50)
        text("Press ENTER to confirm", width / 2, height / 2 + 100)
        text("A I D. SHOOT: SPACE", width / 2, height / 2 + 200)
    
    elif game_state == "INPUT_HITS":                               # Prośba o podanie liczby trafień potrzebnych do wygranej
        textSize(100)
        text('JET FIGHTER', width / 2, height / 3)
        textSize(30)
        text("Enter number of hits to win:", width / 2, height / 2)
        text(str(max_hits), width / 2, height / 2 + 50)
        text("Press ENTER to start the game", width / 2, height / 2 + 100)
    
    elif game_state == "PLAY":                                     # Główna pętla gry
        if start_time == 0:
            start_time = millis()
        
        current_time = (millis() - start_time) / 1000              # Zapisanie czasu rozpoczęcia gry

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
            
            for i, plane in enumerate(planes):                     # Sprawdzenie kolizji kul z samolotami
                if plane.check_collision(bullet):
                    if bullet.is_player_one != (i == 0):
                        if bullet.is_player_one:
                            player1_score += 1
                        else:
                            player2_score += 1
                        bullets.remove(bullet)
                        if player1_score >= max_hits or player2_score >= max_hits:
                            game_state = "END"                     # Zakończenie gry, jeśli któryś gracz osiągnie maksymalną liczbę trafień
                        break
            
            if bullet.is_off_screen():
                bullets.remove(bullet)

        fill(255)                                                  # Wyświetlenie wyników i czasu
        textSize(24)
        textAlign(LEFT, TOP)
        text(player2_name + ": " + str(player2_score), 10, 10)
        textAlign(RIGHT, TOP)
        text(player1_name + ": " + str(player1_score), width - 10, 10)
        
        textAlign(CENTER, TOP)
        text("Time: {:.1f}".format(current_time), width / 2, 10)

        textAlign(CENTER, TOP)
        text("Hits to win: " + str(max_hits), width / 2, 40)

    elif game_state == "END":                                      # Wyświetlenie ekranu końca gry
        textSize(50)
        if player1_score >= max_hits:
            text(player1_name + " wins!", width / 2, height / 2 - 50)
        elif player2_score >= max_hits:
            text(player2_name + " wins!", width / 2, height / 2 - 50)
        
        textSize(30)
        text("Final Score:", width / 2, height / 2 + 50)
        text(player1_name + ": " + str(player1_score), width / 2, height / 2 + 100)
        text(player2_name + ": " + str(player2_score), width / 2, height / 2 + 150)
        text("Total time: {:.1f} seconds".format(current_time), width / 2, height / 2 + 200)

    iteracja += 1

def keyPressed():
    global game_state, player1_name, player2_name, max_hits, start, start_time
    
    if game_state == "START":
        if key == ENTER:
            if player1_name:
                game_state = "INPUT_NAME2"
            return
        if key == BACKSPACE:
            player1_name = player1_name[:-1]
        elif key != CODED and len(player1_name) < 10:
            player1_name += key
    
    elif game_state == "INPUT_NAME2":
        if key == ENTER:
            if player2_name:
                game_state = "INPUT_HITS"
            return
        if key == BACKSPACE:
            player2_name = player2_name[:-1]
        elif key != CODED and len(player2_name) < 10:
            player2_name += key
    
    elif game_state == "INPUT_HITS":
        if key == ENTER and max_hits > 0:
            game_state = "PLAY"
            start = True
            start_time = 0
            return
        if key == BACKSPACE:
            max_hits = max_hits // 10
        elif key.isdigit():
            max_hits = max_hits * 10 + int(key)
    
    elif game_state == "PLAY":
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
            planes[1].shoot(False)
