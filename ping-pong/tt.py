from pygame import *

class Gamesp(sprite.Sprite):
    def __init__(self, pl_image, pl_y, pl_x, size_x, size_y, pl_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(pl_image), (size_x, size_y))
        self.speed = pl_speed
        self.rect = self.image.get_rect()
        self.rect.x = pl_x
        self.rect.y = pl_y
    def reset(self):
        w.blit(self.image, (self.rect.x, self.rect.y))

class Player(Gamesp):
    def upd_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 15:
            self.rect.y = self.rect.y - self.speed
        if keys[K_s] and self.rect.y < 625:
            self.rect.y = self.rect.y + self.speed
        
        
    def upd_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 15:
            self.rect.y = self.rect.y - self.speed
        if keys[K_DOWN] and self.rect.y < 625:
            self.rect.y = self.rect.y + self.speed
        
class Pl1(Gamesp):
    def update(self):      
        if self.rect.y > 475:
            self.rect.y = self.rect.y - self.speed
        if self.rect.y < 25:
            self.rect.y = self.rect.y + self.speed

        global aa
        aa = "rig"
        if aa == "rig":
            self.rect.x = self.rect.x - self.speed 
        if aa == "lef":
            self.rect.x = self.rect.x + self.speed

font.init()
f1 = font.Font(None, 30)

width = 700
height = 500
player = "rocket.png"
bal = "asteroid.png"
im_back = 'galaxy.jpg'

display.set_caption("Ping-pong")
w = display.set_mode((width, height))
b1 = transform.scale(image.load(im_back), (width, height))

player_l = Player(player, 250, 30, 50, 100, 9)
player_r = Player(player, 250, 670, 50, 100, 9)
ball = Pl1(bal, 250, 350, 50, 50, 5)

game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if not finish:
        w.blit(b1, (0, 0))

        player_l.upd_l()
        player_r.upd_r()
        ball.update()

        ball.reset()
        player_l.reset()
        player_r.reset() 
        
        if sprite.collide_rect(player_l, ball):
            aa = "lef"
        
        if sprite.collide_rect(player_r, ball):
            aa = "rig"
            
        if ball.rect.x > 700:
            text = f1.render("Игрок 1 выиграл", True, (255, 255, 255))
            w.blit(text,(275, 225))
            player_l = Player(player, 250, 30, 50, 100, 9)
            player_r = Player(player, 250, 670, 50, 100, 9)
            ball = Pl1(bal, 250, 350, 50, 50, 5)
        
        if ball.rect.x < 0:
            text = f1.render("Игрок 2 выиграл", True, (255, 255, 255))
            w.blit(text,(275, 225))
            player_l = Player(player, 250, 30, 50, 100, 9)
            player_r = Player(player, 250, 670, 50, 100, 9)
            ball = Pl1(bal, 250, 350, 50, 50, 3)
            
    display.update()

    time.delay(50)
