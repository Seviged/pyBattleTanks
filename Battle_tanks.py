# -*- coding: UTF-8 -*-
import pygame
import random
import time
import levels


pygame.init()
size = 650,500
screen = pygame.display.set_mode(size, pygame.DOUBLEBUF | pygame.HWSURFACE)
pygame.display.set_caption('Battle Tanks')
clock = pygame.time.Clock()
color = 0, 0, 0
color2 = 0, 255, 0

fs = pygame.image.load('images/fs.png')
back = pygame.image.load('images/back.png')
kir = pygame.image.load('images/kir.png')
beton = pygame.image.load('images/beton.png')
forest = pygame.image.load('images/forest.png')
base = pygame.image.load('images/base.png')
dbase = pygame.image.load('images/dbase.png')
water = pygame.image.load('images/water.png')
bullet1 = pygame.image.load('images/ammo.png')
bullet2 = pygame.transform.rotate(bullet1, 180)
bullet3 = pygame.transform.rotate(bullet1, 90)
bullet4 = pygame.transform.rotate(bullet1, 270)
ggu = pygame.image.load('images/ggu.png')
enu = pygame.image.load('images/vrag1.png')
enu2 = pygame.image.load('images/vrag2.png')
enu3 = pygame.image.load('images/vrag3.png')
e = pygame.image.load('images/e.png')
bb = pygame.image.load('images/bboom.png')
bl = pygame.image.load('images/blopatka.png')
bz = pygame.image.load('images/bzvezdochka.png')
e_rect = e.get_rect()
e_rect.width = e_rect.height
slide_rect = e.get_rect()
slide_rect.width = slide_rect.height
reloads = 60
bonuses = []
level = 0
ii=0
lopatka = 0
orient = 1
move = 0
lev = levels.lev[level]
matrix =  lev
counten = 0
betas = 0
x = 0
y = 0
a = matrix
shoot = 0
fly = 0
ilolo = 118
shoots = []
enemi = []
gmove = 0
vermove = 0
key = 0
enable = 0
font = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None, 18)
font3 = pygame.font.Font(None, 64)
zet = 0
initbase = True
basehp = 2
plives = 3
plshoot = 1
shbonus = random.randint(300, 700)
rect = []
booms = []

class Base:
        def __init__(self, basehp):
                self.basehp = basehp
                initbase = False
        def destroy(self):
                if self.basehp == 0:
                        base = dbase


class Boom:
        def __init__(self, e_rectcenter):
                self.explosion = e
                self.e_rect = e_rect
                self.e_rect.center = e_rectcenter
                self.slide_rect = slide_rect
                self.ilolo = 0
                
        def render(self, screen):
                screen.blit(e, self.e_rect, self.slide_rect)
                
        def step(self):
                self.ilolo += 1
                self.slide_rect.x = (self.ilolo / 2) * 20
        def destroy(self):
                if self.ilolo > 7:
                        return True
                return False

class Bonus:
        def __init__(self, matrix):
                global bb,bl,bz
                self.type = random.randint(1, 3)
                if self.type == 1:
                        self.image = bb
                elif self.type == 2:
                        self.image = bl
                elif self.type == 3:
                        self.image = bz
                self.x = 0
                self.y = 0
                while matrix[self.y][self.x] != 0:
                        self.x = random.randint(1, 23)
                        self.y = random.randint(1, 23)
                self.rect = pygame.Rect((self.x*20,self.y*20),(20,20))
                        
        def render(self, screen):
                screen.blit(self.image, (self.x*20, self.y*20))

