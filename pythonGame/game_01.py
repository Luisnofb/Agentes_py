import pygame
from agenteSimples import SimpleR1, SimpleR2
from agenteModelo import  ModelR1, ModelR2
from agenteObjetivo import ObjectiveR1, ObjectiveR2
from agenteUtilidade import UtilityR1, UtilityR2
import trash as tx
import functions as fc

# LOAD
pygame.init()

#####
ctrl = 3
####

size = 600
lix, cords = tx.fullTrash()
numlix = len(lix)
timer = 0
tempo_segundo = 0
txt = ''

# agentes
if ctrl == 1:
    ar1 = SimpleR1()
    ar2 = SimpleR2()
    txt = 'Simples'
elif ctrl ==2:
    ar1 = ModelR1()
    ar2 = ModelR2()
    txt = 'Modelo'
elif ctrl ==3:
    ar1 = ObjectiveR1(cords)
    ar2 = ObjectiveR2()
    txt = 'Objetivo'
else:
    ar1 = UtilityR1(lix)
    ar2 = UtilityR2()
    txt = 'Utilidade'

# info
font = pygame.font.SysFont('arial black', 15)
texto = font.render("Tempo: ", True, (255, 255, 255))
tipo = font.render(txt, True, (255, 255, 255))
pos_txt = texto.get_rect()
pos_tipo = tipo.get_rect()
pos_txt.center = (35, 640)
pos_tipo.center =(37, 615)

# lixeiras
l1 = []
l2 = []

# images#
red = pygame.image.load('img/roboR.png')
blue = pygame.image.load('img/roboB.png')
lixo = pygame.image.load('img/lix.png')
rec = pygame.image.load('img/rec.png')
fire = pygame.image.load('img/fire.png')

# pre_set
janela = pygame.display.set_mode((size, size+60))
pygame.display.set_caption("Agentes")
open_windown = True

while open_windown:

    pygame.time.delay(50)# delay da tela

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open_windown = False

    #a.x,a.y,loo = fc.key_key(a.x,a.y,1,loo)#movimento manual dos robos por hr
    #r2x,r2y,loo = fc.key_key(r2x,r2y,2,loo)

    #a.x,a.y = fc.lopeli(a.x,a.y)#colisoes por hr
    #r2x,r2y = fc.lopeli(r2x,r2y)

    ar1.IA(cords,lix,l1,l2) #IA ag1

    if ar2.work >0:
        texto,timer,tempo_segundo = fc.temporizador(timer,tempo_segundo,texto,font)


#Draw
    janela.fill((0,0,0))#cor da janela

    tx.espalhaLixo(lix,janela)

    janela.blit(lixo, (0,(30 * 11)))
    janela.blit(lixo, (585-15,(30 * 11)))
    janela.blit(rec, (585 - 15, 585-15))
    janela.blit(fire, (-3, 585 - 20))   #imagens personalizadas
    janela.blit(blue, (ar2.x - 11,ar2.y - 11))
    janela.blit(red, (ar1.x - 11, ar1.y - 11))
    janela.blit(tipo, pos_tipo)
    janela.blit(texto, pos_txt)


    for i in range(20):#linhas e colunas 20x20
        pygame.draw.line(janela, (0, 155, 0), [30*i,0], [30*i, size], 2)
        pygame.draw.line(janela, (0, 155, 0), [0,30*i], [size, 30*i], 2)
    pygame.draw.line(janela, (0, 155, 0), [0, size], [size, size], 2)#linha da borda inferior

    ar2.IA(l1, l2, janela)  # IA a2

    pygame.display.update()

pygame.quit()


    #pygame.draw.circle(janela, (0, 0, 255), (r2x, r2y), 10)
    #pygame.draw.line(janela,(0,64,0),[0,75],[600,75],2)#linha unica fraca
    #pygame.draw.lines(janela, (0, 255, 0), False, [(30*i, 0), (30*i, size)], 2)#