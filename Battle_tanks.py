# -*- coding: cp1251 -*-
import pygame
import random
import time
import math

pygame.init()
size = 640,500
screen = pygame.display.set_mode(size, pygame.DOUBLEBUF | pygame.HWSURFACE)
pygame.display.set_caption('Battle Tanks')

color = 0, 0, 0
color2 = 0, 255, 0

fs = pygame.image.load('fs.png')
kir = pygame.image.load('kir.png')
beton = pygame.image.load('beton.png')
forest = pygame.image.load('forest2.png')
base = pygame.image.load('base.png')
water = pygame.image.load('water.png')
bullet1 = pygame.image.load('ammo1.png')
bullet2 = pygame.image.load('ammo2.png')
bullet3 = pygame.image.load('ammo3.png')
bullet4 = pygame.image.load('ammo4.png')
gg = pygame.image.load('ggu.png')
ggu = pygame.image.load('ggu.png')
ggd = pygame.image.load('ggd.png')
ggl = pygame.image.load('ggl.png')
ggr = pygame.image.load('ggr.png')
explosion = pygame.image.load('e.png')
e_rect = explosion.get_rect()
e_rect.width = e_rect.height
slide_rect = explosion.get_rect()
slide_rect.width = slide_rect.height



ii=0
orient = 1
move = 0
matrix =  [
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
           [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 1, 2, 0, 2, 2, 0, 0, 7, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 6, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]


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

rect = []
boom = []
class Explosion:
        def __init__(self, e_rectcenter, explosion):
                self.explosion = explosion
                self.e_rect = e_rect
                self.e_rect.center = e_rectcenter
                self.slide_rect = slide_rect
                self.ilolo = 0
        def render(self,screen):
                screen.blit(self.explosion, self.e_rect, self.slide_rect)
        def step(self):
                self.ilolo += 1
                self.slide_rect.x = (ilolo / 2) * 20
        def destroy(self):
                if self.ilolo > 6:
                        return True
                return False
                
enemies = 1

class Shoot:
        def __init__(self, pos1, pos2, orient):
                self.x = pos1
                self.y = pos2
                self.orient = orient
                self.speed = 2
                self.damage = 15

        def step(self):
                if self.orient == 1:
                        self.y -= self.speed
                elif self.orient == 2:
                        self.y += self.speed
                elif self.orient == 3:
                        self.x -= self.speed
                elif self.orient == 4:
                        self.x += self.speed

        def destroy(self, matrix):
                if self.orient == 1:
                        up = matrix[self.y / 10 +1][self.x / 10]
                        if up == 1 or up == 6:
                                return True
                        elif up == 2:
                                matrix[self.y / 10 +1][self.x / 10] = 0
                                play.wall = 0
                                return True
                        else:
                                return False
                elif self.orient == 2:
                        down = matrix[self.y / 10 ][self.x / 10]
                        if down == 1 or down == 6:
                                return True
                        elif down == 2:
                                matrix[self.y / 10 ][self.x / 10] = 0
                                play.wall = 0
                                return True
                        else:
                                return False
                elif self.orient == 3:
                        left = matrix[self.y / 10 ][self.x / 10 +1]
                        if left == 1 or left == 6:
                                return True
                        elif left == 2:
                                matrix[self.y / 10][self.x / 10 +1] = 0
                                play.wall = 0
                                return True
                        else:
                                return False
                elif self.orient == 4:
                        right = matrix[self.y / 10 ][self.x / 10 ]
                        if right == 1 or right == 6:
                                return True
                        elif right == 2:
                                matrix[self.y / 10 ][self.x / 10 ] = 0
                                play.wall = 0
                                return True
                        else:
                                return False


        def dindestroy(self,enemyes):
                if enemyes.x == self.x and enemyes.y == self.y:
                        enemyes.hp -= self.damage
                        return True
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
        def __init__(self, pos1, pos2, gg, ggu, ggd, ggr, ggl):
                self.ggx = pos1 * 10
                self.ggy = pos2 * 10
                self.orient = 1
                self.hp = 50
                self.lives = 3
                self.move = 0
                self.gg = gg
                self.ggu = ggu
                self.ggd = ggd
                self.ggl = ggl
                self.ggr = ggr
                self.wall = 0

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
                        if (self.ggx == enemyes[i].x and self.ggy - 20 == enemyes[i].y):
                                self.wall = 1
                                return True
                        return False
                elif self.orient == 2:
                        if (self.ggx == enemyes[i].x and self.ggy + 20 == enemyes[i].y):
                                self.wall = 2
                                return True
                        return False
                elif self.orient == 3:
                        if (self.ggx - 20 == enemyes[i].x and self.ggy == enemyes[i].y):
                                self.wall = 3
                                return True
                        return False
                elif self.orient == 4:
                        if (self.ggx + 20 == enemyes[i].x and self.ggy == enemyes[i].y):
                                self.wall = 4
                                return True
                        return False


                


        
class Enemy:
        def __init__(self, ggu, ggd, ggr, ggl, tip, resp):
                #self.x = pos1
                #self.y = pos2
                self.orient = 2
                self.en = ggd
                self.enu = ggu
                self.end = ggd
                self.enl = ggl
                self.enr = ggr
                self.wall = 0
                self.shor = 0
                self.timer = 0
                self.k = 40
                self.tip = tip
                self.resp = resp
                if self.tip == 1:
                        self.hp = 15
                elif self.tip == 2:
                        self.hp = 30
                elif self.tip == 3:
                        self.hp = 45
                if resp == 1:
                        self.x, self.y = 10, 10
                elif resp == 2:
                        self.x, self.y = 120, 10
                elif resp == 3:
                        self.x, self.y = 230, 10

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
                elif self.wall == self.orient:
                        oldor = self.orient
                        if oldor == 1:
                                oldor2 = 2
                        elif oldor == 2:
                                oldor2 = 1
                        elif oldor == 3:
                                oldor2 = 4
                        else: oldor2 = 3
                        while self.orient == oldor or self.orient == oldor2:
                                self.orient = random.randint(1, 4)
                        self.timer = 10
                else: self.timer -= 1
                if self.shor == 50 and self.wall == 0:
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
                                self.timer = 10
                        self.shor =0
                

                        

        def render(self, screen):
                screen.blit(self.en, (self.x*2, self.y*2))


        def enshoot(self):
                if self.k == 0:
                        if self.orient == 1:
                                shoots.append(Shoot(self.x, self.y -4, self.orient))
                        elif self.orient == 2:
                                shoots.append(Shoot(self.x, self.y +4, self.orient))
                        elif self.orient == 3:
                                shoots.append(Shoot(self.x-4, self.y, self.orient))
                        elif self.orient == 4:
                                shoots.append(Shoot(self.x +4, self.y, self.orient))
                        self.k = 100
                elif self.timer != 0:
                        pass
                else: self.k -= 1

                
        def destroy(self,i):
                if enemyes[i].x == play.ggx and enemyes[i].y == play.ggy:
                        return True
                return False

        def touch(self):
                if self.orient == 1:
                        if self.x == play.ggx and self.y - 10 == play.ggy:
                                self.wall = 1
                elif self.orient == 2:
                        if self.x == play.ggx and self.y + 10 == play.ggy:
                                self.wall = 2
                elif self.orient == 3:
                        if self.x - 10 == play.ggx and self.y == play.ggy:
                                self.wall = 3
                elif self.orient == 4:
                        if self.x - 10 == play.ggx and self.y == play.ggy:
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
                #elif a[y][x] == 3:
                #        screen.blit(forest, (x*20, y*20))
                elif a[y][x] == 4:
                        screen.blit(water, (x*20, y*20))
                elif a[y][x] == 6:
                        screen.blit(base, (x*20, y*20))
                
                elif a[y][x] == 7:
                        screen.blit(fs, (x*20, y*20)) # начальные координаты танка
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



done = False
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
                                        shoots.append(Shoot(play.ggx, play.ggy, play.orient))
                                        fight = 50
                                
                                
                                

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

        if betas < 20:
                betas += 1
        else:        
                #shoots.append(Shoot(190, 190, 1))
                
                betas = 0
#
        #if enemies > 0:
        #        enemi.append(Enemy(19.0, 3.0))
        #        enemies -=1

                        

        
        if player == 1:
                player -=1
                play = Player(ggx,ggy,gg,ggu,ggd,ggr,ggl)
        play.moveP(key)
        play.walls(matrix)
        

        if player2 > 0:
                if shet == 0:
                        player2 -=1
                        respoun = random.randint(1, 3)
                        qwerty = Enemy(ggu,ggd,ggr,ggl,1,respoun)
                        enemyes.append(qwerty)
                        shet = 100
                shet -=1

        
        for i in reversed(range(0, len(enemyes))):
                
                if enemyes[i].destroy(i):
                        enemyes.pop(i)
        for enemy in enemyes:
                enemy.walls(matrix)
                enemy.enshoot()
                #enemy.touch()
                enemy.move()

        
        
        



        #if orient == 1: это вроде проверка патронов на совпадение)))
        #        for i in reversed(range(0, len(ammos1))):
        #                k = 0
        #                while k < len(ammos2):
        #                        a, b = ammos1[i].pdestroy(), ammos2[k].pdestroy()
        #                        a = math.ceil(a[0]), math.ceil(a[1])
        #                        b = math.ceil(b[0]), math.ceil(b[1]+1)
        #                        if a[1] > b[1]:
        #                                if a[1] == b[1] and (a[0] == b[0] or -1 >= (a[0] - b[0]) <= 1):
        #                                        ammos1.pop(i)
        #                                        ammos2.pop(k)
        #                                        e_rect.center = a[1]*20-10, a[0]*20+10
        #                                        ilolo = 0
        #                        k+=1



        for i in reversed(range(0, len(shoots))):
                shoots[i].step()
                if shoots[i].destroy(matrix):
                        #boom.append(Explosion(((boom[i].x) + 10, (boom[i].y) + 10), explosion))
                        shoots.pop(i)


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
                        if shoots[m2m] == shoots[m1m]:
                                pass
                        elif (shoots[m2m].x == shoots[m1m].x and shoots[m2m].y == shoots[m1m].y) or (dx < 3 and dy < 3):
                                shoots.pop(m2m)
                                shoots.pop(m1m)
                        m2m += 1
                m1m += 1

        m1m = len(shoots) -1
        while m1m > 0:
                m2m = len(enemyes)-1
                while m2m > 0:
                        #if shoots[m1m] == 0:
                        #        pass
                        #else:
                        dx = shoots[m1m].x - enemyes[m2m].x
                        dy = shoots[m1m].y - enemyes[m2m].y
                        if dx < 0:
                                dx = -dx
                        if dy < 0:
                                dy = -dy
                        if (shoots[m1m].x == enemyes[m2m].x and shoots[m1m].y == enemyes[m2m].y) or (dx < 3 and dy < 3):
                                enemyes[m2m].hp -= 15
                                shoots.pop(m1m)
                                #m1m -= 1
                                m1m = len(shoots) -1
                                if enemyes[m2m].hp <= 0:
                                        enemyes.pop(m2m)

                        m2m -= 1
                m1m -= 1
                      
                

        for i in reversed(range(0, len(boom))):
                boom[i].step()
                if boom[i].destroy():
                        boom.pop(i)

                        
        
        #for i in reversed(range(0, len(enemi))):
         #       enemi[i].move(matrix)
                
            
                    
        #for shoot in shoots:
                #shoot.delshoots()
                                
        screen.fill(color)
        pygame.draw.rect(screen, color2, (0,0,500,500), 5)
        pole(matrix)
        #screen.blit(gg, (ggx*20, ggy*20))
        #for Enemy in enemi:
        #        Enemy.render(screen)
        for enemy in enemyes:
                enemy.render(screen)
        play.render(screen)
        for shoot in shoots:
                shoot.render(screen)
        for explosion in shoots:
                explosion.render(screen)
        poleFFF(matrix)
        
        #screen.blit(explosion, e_rect, slide_rect)
        
        

        pygame.display.flip()

        time.sleep(0.025)

        