class Shoot:
        def __init__(self, pos1, pos2, orient, sight):
                self.x = pos1
                self.y = pos2
                self.orient = orient
                self.speed = 2
                self.damage = 15
                self.sight = sight
                self.rect = pygame.Rect(self.x*2+5,self.y*2+5,10,10)

        def step(self):
                if self.orient == 1:
                        self.y -= self.speed
                elif self.orient == 2:
                        self.y += self.speed
                elif self.orient == 3:
                        self.x -= self.speed
                elif self.orient == 4:
                        self.x += self.speed
                self.rect = pygame.Rect(self.x*2+5,self.y*2+5,10,10)

        def destroy(self, matrix):
                if self.orient == 1:
                        up = matrix[self.y / 10 +1][self.x / 10]
                        if up == 1:
                                booms.append(Boom((self.x*2+10, self.y*2+20)))
                                return True
                        elif up == 6:
                                booms.append(Boom((self.x*2+10, self.y*2+10)))
                                bbase.basehp -= 1
                                return True
                        elif up == 2:
                                matrix[self.y / 10 +1][self.x / 10] = 0
                                play.wall = 0
                                booms.append(Boom((self.x*2+10, self.y*2+10)))
                                return True
                        else:
                                return False
                elif self.orient == 2:
                        down = matrix[self.y / 10 ][self.x / 10]
                        if down == 1:
                                booms.append(Boom((self.x*2+10, self.y*2)))
                                return True
                        elif down == 6:
                                booms.append(Boom((self.x*2+10, self.y*2+10)))
                                bbase.basehp -= 1
                                return True
                        elif down == 2:
                                matrix[self.y / 10 ][self.x / 10] = 0
                                play.wall = 0
                                booms.append(Boom((self.x*2+10, self.y*2+10)))
                                return True
                        else:
                                return False
                elif self.orient == 3:
                        left = matrix[self.y / 10 ][self.x / 10 +1]
                        if left == 1:
                                booms.append(Boom((self.x*2+20, self.y*2+10)))
                                return True
                        elif left == 6:
                                booms.append(Boom((self.x*2+14, self.y*2+10)))
                                bbase.basehp -= 1
                                return True
                        elif left == 2:
                                matrix[self.y / 10][self.x / 10 +1] = 0
                                play.wall = 0
                                booms.append(Boom((self.x*2+14, self.y*2+10)))
                                return True
                        else:
                                return False
                elif self.orient == 4:
                        right = matrix[self.y / 10 ][self.x / 10 ]
                        if right == 1:
                                booms.append(Boom((self.x*2, self.y*2+10)))
                                return True
                        elif right == 6:
                                booms.append(Boom((self.x*2+10, self.y*2+10)))
                                bbase.basehp -= 1
                                return True
                        elif right == 2:
                                matrix[self.y / 10 ][self.x / 10 ] = 0
                                play.wall = 0
                                booms.append(Boom((self.x*2+10, self.y*2+10)))
                                return True
                        else:
                                return False



                
                        
        def render(self, screen):
                if self.orient == 1:
                        screen.blit(bullet1, (self.x*2, self.y*2))
                elif self.orient == 2:
                        screen.blit(bullet2, (self.x*2, self.y*2))
                elif self.orient == 3:
                        screen.blit(bullet3, (self.x*2, self.y*2))
                elif self.orient == 4:
                        screen.blit(bullet4, (self.x*2, self.y*2))


                        
                                
                                
                                
                

