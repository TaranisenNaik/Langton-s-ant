import pygame as pg
import random
import time
pg.init()
screen=pg.display.set_mode((800,800))
running=True
class ant():
    def __init__(self,x,y,px,py):
        self.ant_x=x
        self.ant_y=y
        self.prev_x=px
        self.prev_y=py
a=ant(40,40,40,41)


arr_obj=[]

def lineh(y):
    pg.draw.line(screen, (0, 0, 0), 
                 [0, y], 
                 [800, y], 1)
def linev(x):
    pg.draw.line(screen, (0, 0, 0), 
                 [x, 0], 
                 [x, 800], 1)
def save(ant):
    ant.prev_x=ant.ant_x
    ant.prev_y=ant.ant_y
def right(ant):
    if ant.prev_x==ant.ant_x and ant.ant_y<ant.prev_y:
        save(ant)
        ant.ant_x+=1
    elif ant.prev_x==ant.ant_x and ant.ant_y>ant.prev_y:
        save(ant)
        ant.ant_x-=1
    elif ant.prev_y==ant.ant_y and ant.ant_x>ant.prev_x:
        save(ant)
        ant.ant_y+=1
    elif ant.prev_y==ant.ant_y and ant.ant_x<ant.prev_x:
        save(ant)
        ant.ant_y-=1
def left(ant):
    if ant.prev_x==ant.ant_x and ant.ant_y<ant.prev_y:
        save(ant)
        ant.ant_x-=1
    elif ant.prev_x==ant.ant_x and ant.ant_y>ant.prev_y:
        save(ant)
        ant.ant_x+=1
    elif ant.prev_y==ant.ant_y and ant.ant_x>ant.prev_x:
        save(ant)
        ant.ant_y-=1
    elif ant.prev_y==ant.ant_y and ant.ant_x<ant.prev_x:
        save(ant)
        ant.ant_y+=1

class box():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.colour=(255,255,255)
        self.position=False
        self.pheromone=0
    def on(self):
        self.colour=(0,0,0)
        self.position=True
        self.pheromone=5
    def off(self):
        self.colour=(255,255,255)
        self.position=False
        
    def disp(self):
        pg.draw.rect(screen,self.colour,
                 [(self.x-1)*10+1, (self.y-1)*10+1, 9, 9], 0)
rows, cols=81,81
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(box(i,j))
    arr_obj.append(col)
def move(ant):
    if arr_obj[ant.ant_x][ant.ant_y].position:
        arr_obj[ant.ant_x][ant.ant_y].off()
        left(ant)      
    else:
        arr_obj[ant.ant_x][ant.ant_y].on()
        right(ant)
while running:   
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running=False
        
    screen.fill((255,255,255))
    i=10
    while i<800:
        linev(i)
        lineh(i)
        i+=10
    move(a)
    
    
    for i in range(rows):
        col = []
        for j in range(cols):       
            arr_obj[i][j].disp()
    pg.display.update()