# main file to start solving the puzzle
#

#---colors 
maroon = (128,0,0)
violet = (238,130,238)
yellow = (255,255,0)
magenta = ( 255,0,255)
pink = (255,192,203)
dark_green = (0,100,0)
navy = (0,0,128)
cyan = (0,255,255)
white = (255,255,255)
olive = (128,128,0)
firebrick = (178,34,34)
indigo = (75,0,130)
lawn_green = (128,255,0)


#

import bricks, game, sys
#initializes graphics library   
import pygame
from pygame.locals import *

pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((400, 500))
pygame.display.set_caption("Funny puzzle")

Nodes = 0

# surf1 = pygame.Surface(screen.get_size())
# surf1 = surf1.convert()
# surf1.fill((250, 250, 250))

print "screen initiated"

def FindSolution(state, level, screen, surf1, Nodes):
    #returns True if isGoal 
    # global Nodes
    # global surf1
    # global screen
    

    if state.isGoal():
        state.display( screen )
        pygame.display.flip()     
        return True
    
    legalActions = state.getLegalActions()
    Q = len(legalActions) 
    if Q == 0: 
        state.display( screen )
        pygame.display.flip()    
        return False
    
    if level <= 9:
        i = 0
        state.display( screen )
        # font = pygame.font.Font(None, 24)
        # text_surf = font.render("Checked:" + str(Nodes) + "nodes   ", 1, (100, 100, 100))
        
        # screen.blit(text_surf, (200,450) )
        # # surf1.blit(surf1, (0,0) )
        pygame.display.flip()
        pygame.event.poll() 
    
    
    for a in legalActions:
        newState = state.getAction( a )
        Nodes += 1
        if level <= 2:
            i += 1
            print "progress: %.1f%%" % (100.0 * i / Q),  "\tat level", level, "\tnodes checked:", Nodes
        
        if newState.isIsolated():
            continue
                 
        if FindSolution(newState, level + 1, screen, surf1, Nodes):
            GoalStates.append(state)
            
            print "Goal found!", Nodes,"were checked"

            #return True
    
    return False

"""
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

Bricks.reverse()
"""
Bricks = []
#Bricks.append( bricks.brick(maroon, [(0,0),(0,1),(1,0)] ) )

Bricks.append( bricks.brick(firebrick, [(0,0),(0,1),(0,2),(1,0),(1,1)] ) )
Bricks.append( bricks.brick(cyan, [(0,0),(0,1),(0,2),(1,0),(2,0)] ) )
Bricks.append( bricks.brick(yellow, [(0,0),(0,1),(0,2),(1,0),(1,2)] ) )
Bricks.append( bricks.brick(magenta, [(1,0),(0,1),(0,2),(2,0),(1,1)] ) )
Bricks.append( bricks.brick(lawn_green, [(0,0),(0,1),(0,2),(0,3),(1,2)] ) )
Bricks.append( bricks.brick(dark_green, [(0,0),(0,1),(0,2),(1,2),(1,3)] ) )
Bricks.append( bricks.brick(navy, [(0,0),(0,1),(0,2),(1,0),(0,3)] ) )
# new bricks
Bricks.append( bricks.brick(white, [(0,0),(0,1),(0,2),(-1,1)] ) )
Bricks.append( bricks.brick(olive, [(0,0),(1,0),(1,1),(0,1),(1,2),(2,1)] ) )
Bricks.append( bricks.brick(indigo, [(0,0),(0,1),(0,2),(1,1),(-1,2)] ) )

print "Bricks created"

#Level = 0
GoalStates = []

startState = game.gameState(Bricks)

surf1 = None
if not FindSolution(startState, 0, screen, surf1, Nodes): 
    print " there's no solution"
else:
    print "Congats! Soltion is found"


pygame.display.update()    

s = raw_input()