class Player:
        def __init__(self, pos1, pos2):
                self.ggx = pos1 * 10
                self.ggy = pos2 * 10
                self.orient = 1
                self.hp = 25
                self.lives = 3
                self.move = 0
                self.ggu = ggu
                self.ggd = pygame.transform.rotate(self.ggu, 180)
                self.ggl = pygame.transform.rotate(self.ggu, 90)
                self.ggr = pygame.transform.rotate(self.ggu, 270)
                self.gg = self.ggu
                self.wall = 0
                self.rect = pygame.Rect(self.ggx*2,self.ggy*2,20,20)
                self.power = 2

        def moveP(self, key):
                
                if self.orient == 1 and self.wall != 1:
                        if key == 1:
                                self.ggy -= 1
                                self.wall = 0
                        elif key != 0:
                                self.orient = key
                                self.move = 0
                        if (self.ggy % 10) == 0:
                                key = 0
                                self.move = 0
                                
                        elif key == 0:
                                self.ggy -= 1
                                self.move = 1
                                
                elif self.orient == 2 and self.wall != 2:
                        if key == 2:
                                self.ggy += 1
                                self.wall = 0
                        elif key != 0:
                                self.orient = key
                                self.move = 0
                        if (self.ggy % 10) == 0:
                                key = 0
                                self.move = 0
                                
                        elif key == 0:
                                self.ggy += 1
                                self.move = 1
                                
                elif self.orient == 3 and self.wall != 3:
                        if key == 3:
                                self.ggx -= 1
                                self.wall = 0
                        elif key != 0:
                                self.orient = key
                                self.move = 0
                        if (self.ggx % 10) == 0:
                                key = 0
                                self.move = 0
                                
                        elif key == 0:
                                self.ggx -= 1
                                self.move = 1
                                
                elif self.orient == 4 and self.wall != 4:
                        if key == 4:
                                self.ggx += 1
                                self.wall = 0
                        elif key != 0:
                                self.orient = key
                                self.move = 0
                        if (self.ggx % 10) == 0:
                                key = 0
                                self.move = 0
                                
                        elif key == 0:
                                self.ggx += 1
                                self.move = 1

                else: self.move = 0
                self.rect = pygame.Rect(self.ggx*2,self.ggy*2,20,20)
                        


        def walls(self, matrix):
                if (self.ggy % 10) == 0 and (self.ggx % 10) == 0:
                        Y_axisd = matrix[self.ggy / 10 + 1][self.ggx / 10]
                        Y_axisu = matrix[self.ggy / 10 - 1][self.ggx / 10]
                        X_axisr = matrix[self.ggy / 10][self.ggx / 10 + 1]
                        X_axisl = matrix[self.ggy / 10][self.ggx / 10 - 1]
                        if (Y_axisd == 1 or Y_axisd == 2 or Y_axisd == 4 or Y_axisd == 6) and self.orient == 2:
                                self.wall = 2
                        elif (Y_axisu == 1 or Y_axisu == 2 or Y_axisu == 4 or Y_axisu == 6) and self.orient == 1:
                                self.wall = 1
                        elif (X_axisr == 1 or X_axisr == 2 or X_axisr == 4 or X_axisr == 6) and self.orient == 4:
                                self.wall = 4
                        elif (X_axisl == 1 or X_axisl == 2 or X_axisl == 4 or X_axisl == 6) and self.orient == 3:
                                self.wall = 3
                        



        def render(self, screen):
                screen.blit(self.gg, (self.ggx*2, self.ggy*2))

        def touch(self, i):
                if self.orient == 1:
                        if (self.ggx == enemyes[i].x and self.ggy - 10 == enemyes[i].y):
                                self.wall = 1
                                return True
                        return False
                elif self.orient == 2:
                        if (self.ggx == enemyes[i].x and self.ggy + 10 == enemyes[i].y):
                                self.wall = 2
                                return True
                        return False
                elif self.orient == 3:
                        if (self.ggx - 10 == enemyes[i].x and self.ggy == enemyes[i].y):
                                self.wall = 3
                                return True
                        return False
                elif self.orient == 4:
                        if (self.ggx + 10 == enemyes[i].x and self.ggy == enemyes[i].y):
                                self.wall = 4
                                return True
                        return False


                


        
