import pygame
from random import randint
from trash import Lixo

class Cord:
    """Classe teste"""

    def __init__(self, x=0, y=0):
        self.cardis = [x, y]


def lopeli(x, y):
    """controla o movimento de ir e voltar e limita as bordas"""

    if y > 585:
        y = 585
    if y < 10:
        y = 15
    if x < 10:
        x = 15
    if x > 585:
        x = 585
    return x, y


def key_key(x, y, z, loo):
    """controlar o movimento com base na tecla precionada"""
    key = pygame.key.get_pressed()

    if z == 1:
        if key[pygame.K_UP]:
            y -= 30
        if key[pygame.K_DOWN]:
            y += 30
        if key[pygame.K_RIGHT]:
            x += 30
        if key[pygame.K_LEFT]:
            x -= 30
        if key[pygame.K_q]:
            loo = False
        if key[pygame.K_e]:
            loo = True
    else:
        if key[pygame.K_w]:
            y -= 30
        if key[pygame.K_s]:
            y += 30
        if key[pygame.K_d]:
            x += 30
        if key[pygame.K_a]:
            x -= 30

    return x, y, loo


def randTab():
    """Gera numeros randomicos adequados ao modelo do jogo"""
    k = randint(0, 19)
    return 15 + 30 * k


def lixeiro(x, y, l, cords):
    """Prototipo do que sera a lixeira"""
    clone = Lixo()
    if [x, y] in cords:
        for c, k in enumerate(l):
            if k.pontos == [x, y]:
                clone = l[c]
                del (l[c])

        return clone


def mov_1(x, y):
    "prototipo do que sera amivimentação"

    xmax = 15 + 30 * 11
    ymax = 15 + 30 * 11
    tag = False
    if x == xmax:
        tag = True
    if x != xmax:
        if x < xmax:
            x += 30
        else:
            x -= 30
    if tag and y != ymax:
        if y < ymax:
            y += 30
        else:
            y -= 30
    return x, y


def temporizador(timer, tempo_segundo, texto, font):
    if (timer < 20):
        timer += 1
    else:
        tempo_segundo += 1
        texto = font.render("Tempo: " + str(tempo_segundo) + 's', True, (255, 255, 255))
        timer = 0
    return texto, timer, tempo_segundo

"""
lis = []
lo = []
for i in range(10):
     i = randint(0,10)
     j = randint(0,10)
     lis.append([15+30*i,15+30*j])
lis.sort()
for j in range(10):
    lo.append(lis.pop())
    print(lo)
    lo.clear()

"""

"""
lista = [[7,2],[5,3],[5,7]]
print(lista)
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)

"""

"""Forma descartada de armazenamento
matrizx = np.zeros((20,20), np.int32 )
matrizy = np.zeros((20,20), np.int32 )

xpos=-15
for i in range(20):
    xpos+= 30
    ypos = 15
    for j in range(20):
        matrizx[i][j] = xpos
        matrizy[i][j] = ypos
        ypos += 30
"""
# testes...
"""
t = Cord(1,2)
print(t.cardis)
l = list()
for i in range(20):
    x = Cord(15+30*i,15+30*i)
    l.append(x)
l.clear()
for i in range(20):
    for j in range(20):
        x = Cord(15+30*i,15+30*j)
        sl = list()
        sl.append(x.cardis)
        l.append(sl)

print(len(l))
#matriz como linha m*i+j onde m é o n de lementos por linha
print(l[20*0+19])
lin = []
lin.append([1,3])
lin.append([2,4])
if [2,4] in lin:
    print("KKKK")
print(lin,end =' ')
print("\n")
lin.clear()
print(f'-:{len(lin)}')
"""
