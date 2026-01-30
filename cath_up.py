from pygame import *
from random import *

WIDTH = 700
HEIGHT = 500
window = display.set_mode((WIDTH,HEIGHT))
display.set_caption('Футбол')
background = transform.scale(image.load('forest.gif'), (WIDTH, HEIGHT))
lost = 0
score = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x,player_y, player_width, player_height,  player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def updateL(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 600:
            self.rect.y += self.speed
    def updateR(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 15:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 455:
            self.rect.y += self.speed

       
playerL = Player('sprite2.png', 10, 200,65, 65, 5)
playerR = Player('sprite1.png', 630, 200,65, 65, 5)
ball = GameSprite('ball.png', 350, 250, 50,50, 10)

font.init()
ff1 = font.Font(None, 70)
ff2 = font.Font(None, 40)
win = ff1.render('You win!', True, (250, 0, 0))
lose = ff1.render('You lose', True, (255, 0, 0))

clock = time.Clock()
FPS = 60
game = True
finish = False
dx = 3
dy = 3
scoreL = 0
scoreR = 0
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0,0))
        ball.rect.x += dx 
        ball.rect.y += dy
        if sprite.collide_rect(playerL, ball) or sprite.collide_rect(playerR, ball):
            dx *= -1
        if ball.rect.y < 0 or ball.rect.y >490:
            dy *= -1
        if ball.rect.x < 0:
            scoreR += 1
            dx *= -1
        textS = ff1.render('Счет R:' + str(scoreR), True, (0, 0, 255))
        window.blit(textS, (450, 30))
        if ball.rect.x > 680:
            scoreL += 1
            dx *= -1
        textL = ff1.render('Счет L:' + str(scoreL), True, (0, 0, 255))
        window.blit(textL, (30, 30))
        if scoreR > 3:
            winner = 'Правый победил'
            finish = True
        if scoreL > 3:
            winner = 'Левый победил'
            finish = True
        playerL.updateL()
        playerR.updateR()
        ball.reset()
        playerL.reset()
        playerR.reset()
    if finish:
        win = ff1.render(winner, True, (250, 0, 0))
        window.blit(win, (WIDTH//2-200, HEIGHT//2))
        

    display.update()
    clock.tick(FPS)
