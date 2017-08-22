# this program solves a puzzle
# you need to place all bricks into the field defined for the game
# bricks are the figures that can be placed into the field so they ocupy several sits depending on the size of a brick
#
#

import pygame, copy
from pygame.locals import *
import pyganim   
import bricks  


    
class gameState:
    """
    describes the state of the game: list of all bricks, each is in specific state with placed = True or False
    if placed is True, then (x,y,v) describes the place and chosen variant 
    """
    
    def __init__(self, bricks):
        self.bricks = bricks
        #initialize the list of all fields. True if a field is free
        self.fields = [True] * 50
        self.fieldIndex = [(0,4),(-1,3),(-2,2),(-3,1),(-4,0),(-3,-1),(-2,-2),(-1,-3),(0,-4),(1,-5),(2,-4),(3,-3),(4,-2),(5,-1),(4,0),(3,1),(2,2),(1,3),(0,3),(-1,2),(-2,1),(-3,0),(-2,-1),(-1,-2),(0,-3),(1,-4),(2,-3),(3,-2),(4,-1),(3,0),(2,1),(1,2),(0,2),(-1,1),(-2,0),(-1,-1),(0,-2),(1,-3),(2,-2),(3,-1),(2,0),(1,1),(0,1),(-1,0),(0,-1),(1,-2),(2,-1),(1,0),(0,0),(1,-1)]

        for b in self.bricks :
             if b.placed :
                for p in b.getParts(b.x, b.y, b.variant):
                    index = self.getIndex(p[0], p[1])
                    self.fields[index] = False 
        
            
    def getIndex(self, x, y):
        #gets index for self.fields from (x,y). Returns None if index is out od the range
        
        if bricks.isOut(x, y) : return None
        return self.fieldIndex.index((x,y))   
                         
    
    def getXY(self, index):
        #returns (x,y) of the field for the field(index). Returns None if index is out of the range
        if index >= 50: return None
        
        return self.fieldIndex[index]
    
    def getLegalActions(self):
        # returns the list of (brick, x,y, variant) 
        XY = self.getNextXY()
        legalActions = []
        #print "Amount of free bricks:", len( self.getFreeBricks() )
        for b in self.getFreeBricks():
            variants = b.getVariants()
            #print "brick", b.color, "has", variants, "variants"
            for v in range(variants):
                for dx in range(4):
                    x = XY[0]- 3 + dx
                    for dy in range(4):
                        y = XY[1] -3 + dy
                        if XY in b.getParts(x, y, v):
                            fit = True
                            #print "x,y,v:",x,y,v," parts:", b.getParts(x, y, v) 
                            for p in b.getParts(x, y, v):
                                index = self.getIndex( p[0], p[1] )
                                #print p, index,
                                if index == None: 
                                    fit = False
                                    #print fit
                                    break
                                elif not self.fields[ index ]:
                                    fit = False 
                                    #print fit   
                                    break
                                #print fit
                            if fit: legalActions.append( (b, x, y, v) )
        #print len(legalActions), "legal actions"
        return legalActions
    
    def getAction(self, (brick, x, y, variant) ):
        #places brick of variant in (x,y). Returns new state if successful and None if not
        
        newState = copy.deepcopy(self)
        if brick.placed: return None
        
        fit = True
        
        for p in brick.getParts(x, y, variant):
            index = self.getIndex( p[0], p[1] )
                        
            if bricks.isOut(p[0], p[1]): 
                fit = False
                break
            elif not self.fields[ index ]:
                fit = False 
                break
        if fit:
            for b in newState.bricks :
                if b.color == brick.color:
                    b.placed = True
                    b.variant = variant
                    b.x = x
                    b.y = y
                    for p in b.getParts(x, y, variant):
                        index = self.getIndex(p[0], p[1])
                        newState.fields[index] = False
        return newState
             
            
    def isGoal(self):
        #returns True if it is a Goal state
        
        for b in self.bricks:
            if not b.placed: return False
        return True
    
    def getNextXY(self):
        """
        returns next (x,y) which should be covered by a next brick
        """
        if self.isGoal(): return None
    
        for i in range(50) :
            if self.fields[i]: return self.getXY(i) 
                    
        print "Error: no free fields while game is not over"
        return None    
    
    def isIsolated(self):
        #returns True if there is an isolated free fields
        pP = sum( b.size for b in self.bricks if b.placed )
        for index in [17] + range( 1 , int( pP / 1.5 )  ) + range( 19, 18 + int( pP / 2 ) ) + range( 32, 32 + int(pP / 3 )):
            if self.fields[index] == False : continue
            
            X, Y = self.getXY(index)
                        
            isolated = True
            for d in [-1,1]:
                i = self.getIndex(X + d, Y)
                if i != None: 
                    if self.fields[i] : 
                        isolated = False
                        break
                i = self.getIndex(X, Y + d)
                if i != None:
                    if self.fields[i] : 
                        isolated = False
                        break
            if isolated : return True
        
        return False  
                
            
    def getFreeBricks(self):
        #returns a list of bricks that are not placed
        return [ b for b in self.bricks if b.placed == False ]
    
    

    def display(self, surface):
        #displays the field and placed bricks
        XM = 150
        YM = 200
        surface.fill((0,0,0))

        for i in range(50):
            if self.fields[i] :
                (x,y) = self.getXY(i)
                pygame.draw.circle(surface, (0, 0, 0), (XM + x*30, YM - y*30), 13)
                                
                pygame.draw.circle(surface, (50, 50, 50), (XM + x*30, YM - y*30), 8)
                #pygame.draw.circle(surface, (70, 70, 70), (XM + x*30 + 5, YM - y*30 + 3), 3)        
       
        for b in self.bricks:
            if b.placed :
                for p in b.getParts(b.x, b.y, b.variant):
                    pygame.draw.circle(surface, b.color, (XM + p[0]*30, YM - p[1]*30), 13)
                    pygame.draw.circle(surface, (250,250,250), (XM + p[0]*30-5, YM - p[1]*30-3), 1)
        
        
        
        
    

    
    
