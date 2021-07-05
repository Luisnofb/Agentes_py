from random import randint
import pygame
import functions as fc

class Lixo:
    #lixo
    def __init__(self,x=0,y=0,color=(155, 155, 155)):
        self.pontos =[x,y]
        self.cor = color
        self.tipo =1

def fullTrash():
        """Gera, posiciona e guarda as cordenadas dos lixos e da sua cor"""
        lixos = []
        cords = []
        while len(lixos) < 40:
            c = randint(1, 2)
            vx = fc.randTab()
            vy = fc.randTab()
            if not [vx, vy] in cords and ([vx,vy] != [15,15] and ([vx,vy] != [15,15+30*11] and [vx,vy] != [585,15+30*11]) and ([vx,vy] != [15,585] and [vx,vy] != [585,585])):
                lx = Lixo(vx,vy)
                if c == 1:
                    lx.cor = (155, 55, 0)
                    lx.tipo = 2
                lixos.append(lx)
                cords.append([vx, vy])
        return lixos,cords

def espalhaLixo(lix,window):
    for lx in lix:#Lixos
        pygame.draw.circle(window,lx.cor, (lx.pontos), 6)
        #lix.pop()
