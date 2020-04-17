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




orient = 1
move = 0
matrix =  [
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 3, 3, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 3, 3, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
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
def pole__BETA(a):
        x = 0
        y = 0
        i = 0
        p = 0
        while i < 625:
                if matrix[i] == 1:
                        screen.blit(kir, (x, y))
                        i += 1
                        p += 1
                elif matrix[i] == 0:
                        screen.blit(fs, (x, y))
                        i += 1
                        p += 1
                x +=20
                if p == 25:
                        y += 20
                        p = 0
                        x = 0

betas = 0
x = 0
y = 0
a = matrix
shoot = 0
fly = 0
ilolo = 118
ammos1 = []
ammos2 = []
ammos3 = []
ammos4 = []
gmove = 0
vermove = 0

class Ammo1:
        def __init__(self, pos1, pos2):
                self.amggx, self.amggy = pos1, pos2
                self.d = 0.5
        def step(self):
                self.amggy -= self.d      
        def render(self, screen):
                screen.blit(bullet1, (self.amggx*20, self.amggy*20))
        def destroy(self, matrix):
                per = matrix[int(math.ceil(self.amggy)-1)][int(math.ceil(self.amggx)-1)]
                per2 = matrix[int(math.ceil(self.amggy)-1)][int(math.ceil(self.amggx))]
                if gmove == 0:
                        perist = per2
                else:
                        perist = per
                if perist == 1:
                        e_rect.center = self.amggx*20 + 10, self.amggy*20
                        self.amggy -= self.d
                        return True
                elif perist == 2:
                        
                        if ste == 1:
                                e_rect.center = self.amggx*20 + 10, self.amggy*20
                                if gmove == 0:
                                        matrix[int(math.ceil(self.amggy)-1)][int(math.ceil(self.amggx))] =0
                                else:
                                        matrix[int(math.ceil(self.amggy)-1)][int(math.ceil(self.amggx)-1)] = 0
                                   
                                
                        else:
                                e_rect.center = self.amggx*20 + 10, self.amggy*20-10
                                self.amggy -= self.d
                                if gmove == 0:
                                        matrix[int(math.ceil(self.amggy)-1)][int(math.ceil(self.amggx))] =0
                                else:
                                        matrix[int(math.ceil(self.amggy)-1)][int(math.ceil(self.amggx)-1)] = 0

                        return True
                return False
        def pdestroy(self):
                a = self.amggy
                b = self.amggx
                return a, b
                                
                                
                                

class Ammo2:
        def __init__(self, pos1, pos2):
                self.amggx, self.amggy = pos1, pos2
                self.d = 0.5
        def step(self):
                self.amggy += self.d      
        def render(self, screen):
                screen.blit(bullet2, (self.amggx*20, self.amggy*20))
        def destroy(self, matrix):
                per = matrix[int(math.ceil(self.amggy)-1)][int(math.ceil(self.amggx)-1)]
                per2 = matrix[int(math.ceil(self.amggy)-1)][int(math.ceil(self.amggx))]
                if gmove == 0:
                        perist = per2
                else:
                        perist = per
                if perist == 1:
                        e_rect.center = self.amggx*20 + 10, self.amggy*20 - 10
                        self.amggy += self.d
                        return True
                elif perist == 2:
                        
                        if ste == 2:
                                e_rect.center = self.amggx*20 + 10, self.amggy*20
                                if gmove == 0:
                                        matrix[int(math.ceil(self.amggy)-1)][int(math.ceil(self.amggx))] =0
                                else:
                                        matrix[int(math.ceil(self.amggy)-1)][int(math.ceil(self.amggx)-1)] = 0
                                   
                                
                        else:
                                e_rect.center = self.amggx*20 + 10, self.amggy*20
                                self.amggy += self.d
                                if gmove == 0:
                                        matrix[int(math.ceil(self.amggy)-1)][int(math.ceil(self.amggx))] =0
                                else:
                                        matrix[int(math.ceil(self.amggy)-1)][int(math.ceil(self.amggx)-1)] = 0

                        return True
                return False
        def pdestroy(self):
                a = self.amggy
                b = self.amggx
                return a,  b
        
class Ammo3: 
        def __init__(self, pos1, pos2):
                self.amggx, self.amggy = pos1, pos2
                self.d = 0.5
        def step(self):
                self.amggx -= self.d      
        def render(self, screen):
                screen.blit(bullet3, (self.amggx*20, self.amggy*20))
        def destroy(self, matrix):
                _3per = matrix[int(math.ceil(self.amggy))][int(math.ceil(self.amggx)-1)]
                _3per2 = matrix[int(math.ceil(self.amggy))][int(math.ceil(self.amggx)-1)]
                if vermove == 0:
                        _3perist = _3per2
                else:
                        _3perist = _3per
                if _3perist == 1:
                        if gmove == 1:
                                e_rect.center = self.amggx*20 + 10  , self.amggy*20 + 10
                        else: e_rect.center = self.amggx*20  , self.amggy*20 + 10
                        self.amggx -= self.d
                        return True
                elif _3perist == 2:
                        
                        if ste == 3:
                                e_rect.center = self.amggx*20 , self.amggy*20 + 10
                                if gmove == 0:
                                        matrix[int(math.ceil(self.amggy))][int(math.ceil(self.amggx)-1)] =0
                                else:
                                        matrix[int(math.ceil(self.amggy))][int(math.ceil(self.amggx)-1)] = 0
                                   
                                
                        else:
                                
                                if gmove == 0:
                                        e_rect.center = self.amggx*20 -10, self.amggy*20+10
                                        matrix[int(math.ceil(self.amggy))][int(math.ceil(self.amggx)-1)] =0
                                else:
                                        e_rect.center = self.amggx*20 , self.amggy*20+10
                                        matrix[int(math.ceil(self.amggy))][int(math.ceil(self.amggx)-1)] = 0

                        return True
                return False

class Ammo4:
        def __init__(self, pos1, pos2):
                self.amggx, self.amggy = pos1, pos2
                self.d = 0.5
        def step(self):
                self.amggx += self.d      
        def render(self, screen):
                screen.blit(bullet4, (self.amggx*20, self.amggy*20))
        def destroy(self, matrix):
                _3per = matrix[int(math.ceil(self.amggy))][int(math.ceil(self.amggx)-1)]
                _3per2 = matrix[int(math.ceil(self.amggy))][int(math.ceil(self.amggx)-1)]
                if vermove == 0:
                        _3perist = _3per2
                else:
                        _3perist = _3per
                if _3perist == 1:
                        if gmove == 1:
                                e_rect.center = self.amggx*20   , self.amggy*20 + 10
                        else: e_rect.center = self.amggx*20 -10 , self.amggy*20 + 10
                        self.amggx -= self.d
                        return True
                elif _3perist == 2:
                        
                        if ste == 3:
                                e_rect.center = self.amggx*20 , self.amggy*20 + 10
                                if gmove == 0:
                                        matrix[int(math.ceil(self.amggy))][int(math.ceil(self.amggx)-1)] =0
                                else:
                                        matrix[int(math.ceil(self.amggy))][int(math.ceil(self.amggx)-1)] = 0
                                   
                                
                        else:
                                
                                if gmove == 0:
                                        e_rect.center = self.amggx*20, self.amggy*20 + 10
                                        matrix[int(math.ceil(self.amggy))][int(math.ceil(self.amggx)-1)] =0
                                else:
                                        e_rect.center = self.amggx*20+ 10 , self.amggy*20+10
                                        matrix[int(math.ceil(self.amggy))][int(math.ceil(self.amggx)-1)] = 0

                        return True
                return False
        
                


        





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



ggx = 9.
ggy = 22.
iggx = 9
iggy = 22
shgg = 0
dggx = 0
diggy = 0
firstor = 1
mk = 2
i = 0
dog = 0
ste = 0


        #screen.blit(gg, (ggx*20, ggy*20))




done = False
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                elif event.type == pygame.KEYDOWN:
                        
                        if event.key == pygame.K_LEFT and move == 0 and orient == 3 and ste != 3:
                                #ggx -= 1
                                gg = ggl
                                orient = 3
                                move = 1
                                mk = True
                                gmove = 1
                                
                        elif event.key == pygame.K_RIGHT and move == 0 and orient == 4 and ste != 4:
                                #ggx += 1
                                gg = ggr
                                orient = 4
                                move = 1
                                mk = True
                                gmove = 1
                        elif event.key == pygame.K_UP and move == 0 and orient == 1 and ste != 1:
                                #ggy -= 1
                                gg = ggu
                                orient = 1
                                move = 1
                                mk = True
                                vermove = 1
                        elif event.key == pygame.K_DOWN and move == 0 and orient == 2 and ste != 2:
                                #ggy += 1
                                gg = ggd
                                orient = 2
                                move = 1
                                mk = True
                                vermove = 1
                        elif event.key == pygame.K_LEFT and move == 0 and orient != 3 and dog == 0:
                                #ggx -= 1
                                gg = ggl
                                orient = 3
                                move = 0
                                
                        elif event.key == pygame.K_RIGHT and move == 0 and orient != 4 and dog == 0:
                                #ggx += 1
                                gg = ggr
                                orient = 4
                                move = 0
                        elif event.key == pygame.K_UP and move == 0 and orient != 1 and dog == 0:
                                #ggy -= 1
                                gg = ggu
                                orient = 1
                                move = 0
                        elif event.key == pygame.K_DOWN and move == 0 and orient != 2 and dog == 0:
                                #ggy += 1
                                gg = ggd
                                orient = 2
                                move = 0
                        elif event.key == pygame.K_SPACE:
                                if orient == 1:
                                        ammos1.append(Ammo1(ggx, ggy))
                                elif orient == 2:
                                        ammos2.append(Ammo2(ggx, ggy))
                                elif orient == 3:
                                        ammos3.append(Ammo3(ggx, ggy))
                                elif orient == 4:
                                        ammos4.append(Ammo4(ggx, ggy))
                                

                elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT and move == 1 and orient == 3:
                                #ggx -= 1
                                gg = ggl
                                orient = 3
                                move = 0
                                mk = False
                                dog = 1
                        elif event.key == pygame.K_RIGHT and move == 1 and orient == 4:
                                #ggx += 1
                                gg = ggr
                                orient = 4
                                move = 0
                                dog = 1
                                mk = False
                        elif event.key == pygame.K_UP and move == 1 and orient == 1:
                                #ggy -= 1
                                gg = ggu
                                orient = 1
                                move = 0
                                dog = 1
                                mk = False
                        elif event.key == pygame.K_DOWN and move == 1 and orient == 2:
                                #ggy += 1
                                gg = ggd
                                orient = 2
                                move = 0
                                dog = 1
                                mk = False
                        #elif event.key == pygame.K_SPACE:
                        #        shoot = 0
        ilolo += 1
        slide_rect.x = (ilolo / 2) * 20
        

        if betas < 20:
                betas += 1
        else:        
                ammos1.append(Ammo1(19, 19))
                betas = 0

        

                        

        left = matrix[int(math.ceil(ggy))][int(math.ceil(ggx) - 2)]
        right = matrix[int(math.ceil(ggy))][int(math.ceil(ggx))]
        if gmove == 0:
                up = matrix[int(math.ceil(ggy) - 1)][int(math.ceil(ggx) - 0)]
        else:
                up = matrix[int(math.ceil(ggy) - 1)][int(math.ceil(ggx) - 1)]
        down = matrix[int(math.ceil(ggy) + 1)][int(math.ceil(ggx) -1)]
                        
                        
        if (left == 1  or left == 2 or left == 4 or left == 6) and orient == 3:
                mk = False
                move = 0
                ste = 3
        elif (right == 1 or right == 2 or right == 4 or  right == 6) and orient == 4:
                mk = False
                move = 0
                ste = 4
        elif (up == 1 or up == 2  or up == 4 or up == 6) and orient == 1:
                mk = False
                move = 0
                ste = 1
        elif (down == 1 or down == 2  or down == 4 or down == 6) and orient == 2:
                mk = False
                move = 0
                ste = 2

        






        if move == 1 and orient == 3 and mk == True:
                ggx -= 0.1
                ste = 0
                
                
                

                
                

        elif move == 0 and orient == 3 and mk == False:
                int_ggx = math.ceil(ggx) - 1
                rasdot = int((ggx - int_ggx) * 10)

                if rasdot == 0:
                        mk = True
                        dog = 0
                        
                        
                else:
                        ggx -= 0.1
                        rasdot -= 1
                

                
                
                                
                        
        elif move == 1 and orient == 4 and mk == True:
                ste = 0
                ggx += 0.1

                
                 
                
        elif move == 0 and orient == 4 and mk == False:
                int_ggx = math.ceil(ggx) - 1
                rasdot = int((ggx - int_ggx) * 10)
                
                if rasdot == 0:
                        mk = True
                        dog = 0
                        
                        
                else:
                        ggx += 0.1
                        rasdot -= 1
                



                                
        elif move == 1 and orient == 1 and mk == True:
                ggy += -0.1
                ste = 0
        

        elif move == 0 and orient == 1 and mk == False:
                int_ggy = math.ceil(ggy)
                rasdot = int((ggy - int_ggy) * 10)
                
                if rasdot == 0:
                        mk = True
                        dog = 0
                        
                        
                else:
                        ggy -= 0.1
                        rasdot -= 1
                
                
        elif move == 1 and orient == 2 and mk == True:
                ggy += 0.1
                ste = 0
                

        elif move == 0 and orient == 2 and mk == False:
                int_ggy = math.ceil(ggy) 
                rasdot = int((ggy - int_ggy) * 10)
                
                if rasdot == 0:
                        mk = True
                        dog = 0
                        
                        
                else:
                        ggy += 0.1
                        rasdot -= 1

        

        for i in reversed(range(0, len(ammos1))):
                ammos1[i].step()
                #ammos1[i].pdestroy(ammos2)
                #print ammos1[i].pdestroy()
                #if ammos1[i].pdestroy() == ammos1[i].pdestroy():
                 #       ammos1.pop(i)
                 #       ammos2.pop(i)
                if ammos1[i].destroy(matrix):
                        ammos1.pop(i)
                        ilolo = 0
                        ste = 0

        if orient == 1:
                for i in reversed(range(0, len(ammos1))):
                        k = 0
                        while k < len(ammos2):
                                a, b = ammos1[i].pdestroy(), ammos2[k].pdestroy()
                                a = math.ceil(a[0]), math.ceil(a[1])
                                b = math.ceil(b[0]), math.ceil(b[1]+1)
                                if a[1] == b[1] and (a[0] == b[0] or -1 >= a[0] - b[0] <= 1):
                                        ammos1.pop(i)
                                        ammos2.pop(k)
                                        e_rect.center = a[1]*20-10, a[0]*20+10
                                        ilolo = 0
                                k+=1
        elif orient == 2:
                for i in reversed(range(0, len(ammos2))):
                        k = 0
                        while k < len(ammos1):
                                a, b = ammos2[i].pdestroy(), ammos1[k].pdestroy()
                                a = math.ceil(a[0]), math.ceil(a[1])
                                b = math.ceil(b[0]), math.ceil(b[1]+1)
                                if a[1] == b[1] and (a[0] == b[0] or -1 >= b[0] - a[0] <= 1):
                                        ammos2.pop(i)
                                        ammos1.pop(k)
                                        e_rect.center = b[1]*20-10, b[0]*20+10
                                        ilolo = 0
                                k+=1



                        
        for i in reversed(range(0, len(ammos2))):
                ammos2[i].step()
                if ammos2[i].destroy(matrix):
                        ammos2.pop(i)
                        ilolo = 0
                        ste = 0
        for i in reversed(range(0, len(ammos3))):
                ammos3[i].step()
                if ammos3[i].destroy(matrix):
                        ammos3.pop(i)
                        ilolo = 0
                        ste = 0
        for i in reversed(range(0, len(ammos4))):
                ammos4[i].step()
                if ammos4[i].destroy(matrix):
                        ammos4.pop(i)
                        ilolo = 0
                        ste = 0
                
            
                    

                                
        screen.fill(color)
        pygame.draw.rect(screen, color2, (0,0,500,500), 5)
        pole(matrix)
        screen.blit(gg, (ggx*20, ggy*20))
        poleFFF(matrix)
        for ammo1 in ammos1:
                ammo1.render(screen)
        for ammo2 in ammos2:
                ammo2.render(screen)
        for ammo3 in ammos3:
                ammo3.render(screen)
        for ammo4 in ammos4:
                ammo4.render(screen)
        screen.blit(explosion, e_rect, slide_rect)
        
        

        pygame.display.flip()

        time.sleep(0.01)

        
