#Author:Kreuzer, Martin
#Super Mario-like game---still in progress


import pygame as pg
from tkinter import *
from random import *
import sys


pg.init()


#variables
#>>>>>>>>>>Game Screen<<<<<<<<<<
class sc():
    w = 910
    h = 607
    cap = "PMN_SCB"
    bg = pg.image.load("backG.png")

#>>>>>>>>>>GUI<<<<<<<<<<
class gui():
    w = 250
    h = 250
    cap = "Interface"

def window():
    global win
    win = Tk()
    win.title(gui.cap)
    win.geometry("250x250")

    back = Button(win, text = "Back to Game", command = closeGUI)
    back.pack()
    exitGame = Button(win, text = "Exit Game", command = exitG)
    exitGame.pack()
    
    win.mainloop()

def closeGUI():
    win.destroy()

def exitG():
    closeGUI()
    pg.display.quit()
    sys.exit()

def call():
    if keys[pg.K_ESCAPE]:
        window()

    
#>>>>>>>>>>Player<<<<<<<<<<
class plr:
    
    w = 20
    h = 20
    x = w
    y = sc.h -h * 2
    jump = 8
    vel = 10
    isJump = False
    direction = 1

#>>>>>>>>>>Jump<<<<<<<<<<

def jump():

    if not plr.isJump:
        if keys[pg.K_UP]:
            plr.isJump = True

    else:
        if plr.jump >= -8:
            neg = 1
            if plr.jump < 0:
                neg = -1
            plr.y -= (plr.jump**2) *0.5 *neg
            plr.jump -= 1
        else:
            plr.isJump = False
            plr.jump = 8



    


#>>>>>>>>>>Left and Right<<<<<<<<<<
def left():
    if keys[pg.K_LEFT] and not (plr.x <= plr.w/2) and not keys[pg.K_RIGHT]:
        if plr.isJump:
            plr.x -= plr.vel * 0.5
        else:
            plr.x -= plr.vel * 1.5

def right():
    if keys[pg.K_RIGHT] and not (plr.x >= (sc.w-plr.w*1.5)) and not keys[pg.K_LEFT]:
        if plr.isJump:
            plr.x += plr.vel * 0.5
        else:
            plr.x += plr.vel * 1.5



#>>>>>>>>>>Game Window<<<<<<<<<<
screen = pg.display.set_mode((sc.w, sc.h))
pg.display.set_caption(sc.cap)

def paint():
    screen.fill((0))
    pg.draw.rect(screen, (250,0,0), (plr.x, plr.y, plr.w, plr.h))
    pg.draw.rect(screen, (0,0,250), (plr.x, plr.y-plr.h, plr.w, plr.h))
    pg.display.update()


                
#>>>>>>>>>>Mainloop<<<<<<<<<<
run = True
while run:

    pg.time.delay(75)
        
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            
    keys = pg.key.get_pressed()
    pg.Surface.blit(sc.bg , (0,0))
    
    jump()
    left()
    right()
    paint()
    call()
    
pg.quit()
