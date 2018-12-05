import pygame
from time import gmtime, strftime
pygame.init()

win = pygame.display.set_mode((1500,1000))

pygame.display.set_caption("First Game")

walkLeft = [pygame.image.load('HeroRIGHT\_RUN_000.png'), pygame.image.load('HeroRIGHT\_RUN_001.png'), pygame.image.load('HeroRIGHT\_RUN_002.png'), pygame.image.load('HeroRIGHT\_RUN_003.png'), pygame.image.load('HeroRIGHT\_RUN_004.png'), pygame.image.load('HeroRIGHT\_RUN_005.png'), pygame.image.load('HeroRIGHT\_RUN_006.png')]
walkRight = [pygame.image.load('HeroLEFT\_RUN_000.png'), pygame.image.load('HeroLEFT\_RUN_001.png'), pygame.image.load('HeroLEFT\_RUN_002.png'), pygame.image.load('HeroLEFT\_RUN_003.png'), pygame.image.load('HeroLEFT\_RUN_004.png'), pygame.image.load('HeroLEFT\_RUN_005.png'), pygame.image.load('HeroLEFT\_RUN_006.png')]
bg = pygame.image.load('bg.png')
charRight = [pygame.image.load('HeroIDLE\_IDLE_000.png'), pygame.image.load('HeroIDLE\_IDLE_001.png'), pygame.image.load('HeroIDLE\_IDLE_002.png'), pygame.image.load('HeroIDLE\_IDLE_003.png'), pygame.image.load('HeroIDLE\_IDLE_004.png'), pygame.image.load('HeroIDLE\_IDLE_005.png'), pygame.image.load('HeroIDLE\_IDLE_006.png')]
charLeft = [pygame.image.load('HeroIDLEleft\_IDLE_000.png'), pygame.image.load('HeroIDLEleft\_IDLE_001.png'), pygame.image.load('HeroIDLEleft\_IDLE_002.png'), pygame.image.load('HeroIDLEleft\_IDLE_003.png'), pygame.image.load('HeroIDLEleft\_IDLE_004.png'), pygame.image.load('HeroIDLEleft\_IDLE_005.png'), pygame.image.load('HeroIDLEleft\_IDLE_006.png')]

clock = pygame.time.Clock()


class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 85, self.y + 25, 45, 80)
        

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//7], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//7], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                number = (int(strftime("%S", gmtime()))) % 7
                win.blit(charRight[number], (self.x,self.y))
            else:
                number = (int(strftime("%S", gmtime()))) % 7
                win.blit(charLeft[number], (self.x,self.y))
                
        self.hitbox = (self.x + 85, self.y + 25, 45, 80)
        pygame.draw.rect(win, (255,0,0), self.hitbox,2)


class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)


class enemy(object):
    walkRight = [pygame.image.load('OrcRIGHT\RUN_000.png'), pygame.image.load('OrcRIGHT\RUN_001.png'), pygame.image.load('OrcRIGHT\RUN_002.png'), pygame.image.load('OrcRIGHT\RUN_003.png'), pygame.image.load('OrcRIGHT\RUN_004.png'), pygame.image.load('OrcRIGHT\RUN_005.png'), pygame.image.load('OrcRIGHT\RUN_006.png')]
    walkLeft = [pygame.image.load('OrcLEFT\RUN_000.png'), pygame.image.load('OrcLEFT\RUN_001.png'), pygame.image.load('OrcLEFT\RUN_002.png'), pygame.image.load('OrcLEFT\RUN_003.png'), pygame.image.load('OrcLEFT\RUN_004.png'), pygame.image.load('OrcLEFT\RUN_005.png'), pygame.image.load('OrcLEFT\RUN_006.png')]
    
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 60, self.y + 5, 40, 80)

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0
        
        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount//7], (self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount//7], (self.x,self.y))
            self.walkCount += 1
        self.hitbox = (self.x + 60, self.y + 5, 40, 80)
        pygame.draw.rect(win, (255,0,0), self.hitbox,2)
            
    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        


def redrawGameWindow():
    win.blit(bg, (0,0))
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    
    pygame.display.update()


#mainloop
man = player(800, 700, 64,64)
goblin = enemy(100, 700, 64, 64, 1000)
bullets = []
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1
            
        if len(bullets) < 5:
            bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 1000 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
        
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
            
    redrawGameWindow()

pygame.quit()


