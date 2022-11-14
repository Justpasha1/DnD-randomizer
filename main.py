import pygame
import os
from random import randint

#program settings
screen = pygame.display.set_mode((500, 500))
bg = (0, 0, 0)
pygame.display.set_caption("DnD randomizer")
pathicon = os.path.join(os.path.abspath(__file__ + "/..") + "\images\dndnumicon.png")
icon = pygame.image.load(pathicon)
pygame.display.set_icon(icon)
pygame.display.flip()

class Images():
    def __init__(self, x, y, widht, height, path):
        self.X = x
        self.Y = y
        self.WIDHT = widht
        self.HEIGHT = height
        self.PATH = path
    def loadimages(self):
        path = os.path.join(os.path.abspath(__file__ + "/.."))
        images = path + self.PATH
        images = pygame.image.load(images)
        images = pygame.transform.scale(images, (self.WIDHT, self.HEIGHT))
        screen.blit(images, (self.X, self.Y))

bgimages = Images(0, 0, 500, 500, "\images\gdnd.png")
texttitle = Images(100,0,300,50,"\images\chooseone.png")
buttonguit1 = Images(150, 400,200,100,"\images\wbutton1.png")
buttonguit2 = Images(275, 400,200,100,"\images\wbutton1.png")
buttonback = Images(25, 400, 200, 100, "\images\wbutton3.png")
buttonroll = Images(150, 300, 200, 100, "\images\wbutton2.png")
d2b = Images(50, 100, 60, 60, "\images\dndnum2.png")
d3b = Images(135, 100, 60, 60, "\images\dndnum3.png")
d4b = Images(220, 100, 60, 60, "\images\dndnum4.png")
d6b = Images(305, 100, 60, 60, "\images\dndnum6.png")
d8b = Images(390, 100, 60, 60, "\images\dndnum8.png")
d12b = Images(110, 180, 60, 60, "\images\dndnum12.png")
d16b = Images(220, 180, 60, 60, "\images\dndnum16.png")
d20b = Images(330, 180, 60, 60, "\images\dndnum20.png")
dndnum = Images(160, 75, 180, 180, "\images\dndnum1.png")