class Enemy:
        def __init__(self, tip, resp):
                self.orient = 2
                self.wall = 0
                self.shor = 0
                self.timer = 0
                self.k = 40
                self.lap = 0
                self.tip = tip
                self.resp = resp
                if self.tip == 1:
                        self.enu = enu
                        self.end = pygame.transform.rotate(self.enu, 180)
                        self.enl = pygame.transform.rotate(self.enu, 90)
                        self.enr = pygame.transform.rotate(self.enu, 270)
                        self.en = self.end
                        self.hp = 15
                elif self.tip == 2:
                        self.enu = enu2
                        self.end = pygame.transform.rotate(self.enu, 180)
                        self.enl = pygame.transform.rotate(self.enu, 90)
                        self.enr = pygame.transform.rotate(self.enu, 270)
                        self.en = self.end
                        self.hp = 30
                elif self.tip == 3:
                        self.enu = enu3
                        self.end = pygame.transform.rotate(self.enu, 180)
                        self.enl = pygame.transform.rotate(self.enu, 90)
                        self.enr = pygame.transform.rotate(self.enu, 270)
                        self.en = self.end
                        self.hp = 45
                if resp == 1:
                        self.x, self.y = 10, 10
                elif resp == 2:
                        self.x, self.y = 120, 10
                elif resp == 3:
                        self.x, self.y = 230, 10
                self.rect = pygame.Rect(self.x*2,self.y*2,20,20)

        def walls(self, matrix):
                if (self.y % 10) == 0 and (self.x % 10) == 0:
                        Y_axisd = matrix[self.y / 10 + 1][self.x / 10]
                        Y_axisu = matrix[self.y / 10 - 1][self.x / 10]
                        X_axisr = matrix[self.y / 10][self.x / 10 + 1]
                        X_axisl = matrix[self.y / 10][self.x / 10 - 1]
                        if (Y_axisd == 1 or Y_axisd == 2 or Y_axisd == 4 or Y_axisd == 6) and self.orient == 2:
                                self.wall = 2
                        elif (Y_axisu == 1 or Y_axisu == 2 or Y_axisu == 4 or Y_axisu == 6) and self.orient == 1:
                                self.wall = 1
                        elif (X_axisr == 1 or X_axisr == 2 or X_axisr == 4 or X_axisr == 6) and self.orient == 4:
                                self.wall = 4
                        elif (X_axisl == 1 or X_axisl == 2 or X_axisl == 4 or X_axisl == 6) and self.orient == 3:
                                self.wall = 3
                        else: self.wall = 0
        def move(self):
                if self.wall != self.orient and self.timer == 0:
                        self.shor +=1
                        if self.orient == 1:
                                self.en = self.enu
                                self.y -= 1
                        elif self.orient == 2:
                                self.en = self.end
                                self.y += 1
                        elif self.orient == 3:
                                self.en = self.enl
                                self.x -= 1
                        elif self.orient == 4:
                                self.en = self.enr
                                self.x += 1
                elif self.wall == self.orient and self.timer == 0:
                        if self.lap == 0:
                                if self.orient == 1:
                                        shoots.append(Shoot(self.x, self.y -4, self.orient, 0))
                                elif self.orient == 2:
                                        shoots.append(Shoot(self.x, self.y +4, self.orient, 0))
                                elif self.orient == 3:
                                        shoots.append(Shoot(self.x-4, self.y, self.orient, 0))
                                elif self.orient == 4:
                                        shoots.append(Shoot(self.x +4, self.y, self.orient, 0))
                                self.lap = 1
                        elif self.lap == 1:
                                oldor = self.orient
                                if oldor == 1:
                                        oldor2 = 2
                                elif oldor == 2:
                                        oldor2 = 1
                                elif oldor == 3:
                                        oldor2 = 4
                                else: oldor2 = 3
                                while self.orient == oldor:
                                        self.orient = random.randint(1, 4)
                                self.timer = 30
                                self.lap = 0
                        
                elif self.timer == 10:
                        if self.orient == 1:
                                self.en = self.enu
                        elif self.orient == 2:
                                self.en = self.end
                        elif self.orient == 3:
                                self.en = self.enl
                        elif self.orient == 4:
                                self.en = self.enr
                        self.timer -= 1
                else: self.timer -= 1
                if self.shor == 30 and self.wall == 0:
                        oldor = self.orient
                        if oldor == 1:
                                oldor2 = 2
                        elif oldor == 2:
                                oldor2 = 1
                        elif oldor == 3:
                                oldor2 = 4
                        else: oldor2 = 3
                        self.orient = random.randint(1, 4)
                        if oldor == self.orient or self.orient == oldor2:
                                pass
                        else:
                                self.timer = 30
                        self.shor =0
                self.rect = pygame.Rect(self.x*2,self.y*2,20,20)
                

                        

        def render(self, screen):
                screen.blit(self.en, (self.x*2, self.y*2))


        def enshoot(self):
                if self.k == 0:
                        if self.orient == 1:
                                shoots.append(Shoot(self.x, self.y -4, self.orient, 0))
                        elif self.orient == 2:
                                shoots.append(Shoot(self.x, self.y +4, self.orient, 0))
                        elif self.orient == 3:
                                shoots.append(Shoot(self.x-4, self.y, self.orient, 0))
                        elif self.orient == 4:
                                shoots.append(Shoot(self.x +4, self.y, self.orient, 0))
                        self.k = 50
                elif self.timer != 0:
                        pass
                else: self.k -= 1

                

        def touch(self):
                if play.orient == 1:
                        oldor2 = 2
                elif play.orient == 2:
                        oldor2 = 1
                elif play.orient == 3:
                        oldor2 = 4
                else: oldor2 = 3
                if self.orient == 1:
                        if self.x == play.ggx and self.y - 20 == play.ggy:
                                self.orient = oldor2
                                shoots.append(Shoot(self.x, self.y -4, self.orient, 0))
                                self.timer = 10
                                self.wall = 1
                elif self.orient == 2:
                        if self.x == play.ggx and self.y + 20 == play.ggy:
                                self.orient = oldor2
                                shoots.append(Shoot(self.x, self.y+4, self.orient, 0))
                                self.timer = 10
                                self.wall = 2
                elif self.orient == 3:
                        if self.x - 20 == play.ggx and self.y == play.ggy:
                                self.orient = oldor2
                                shoots.append(Shoot(self.x-4, self.y, self.orient, 0))
                                self.timer = 10
                                self.wall = 3
                elif self.orient == 4:
                        if self.x - 20 == play.ggx and self.y == play.ggy:
                                self.orient = oldor2
                                shoots.append(Shoot(self.x+4, self.y, self.orient, 0))
                                self.timer = 10
                                self.wall = 4
                
                


        



