import pygame
import functions as fc
from trash import Lixo


class SimpleR1:

    def __init__(self):
        self.x = 15 #valor da corrdenada em x
        self.y = 15 # " "  "  " y
        self.cards = [self.x, self.y]  # pontos cardeiais
        self.hor = 1# controle de moviment horizontal
        self.vert = 0 # controle de movimento vertical
        self.dir = True #direção
        self.ob = 1 #lixeira alvo
        self.back = False
        self.bag = []#armazenamento de lixo
        self.memory = []#memoria do ponto de retorno
        self.work = 40 #n de controle

    def where(self):
        self.cards = [self.x, self.y]


    def search(self,list,listx,x,y):
        if [x, y] in list:
            self.bag = fc.lixeiro(x,y,listx,list)
            return True
        else:
            return False

    def mov(self, cord):
        if[self.x, self.y] != cord:
            xmax = cord[0]
            ymax = cord[1]
            if self.y != ymax:
                if self.y < ymax:
                    self.y += 30
                else:
                    self.y -= 30
            if self.x != xmax:
                if self.x < xmax:
                    self.x += 30
                else:
                    self.x -= 30
        self.where()

    def auto(self):

        if self.dir and self.vert != 1:
            self.x += 30
        elif not self.dir and self.vert != 1:
            self.x -= 30

        if self.vert == 1:
            self.y += 30
            self.vert = 0

        if self.x + 30 > 585 and self.hor == 1:
            self.hor = 0
            self.vert = 1
            self.dir = False

        if self.x - 30 < 15 and self.hor == 0:
            self.hor = 1
            self.vert = 1
            self.dir = True

    def IA(self,l,lx,l1,l2):

        if self.work != 0:

            if self.x <= 15+30*11:
                ob = [15 + 30 * 0, 15 + 30 * 11]
                self.ob =1
            else:
                ob = [15 + 30 *19, 15 + 30 * 11]
                self.ob =0

            if self.bag == [] and not self.back:

                self.auto()
                busc = self.search(l,lx, self.x, self.y)

                if busc:
                    self.where()
                    self.memory = self.cards

            elif self.bag != []:
                self.mov(ob)
                self.where()
                if self.cards == ob:
                    if self.ob == 1:
                        if l1 == []:
                            l1.append(self.bag)
                            self.work -= 1
                            self.bag = []
                            self.back = True
                            print("Depositado!")
                        else:
                            print("Aguardando...")
                    else:
                        if l2 == []:
                            l2.append(self.bag)
                            self.work -= 1
                            self.bag = []
                            self.back = True
                            print("Depositado!")
                        else:
                            print("Aguardando...")

            elif self.back:
                self.mov(self.memory)
                self.where()
                if self.cards == self.memory:
                    self.back = False
        else:
            self.mov([15,15])



class SimpleR2:
    def __init__(self):
        self.x = 585  # valor da corrdenada em x
        self.y = 15  # " "  "  " y
        self.cards = [self.x, self.y]  # pontos cardeiais
        self.ob =0
        self.bag = [] # armazenamneot de lixo
        self.work = 40  # n de controle

    def where(self):
        self.cards = [self.x, self.y]

    def mov(self, cord):
        if[self.x, self.y] != cord:
            xmax = cord[0]
            ymax = cord[1]
            if self.y != ymax:
                if self.y < ymax:
                    self.y += 30
                else:
                    self.y -= 30
            if self.x != xmax:
                if self.x < xmax:
                    self.x += 30
                else:
                    self.x -= 30
        self.where()

    def IA(self,l1,l2,w):
        if self.work != 0:
            if self.bag == []:
                if self.ob == 1:
                    self.mov([15,15+30*11])
                    if self.cards == [15,15+30*11]:
                        if l1 == []:
                            self.ob = 0
                        else:
                            self.bag = l1.pop()
                            l1.clear()
                            print("Retirado!")
                            self.ob = 1
                else:
                    self.mov([585,15+30*11])
                    if self.cards == [585,15+30*11]:
                        if l2 == []:
                            self.ob = 1
                        else:
                            self.bag = l2.pop()
                            l2.clear()
                            print("Retirado!")
                            self.ob = 0

            elif self.bag != []:
                drw = [self.x, self.y + 5]
                if self.bag.tipo == 1:
                    self.mov([15+30*19,15+30*19])
                    pygame.draw.circle(w, self.bag.cor, (drw), 6)
                    if self.cards == [15+30*19,15+30*19]:
                        self.bag = []
                        self.work -=1
                        print("Reciclado!")
                else:
                    self.mov([15, 15 + 30 * 19])
                    pygame.draw.circle(w, self.bag.cor, (drw), 6)
                    if self.cards == [15, 15 + 30 * 19]:
                        self.bag = []
                        self.work -=1
                        print('Queimado!')
        else:
            self.mov([585,15])

