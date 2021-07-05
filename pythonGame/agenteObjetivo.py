import pygame
import functions as fc
from trash import Lixo


class ObjectiveR1:
    def __init__(self,list):
        self.estado = 'buscar'
        self.x = 15  # valor da corrdenada em x
        self.y = 15  # " "  "  " y
        self.cards = [self.x, self.y]  # pont
        self.bag = Lixo()  # armazenamento de lixo
        self.work = 40  # n de
        self.ob = 0
        list.sort() #plano de movimento
        self.objetivo = list

    def where(self):
        self.cards = [self.x, self.y]

    def muda(self, std='buscar'):
        self.estado = std

    def search(self, list, listx, x, y):
        if [x, y] in list:
            self.bag = fc.lixeiro(x, y, listx, list)
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

    def IA(self,l,lx,l1,l2):
        if self.work != 0:
            if self.estado == 'buscar':
                if len(self.objetivo) > 0:
                    ponto = self.objetivo[0]
                    self.mov(ponto)
                    if self.cards == ponto:
                        busc = self.search(l,lx,self.x,self.y)
                        if busc:
                            del(self.objetivo[0])
                            self.muda('levar')

            elif self.estado == 'levar':


                if l1 == [] and self.x <= 15+30*11:
                    ponto = [15, 15 + 30 * 11]
                    self.mov(ponto)
                    if self.cards == ponto:
                        l1.append(self.bag)
                        self.work -= 1
                        self.bag = []
                        print("Depositado!")
                        self.ob=0
                        self.muda()

                elif l2 == [] and self.x > 15+30*11:
                    self.ob = 1
                    ponto = [585, 15 + 30 * 11]
                    self.mov(ponto)
                    if self.cards == ponto:
                        l2.append(self.bag)
                        self.work -= 1
                        self.bag = []
                        print("Depositado!")
                        self.ob=0
                        self.muda()
        else:
            self.mov([15, 15])


class ObjectiveR2:

    def __init__(self):
        self.estado = 'buscar'
        self.x = 585  # valor da corrdenada em x
        self.y = 15  # " "  "  " y
        self.cards = [self.x, self.y]  # pontos cardeiais
        self.bag = Lixo()  # armazenamneot de lixo
        self.work = 40  # n de controle


    def where(self):
        self.cards = [self.x, self.y]

    def muda(self, std='buscar'):
        self.estado = std

    def mov(self, cord):
        if [self.x, self.y] != cord:
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
            if self.estado == 'buscar':
                if l1 != []:
                    self.mov([15, 15 + 30 * 11])
                    if self.cards == [15, 15 + 30 * 11]:
                        self.bag = l1.pop()
                        l1.clear()
                        print("Retirado!")
                        self.muda('processar')
                elif l2 != []:
                    self.mov([585, 15 + 30 * 11])
                    if self.cards == [585, 15 + 30 * 11]:
                        self.bag = l2.pop()
                        l2.clear()
                        print("Retirado!")
                        self.muda('processar')
                else:
                    print("Aaguardando...")

            elif self.estado == 'processar':
                drw = [self.x, self.y + 5]
                if self.bag.tipo == 1:
                    self.mov([15 + 30 * 19, 15 + 30 * 19])
                    pygame.draw.circle(w, self.bag.cor, (drw), 6)
                    if self.cards == [15 + 30 * 19, 15 + 30 * 19]:
                        self.bag = []
                        self.work -= 1
                        print("Reciclado!")
                        self.muda()
                else:
                    self.mov([15, 15 + 30 * 19])
                    pygame.draw.circle(w, self.bag.cor, (drw), 6)
                    if self.cards == [15, 15 + 30 * 19]:
                        self.bag = []
                        self.work -= 1
                        print('Queimado!')
                        self.muda()
        else:
            self.mov([585,15])