#randomizer cycle
game = True
scene = 1
while game:
    if scene == 1:
        bgimages.loadimages()
        texttitle.loadimages()
        buttonguit1.loadimages()
        d2b.loadimages()
        d3b.loadimages()
        d4b.loadimages()
        d6b.loadimages()
        d8b.loadimages()
        d12b.loadimages()
        d16b.loadimages()
        d20b.loadimages()
    if scene == 2:
        bgimages.loadimages()
        buttonguit2.loadimages()
        buttonback.loadimages()
        buttonroll.loadimages()
        dndnum.loadimages()
    if scene == 3:
        bgimages.loadimages()
        buttonguit2.loadimages()
        buttonback.loadimages()
        buttonroll.loadimages()
        dndnum.loadimages()
    if scene == 4:
        bgimages.loadimages()
        buttonguit2.loadimages()
        buttonback.loadimages()
        buttonroll.loadimages()
        dndnum.loadimages()
    if scene == 5:
        bgimages.loadimages()
        buttonguit2.loadimages()
        buttonback.loadimages()
        buttonroll.loadimages()
        dndnum.loadimages()
    if scene == 6:
        bgimages.loadimages()
        buttonguit2.loadimages()
        buttonback.loadimages()
        buttonroll.loadimages()
        dndnum.loadimages()
    if scene == 7:
        bgimages.loadimages()
        buttonguit2.loadimages()
        buttonback.loadimages()
        buttonroll.loadimages()
        dndnum.loadimages()
    if scene == 8:
        bgimages.loadimages()
        buttonguit2.loadimages()
        buttonback.loadimages()
        buttonroll.loadimages()
        dndnum.loadimages()
    if scene == 9:
        bgimages.loadimages()
        buttonguit2.loadimages()
        buttonback.loadimages()
        buttonroll.loadimages()
        dndnum.loadimages()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if scene == 1:
                if 150 <= mouse[0] <= 350 and 400 <= mouse[1] <= 500:
                    game = False
                if 50 <= mouse[0] <= 110 and 100 <= mouse[1] <= 160:
                    scene = 2
                if 135 <= mouse[0] <= 195 and 100 <= mouse[1] <= 160:
                    scene = 3
                if 220 <= mouse[0] <= 280 and 100 <= mouse[1] <= 160:
                    scene = 4
                if 305 <= mouse[0] <= 365 and 100 <= mouse[1] <= 160:
                    scene = 5
                if 390 <= mouse[0] <= 450 and 100 <= mouse[1] <= 160:
                    scene = 6
                if 110 <= mouse[0] <= 170 and 180 <= mouse[1] <= 240:
                    scene = 7
                if 220 <= mouse[0] <= 280 and 180 <= mouse[1] <= 240:
                    scene = 8
                if 330 <= mouse[0] <= 390 and 180 <= mouse[1] <= 240:
                    scene = 9
            if scene == 2:
                if 25 <= mouse[0] <= 225 and 400 <= mouse[1] <= 500:
                    scene = 1
                if 275 <= mouse[0] <= 475 and 400 <= mouse[1] <= 500:
                    game = False
                if 150 <= mouse[0] <= 350 and 300 <= mouse[1] <= 400:
                    number = str(randint(1,2))
                    dndnum.PATH = "\images\dndnum" + number + ".png"
            if scene == 3:
                if 25 <= mouse[0] <= 225 and 400 <= mouse[1] <= 500:
                    scene = 1
                if 275 <= mouse[0] <= 475 and 400 <= mouse[1] <= 500:
                    game = False
                if 150 <= mouse[0] <= 350 and 300 <= mouse[1] <= 400:
                    number = str(randint(1,3))
                    dndnum.PATH = "\images\dndnum" + number + ".png"
            if scene == 4:
                if 25 <= mouse[0] <= 225 and 400 <= mouse[1] <= 500:
                    scene = 1
                if 275 <= mouse[0] <= 475 and 400 <= mouse[1] <= 500:
                    game = False
                if 150 <= mouse[0] <= 350 and 300 <= mouse[1] <= 400:
                    number = str(randint(1,4))
                    dndnum.PATH = "\images\dndnum" + number + ".png"
            if scene == 5:
                if 25 <= mouse[0] <= 225 and 400 <= mouse[1] <= 500:
                    scene = 1
                if 275 <= mouse[0] <= 475 and 400 <= mouse[1] <= 500:
                    game = False
                if 150 <= mouse[0] <= 350 and 300 <= mouse[1] <= 400:
                    number = str(randint(1,6))
                    dndnum.PATH = "\images\dndnum" + number + ".png"
            if scene == 6:
                if 25 <= mouse[0] <= 225 and 400 <= mouse[1] <= 500:
                    scene = 1
                if 275 <= mouse[0] <= 475 and 400 <= mouse[1] <= 500:
                    game = False
                if 150 <= mouse[0] <= 350 and 300 <= mouse[1] <= 400:
                    number = str(randint(1,8))
                    dndnum.PATH = "\images\dndnum" + number + ".png"
            if scene == 7:
                if 25 <= mouse[0] <= 225 and 400 <= mouse[1] <= 500:
                    scene = 1
                if 275 <= mouse[0] <= 475 and 400 <= mouse[1] <= 500:
                    game = False
                if 150 <= mouse[0] <= 350 and 300 <= mouse[1] <= 400:
                    number = str(randint(1,12))
                    dndnum.PATH = "\images\dndnum" + number + ".png"
            if scene == 8:
                if 25 <= mouse[0] <= 225 and 400 <= mouse[1] <= 500:
                    scene = 1
                if 275 <= mouse[0] <= 475 and 400 <= mouse[1] <= 500:
                    game = False
                if 150 <= mouse[0] <= 350 and 300 <= mouse[1] <= 400:
                    number = str(randint(1,16))
                    dndnum.PATH = "\images\dndnum" + number + ".png"
            if scene == 9:
                if 25 <= mouse[0] <= 225 and 400 <= mouse[1] <= 500:
                    scene = 1
                if 275 <= mouse[0] <= 475 and 400 <= mouse[1] <= 500:
                    game = False
                if 150 <= mouse[0] <= 350 and 300 <= mouse[1] <= 400:
                    number = str(randint(1,20))
                    dndnum.PATH = "\images\dndnum" + number + ".png"

    pygame.display.update()
    mouse = pygame.mouse.get_pos()