def pole(a):
        x = 0
        y = 0
        i = 0
        while i < 625:

                if a[y][x] == 0:
                        screen.blit(fs, (x*20, y*20))
                elif a[y][x] == 1:
                        screen.blit(beton, (x*20, y*20))
                elif a[y][x] == 2:
                        screen.blit(kir, (x*20, y*20))
                elif a[y][x] == 4:
                        screen.blit(water, (x*20, y*20))
                elif a[y][x] == 6:
                        screen.blit(base, (x*20, y*20))
                
                elif a[y][x] == 7:
                        screen.blit(fs, (x*20, y*20)) 
                x += 1
                if x > 24:
                        x = 0
                        y += 1
                i += 1


def poleFFF(a):
        x = 0
        y = 0
        i = 0
        while i < 625:

                if a[y][x] == 3:
                        screen.blit(forest, (x*20, y*20))

                x += 1
                if x > 24:
                        x = 0
                        y += 1
                i += 1



ggx = 9
ggy = 22
i = 0
shet = 0
enemyes = []
player = 1
player2 = 20
fight = 0
p2count = 20
kleo = 100
go = False
done = False
menu = font3.render(u'Новая игра', 1, (255, 255, 10))
menupos = pygame.Rect(365, 340,247,45)
menu2 = font3.render(u'Выход', 1, (255, 255, 10))
menupos2 = pygame.Rect(365, 400,154,45)
def mmenu(go):
        global menu, menu2,menupos,menupos2, done
        while not go:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                done = True
                                go = True
                        elif event.type == pygame.MOUSEMOTION:
                                if menupos2.collidepoint(event.pos):
                                        menu2 = font3.render(u'Выход', 1, (255, 0, 0))
                                        menu = font3.render(u'Новая игра', 1, (255, 255, 10))
                                        game = 2
                                elif menupos.collidepoint(event.pos):
                                        menu = font3.render(u'Новая игра', 1, (255, 0, 0))
                                        menu2 = font3.render(u'Выход', 1, (255, 255, 10))
                                        game = 1
                                else:
                                        menu = font3.render(u'Новая игра', 1, (255, 255, 10))
                                        menu2 = font3.render(u'Выход', 1, (255, 255, 10))
                                        game = 0
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                                if game == 1:
                                        go = True
                                        done = False
                                elif game == 2:
                                        go = True
                                        done = True
                screen.fill(color)
                screen.blit(back, (0, 0))
                screen.blit(menu, menupos)
                screen.blit(menu2, menupos2)
                pygame.display.flip()
