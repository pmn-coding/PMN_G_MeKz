#author: M. Kreuzer, PMN
#Small, basic Tetris game

#Libraries
import pygame as pg
from random import randint
import time

pg.init()

#__________Set Screen__________
sw = 300
sh = 500

win = pg.display.set_mode((sw,sh))
pg.display.set_caption("Tetris 1.0")

#variables
y = 0               #y Position of block
lay = []            #Blocks on floor
block1 = [30, 10]   #first kind of block
block2 = [10, 30]   #second " " "
block3 = [20, 20]   #third " " "
isBlock = False     #Is there a block on the field
run  = True         #main loop runs/doesn't run

while run:

    pg.time.delay(100)

#_________Check for quitting__________
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

#_________Create Block__________
    if isBlock == False:
        n = randint(1,3)
        if n == 1:
            block = block1
        elif n == 2:
            block = block2
        else:
            block = block3
    
        x = randint(0, 280)
        while not x%10 == 0:
            x = randint(0,280)

        pg.draw.rect(win, (255,0,0), (x, y, block[0], block[1]))

        isBlock = True

#__________DROPPING__________
    else:
        while not y + block[1] - sh == 0:
            y += 10
            win.fill(0)
            pg.draw.rect(win, (255,0,0), (x, y, block[0], block[1]))
            #Need Delay
        
        lay.append([x,y,block[0],block[1]])
        isBlock = False
        y = 0
#_________Draw fallen blocks________
    for b in lay:
        pg.draw.rect(win, (255,0,0), (lay[b][0], lay[b][1], lay[b][2], lay[b][3]))
        #Some kind of list error
    pg.display.update()

quit()