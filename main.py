from pygame import *
win_width = 700
win_height = 500
window = display.set_mode((win_width,win_height))
display.set_caption("Maze")
background = transform.scale(image.load("BackGround.png"),(win_width,win_height))

game = True
clock = time.Clock()
FPS = 60
mixer.init()
mixer.music.load("MUSIC.mp3")
mixer.music.play()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.rect = self.image.get_rect()
        self.speed = player_speed
        self.rect_x = player_x
        self.rect_y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 3:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 70:
            self.rect.x += self.speed
        if keys[K_DOWN] and self.rect.y <  win_height - 70:
            self.rect.y += self.speed
        if keys[K_UP] and self.rect.y > 3:
            self.rect.y -= self.speed
class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= win_width - 85:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Wall(sprite.Sprite):
    def __init__(self, color_1,color_2,color_3,wall_x,wall_y,wall_width,wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.wall_width = wall_width
        self.wall_heigth = wall_height
        self.image = Surface((self.wall_width, self.wall_heigth))
        self.image.fill((color_1,color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect_x = wall_x
        self.rect_y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
w1 = Wall(90,102,62,100,20,450,10)
w2 = Wall(90, 102, 62,100,20,450,10)
w3 = Wall(90, 102, 62,100,20,450,10)
w4 = Wall(90, 102, 62,100,20,450,10)
w5 = Wall(90, 102, 62,100,20,450,10)
w6 = Wall(90, 102, 62,100,20,450,10)
w7 = Wall(90, 102, 62,100,20,450,10)

player = Player("Knight-transformed.png",5, win_height - 80,4)
enemy = Enemy("Sceleton-transformed.png",win_width - 80, 280, 3)
goal = GameSprite('treasure.png',400,420,0)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        window.blit(background, (0,0))
        player.update()
        player.reset()
        enemy.update()
        enemy.reset()
        goal.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        display.update()
        clock.tick(FPS)