mmenu(go)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                elif event.type == pygame.KEYDOWN:
                        
                        if event.key == pygame.K_LEFT and play.orient == 3 and play.wall != 3:
                                key = 3
                                enable = 1
                        elif event.key == pygame.K_RIGHT and play.orient == 4 and play.wall != 4:
                                key = 4
                                enable = 1
                        elif event.key == pygame.K_UP and play.orient == 1 and play.wall != 1:
                                key = 1
                                enable = 1
                        elif event.key == pygame.K_DOWN and play.orient == 2 and play.wall != 2:
                                key = 2
                                enable = 1
                        elif event.key == pygame.K_LEFT and play.orient != 3 and enable == 0 and play.move == 0:
                                play.orient = 3
                                play.gg = play.ggl
                        elif event.key == pygame.K_RIGHT and play.orient != 4 and enable == 0 and play.move == 0:
                                play.orient = 4
                                play.gg = play.ggr
                        elif event.key == pygame.K_UP and play.orient != 1 and enable == 0 and play.move == 0:
                                play.orient = 1
                                play.gg = play.ggu
                        elif event.key == pygame.K_DOWN and play.orient != 2 and enable == 0 and play.move == 0:
                                play.orient = 2
                                play.gg = play.ggd
                        elif event.key == pygame.K_SPACE:
                                if fight <= 0:
                                        shoots.append(Shoot(play.ggx, play.ggy, play.orient, 1))
                                        if play.power == 3:
                                                plshoot = 9
                                        elif play.power == 4:
                                                plshoot =19
                                        fight = 20
                                
                                
                                

                elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT and play.orient == 3:
                                key = 0
                                enable = 0
                        elif event.key == pygame.K_RIGHT and play.orient == 4:
                                key = 0
                                enable = 0
                        elif event.key == pygame.K_UP and play.orient == 1:
                                key = 0
                                enable = 0
                        elif event.key == pygame.K_DOWN and play.orient == 2:
                                key = 0
                                enable = 0

        #ilolo += 1
        #slide_rect.x = (ilolo / 2) * 20
        fight -= 1


        if initbase == True:
                bbase = Base(basehp)
                initbase = False
                        

        if plshoot  == 5:
                shoots.append(Shoot(play.ggx, play.ggy, play.orient, 1))
                plshoot = 1
        elif plshoot == 10:
                shoots.append(Shoot(play.ggx, play.ggy, play.orient, 1))
                plshoot -= 1
        elif plshoot == 1:
                pass
        else: plshoot -= 1


       
        
        if player == 1:
                player -=1
                play = Player(ggx,ggy)
                
        play.moveP(key)
        play.walls(matrix)
        
        if player2 > 0:
                if len(enemyes) < 4:
                        if shet ==0:
                                player2 -=1
                                respoun = random.randint(1, 3)
                                tip = random.randint(1, 3)
                                qwerty = Enemy(tip,respoun)
                                enemyes.append(qwerty)
                                shet = 100
                        shet -=1

        

        for enemy in enemyes:
                enemy.walls(matrix)
                enemy.enshoot()
                enemy.move()
                enemy.walls(matrix)

        
        
        
        if shbonus == 0:
                bonuses.append(Bonus(matrix))
                shbonus = random.randint(300, 700)
        else:
                shbonus -= 1



        m1m =0
        while m1m < len(shoots):
                m2m = 0
                while m2m < len(shoots):
                        dx = shoots[m2m].x - shoots[m1m].x
                        dy = shoots[m2m].y - shoots[m1m].y
                        if dx < 0:
                                dx = -dx
                        if dy < 0:
                                dy = -dy
                        if shoots[m2m].sight == shoots[m1m].sight:
                                pass
                        elif (shoots[m2m].x == shoots[m1m].x and shoots[m2m].y == shoots[m1m].y) or (dx < 3 and dy < 3):
                                booms.append(Boom((shoots[m1m].x*2+10, shoots[m1m].y*2+10)))
                                shoots.pop(m2m)
                                shoots.pop(m1m)
                                
                        m2m += 1
                m1m += 1


        fps = (str((float(int(clock.get_fps()*10))/10)))
        fps2 = 'fps: ' + fps
        
        text = font.render(fps2, 1, (255, 255, 10))
        textpos = text.get_rect()
        textpos = (510, 30)
        
        text2 = font2.render(u'Осталось врагов: ' + str(p2count), 1, (255, 255, 10))
        textpos2 = text2.get_rect()
        textpos2 = (510, 60)

        text3 = font3.render(u'Вы победили!', 1, (255, 10, 10))
        textpos3 = text3.get_rect(centerx=(screen.get_width()-140)/2,centery=screen.get_height()/2)
        text4 = font.render(u'Уровень: ' + str(level + 1), 1, (255, 255, 10))
        textpos4 = text4.get_rect()
        textpos4 = (510, 5)
        text5 = font3.render(u'Вы проиграли!', 1, (255, 10, 10))
        textpos5 = text5.get_rect(centerx=(screen.get_width()-140)/2,centery=screen.get_height()/2)

        text9 = font3.render(u'Вы прошли игру!', 1, (255, 10, 10))
        textpos9 = text5.get_rect(centerx=(screen.get_width())/2,centery=screen.get_height()/2)


        text6 = font2.render(u'Уровень игрока: ' + str(play.power - 1), 1, (255, 255, 10))
        textpos6 = text2.get_rect()
        textpos6 = (510, 80)

        text7 = font2.render(u'Здоровье игрока: ' + str(play.hp), 1, (255, 255, 10))
        textpos7 = text2.get_rect()
        textpos7 = (510, 100)

        text8 = font2.render(u'Жизни игрока: ' + str(plives), 1, (255, 255, 10))
        textpos8 = text2.get_rect()
        textpos8 = (510, 120)


        for i in reversed(range(0, len(enemyes))):
                for k in reversed(range(0, len(shoots))):
                        if shoots[k].sight == 0:
                                pass
                        else:
                                if enemyes[i].rect.colliderect(shoots[k].rect):
                                        enemyes[i].hp -= 15
                                        booms.append(Boom((shoots[k].rect.center)))
                                        shoots.pop(k)
                                        if enemyes[i].hp <= 0:
                                                enemyes.pop(i)
                                                i-=1
                                                p2count -= 1


        for i in reversed(range(0, len(enemyes))):
                for k in reversed(range(0, len(bonuses))):
                        if enemyes[i].rect.colliderect(bonuses[k].rect):
                                        bonuses.pop(k)


        for i in reversed(range(0, len(shoots))):
                if shoots[i].sight == 1:
                        pass
                else:
                        if play.rect.colliderect(shoots[i].rect):
                                play.hp -=15
                                booms.append(Boom((shoots[i].rect.center)))
                                shoots.pop(i)
                                if play.hp < 0:
                                        booms.append(Boom((play.rect.center)))
                                        zet = 1
                                        plives -= 1


        for k in reversed(range(0, len(bonuses))):
                if play.rect.colliderect(bonuses[k].rect):
                        if bonuses[k].type == 1:
                                for i in reversed(range(0, len(enemyes))):
                                        booms.append(Boom((enemyes[i].rect.center)))
                                        enemyes.pop(i)
                                        counten += 1
                                p2count -= counten
                                counten = 0
                                bonuses.pop(k)
                        elif bonuses[k].type == 2:
                                matrix[23][11] = 1
                                matrix[23][13] = 1
                                matrix[22][11] = 1
                                matrix[22][13] = 1
                                matrix[22][12] = 1
                                bonuses.pop(k)
                                lopatka = 1
                                lopatka_s = 300
                        elif bonuses[k].type == 3:
                                bonuses.pop(k)
                                play.power += 1
                                if play.power > 4:
                                        play.power = 4
                                play.hp += 5
                                

                
        if lopatka == 1:
                if lopatka_s == 0:
                        matrix[23][11] = 2
                        matrix[23][13] = 2
                        matrix[22][11] = 2
                        matrix[22][13] = 2
                        matrix[22][12] = 2
                        lopatka = 0
                else: lopatka_s -= 1
        for i in reversed(range(0, len(booms))):
                booms[i].step()
                if booms[i].destroy():
                        booms.pop(i)

        for i in reversed(range(0, len(enemyes))):
                Rect = play.rect
                if Rect.colliderect(enemyes[i].rect):
                        if play.power > enemyes[i].tip:
                                booms.append(Boom((enemyes[i].rect.center)))
                                enemyes.pop(i)
                                p2count -= 1
                        elif play.power <= enemyes[i].tip:
                                if zet == 0:
                                        booms.append(Boom((play.rect.center)))
                                        plives -= 1
                                        zet = 1
                                
                
        for i in reversed(range(0, len(shoots))):
                shoots[i].step()
                if shoots[i].destroy(matrix):
                        shoots.pop(i)
                        

        if zet != 0 and plives > 0:
                if zet == 20:
                        play = Player(ggx,ggy)
                        zet = 0
                else: zet += 1
                    
        if bbase.basehp == 0:
                base = dbase
        
                                
        screen.fill(color)
        pygame.draw.rect(screen, color2, (0,0,500,500), 5)
        pole(matrix)
        for enemy in enemyes:
                enemy.render(screen)
        if zet == 0:
                play.render(screen)
        for shoot in shoots:
                shoot.render(screen)
        for bonus in bonuses:
                bonus.render(screen)
        for boom in booms:
                boom.render(screen)
        poleFFF(matrix)
        screen.blit(text, textpos)
        screen.blit(text2, textpos2)
        screen.blit(text4, textpos4)
        screen.blit(text6, textpos6)
        screen.blit(text7, textpos7)
        screen.blit(text8, textpos8)
        if p2count == 0:
                screen.blit(text3, textpos3)
                if reloads != 0:
                        reloads -= 1
                else:
                        time.sleep(1)
                        p2count = 20
                        player2 = 20
                        for k in reversed(range(0, len(bonuses))):
                                bonuses.pop(k)
                        level += 1
                        if level == 3:
                                screen.fill((0,0,0))
                                screen.blit(text9, textpos9)
                                if reloads != 0:
                                        reloads -= 1
                                else:
                                        time.sleep(1)
                                        reloads = 60
                                        go = False
                                        done = True
                        else:
                                matrix = levels.lev[level]
                        reloads = 60
                        shbonus = random.randint(300, 700)
                        enable = 0
                        powerp = play.power
                        play = 0
                        play = Player(ggx,ggy)
                        play.power = powerp
                        
                
        elif bbase.basehp < 1 or plives < 1:
                screen.blit(text5, textpos5)
                if reloads != 0:
                        reloads -= 1
                else:
                        time.sleep(1)
                        reloads = 60
                        go = False
                        done = True

        

        pygame.display.flip()
        clock.tick(30)
