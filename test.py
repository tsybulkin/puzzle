# main file to start solving the puzzle
#
#
#

import bricks

def getXY(state):
    """
    returns next (x,y) which should be covered by a next brick
    """
    if state.isGoal() return None
    
    freeFields = Fields
    
    for b in state if b.placed:
        for (x,y) in b.getParts(b.x, b.y, b.variant) :
            freeFields.remove((x,y))
    Y = max([freeFields[i][1] for i in range(len(freeFields))])
    X = min([freeFields[i][0] for i in range(len(freeFields)) if freeFields[i][1] == Y ] )
    return (X,Y)


# create the list of all fields
Fields = []
for x in range(-5, 6):
    for y in range (-6, 4):
        if not bricks.isOut(x, y):
            Fields.append((x,y))
            

Bricks = []
# 3-parts:
Bricks.append( bricks.brick((250,250,250), [(0,0),(0,1),(1,0)] ) )
# 4-parts:
Bricks.append( bricks.brick((150,210,70), [(0,0),(-1,0),(0,1),(1,0)] ) )
Bricks.append( bricks.brick((80,35,0), [(0,0),(0,1),(1,1),(1,2)] ) )
Bricks.append( bricks.brick((50,0,70), [(0,0),(1,0),(2,0),(3,0)] ) )
# 5-parts:
Bricks.append( bricks.brick((180,0,50), [(0,0),(0,1),(0,2),(1,0),(1,1)] ) )
Bricks.append( bricks.brick((150,200,250), [(0,0),(0,1),(0,2),(1,0),(2,0)] ) )
Bricks.append( bricks.brick((240,250,0), [(0,0),(0,1),(0,2),(1,0),(1,2)] ) )
Bricks.append( bricks.brick((150,50,150), [(1,0),(0,1),(0,2),(2,0),(1,1)] ) )
Bricks.append( bricks.brick((250,180,200), [(0,0),(0,1),(0,2),(0,3),(1,2)] ) )
Bricks.append( bricks.brick((0,120,25), [(0,0),(0,1),(0,2),(1,2),(1,3)] ) )
Bricks.append( bricks.brick((0,0,100), [(0,0),(0,1),(0,2),(1,0),(0,3)] ) )


startState = gameState(Bricks)
state = startState

x, y = getXY(state)


print "In the field:", bricks.isOut(0,0), bricks.isOut(1,3), bricks.isOut(-2,2), bricks.isOut(-3,-1), bricks.isOut(1,-5), bricks.isOut(4,-2)
print "Out of the field:", bricks.isOut(1,4), bricks.isOut(-3,2), bricks.isOut(0,-5), bricks.isOut(5,0), bricks.isOut(5,2)
    
   
import pygame
from pygame.locals import *
import pyganim
pygame.init()
windowSurface = pygame.display.set_mode((1280, 960), 0, 32)
surf1 = pygame.Surface((1200, 900))

i = 0
for b in Bricks:
    for v in range(b.getVariants()):
        for p in b.getParts(0,0,v):
            pygame.draw.circle(surf1, b.color, (50 + i*100 + p[0]*20, 50 + v*100 + p[1]*20), 9)
        
    i += 1
    


# create the PygAnimation object
animObj = pyganim.PygAnimation([(surf1, 1)])
animObj.play()

while True: # main loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    animObj.blit(windowSurface, (0, 0))
    pygame.display.update()
