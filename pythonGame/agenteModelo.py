import pygame
import functions as fc
from trash import Lixo

class ModelR1:

    def __init__(self):
        self.estado = 'buscar'
        self.regra = ''
        self.x = 15  # valor da corrdenada em x
        self.y = 15  # " "  "  " y
        self.cards = [self.x, self.y]  # pont
        self.bag = Lixo()  # armazenamento de lixo
        self.work = 40  # n de controle
        self.mapa = []
        self.retorno = []
        self.atlas()

    def atlas(self):
        for i in range(20):
            for j in range(20):
                x = [15 + 30 * j, 15 + 30 * i]
                self.mapa.append(x)

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
    def mov(self, cord,t=0):
        if[self.x, self.y] != cord:
            xmax = cord[0]
            ymax = cord[1]
            if t==0:
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
            else:
                if self.y != ymax:
                    if self.y < ymax:
                        self.y += 30
                    else:
                        self.y -= 30
                elif self.x != xmax:
                    if self.x < xmax:
                        self.x += 30
                    else:
                        self.x -= 30
        self.where()

    def ruler(self,l1,l2):
        if self.estado == 'buscar':
            if len(self.mapa) > 0:
                self.regra = 'andar'
            else:
                self.regra = 'esperar'

        elif self.estado == 'levar':
            if l1 == [] and self.x <= 15+30*11:
                self.regra = 'lixo1'
            elif l2 == [] and self.x >15+30*11:
                self.regra = 'lixo2'
            elif l1 ==[]:
                self.regra = 'lixo1'
            elif l2 ==[]:
                self.regra = 'lixo2'


    def atuador(self,l,lx,l1,l2):
        if self.regra == 'andar':

            ponto = self.mapa[0]
            self.mov(ponto,1)
            self.where()
            if self.cards == ponto:
                busc = self.search(l, lx, self.x, self.y)
                if busc:
                    del (self.mapa[0])
                    self.muda('levar')
                else:
                    del (self.mapa[0])
            elif self.cards != ponto :#observa pobntos de interesse no caminho e os leva logo
                ponto = [self.x,self.y]
                if ponto in l:
                    for c, k in enumerate(self.mapa):
                        if ponto[0] == k[0] and ponto[1] == k[1]:
                            busc = self.search(l, lx, self.x, self.y)
                            if busc:
                                del (self.mapa[c])
                                self.muda('levar')

        elif self.regra == 'esperar':
            pass

        elif self.regra == 'lixo1':
            ponto = [15,15+30*11]
            self.mov(ponto)
            if self.cards == ponto:
                l1.append(self.bag)
                self.work -= 1
                self.bag = []
                print("Depositado!")
                self.muda()

        elif self.regra == 'lixo2':
            ponto = [585, 15 + 30 * 11]
            self.mov(ponto)
            if self.cards == ponto:
                l2.append(self.bag)
                self.work -= 1
                self.bag = []
                print("Depositado!")
                self.muda()

    def IA(self,l,lx,l1,l2):
        if self.work > 0:
            self.ruler(l1,l2)
            self.atuador(l,lx,l1,l2)
        else:
            self.mov([15,15])

class ModelR2:

    def __init__(self):
        self.estado = 'buscar'
        self.regra = ''
        self.x = 585  # valor da corrdenada em x
        self.y = 15  # " "  "  " y
        self.cards = [self.x, self.y]  # pont
        self.bag = Lixo()  # armazenamento de lixo
        self.work = 40  # n de controle

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

    def ruler(self):
        if self.estado == 'buscar':
                self.regra = 'busca'

        elif self.estado == 'levar':
            if self.bag.tipo == 1:
                self.regra = 'recl'
            elif self.bag.tipo == 2:
                self.regra = 'insi'

    def atuador(self,l1,l2,w):
        if self.regra == 'busca':
            if l1 != [] :
                ponto =[15,15 + 30 * 11]
                self.mov(ponto)
                if self.cards == ponto:
                    self.bag = l1.pop()
                    self.muda('levar')

            elif l2 != [] :
                ponto = [585, 15 + 30 * 11]
                self.mov(ponto)
                if self.cards == ponto:
                    self.bag = l2.pop()
                    self.muda('levar')

        elif self.regra == 'recl':
            drw = [self.x, self.y + 5]
            ponto = [585,585]
            self.mov(ponto)
            pygame.draw.circle(w, self.bag.cor, (drw), 6)
            if self.cards == ponto:
                self.bag = []
                self.work -= 1
                print("Reciclado!")
                self.muda()

        elif self.regra == 'insi':
            drw = [self.x, self.y + 5]
            ponto = [15,585]
            self.mov(ponto)
            pygame.draw.circle(w, self.bag.cor, (drw), 6)
            if self.cards == ponto:
                self.bag = []
                self.work -= 1
                print("Queimado!")
                self.muda()

    def IA(self,l1,l2,w):
        if self.work > 0:
            self.ruler()
            self.atuador(l1, l2, w)
        else:
            self.mov([585, 15])



