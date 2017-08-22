# Define different types of bricks
#
#
#
#

class brick:
    """
    defines bricks
    """
    
    def __init__(self, color, xyList): 
        
        self.color = color
        self.size = len(xyList)
        self.variant = 0
        self.x = 0
        self.y = 0
        self.partsList = []
        
        baseX = min( [xyList[i][0] for i in range(len(xyList))] )
        baseY = min( [xyList[i][1] for i in range(len(xyList))] )
        
        for xy in xyList:
            self.partsList.append((xy[0] - baseX, xy[1] - baseY)) 
        
        self.placed = False
    
        
    def getParts(self, x, y, variant):
        # returns a list of (x,y) of all parts of a brick started with (x,y)
        i = variant
        if variant >= 4:
            b = self.__simCopy__()
            i -= 4
        else:
            b = self 
        
        while i != 0:
            b = b.__rotatedCopy__()
            if b == self:
                b = self.__simCopy__()
            i -= 1
        
        return [(xi + x, yi + y) for (xi, yi) in b.partsList ]
    
    
    def __normalize__(self):
        baseX = min( [self.partsList[i][0] for i in range(self.size) ] )
        baseY = min( [self.partsList[i][1] for i in range(self.size) ] )
        
        xyList = self.partsList
        self.partsList = []
        for p in xyList:
            self.partsList.append( (p[0]-baseX, p[1]-baseY) )
                    
        
    def __rotatedCopy__(self):
        b = brick(self.color, self.partsList)
        xyList = b.partsList
        b.partsList = []
        for xy in xyList:
            b.partsList.append( (xy[1], -xy[0]) )
        b.__normalize__()
        return b 
        
        
    def __simCopy__(self):
        b = brick(self.color, self.partsList)
        xyList = b.partsList
        b.partsList = []
        for xy in xyList:
            b.partsList.append( (-xy[0], xy[1]) )
        b.__normalize__()
        return b  
    
    
    def __eq__(self, anotherBrick):    
        #returns True if it is similar to anotherBrck
        if self.size != anotherBrick.size:
            return False
        
        for p1 in self.partsList:
            res = False
            for p2 in anotherBrick.partsList:
                if p1 == p2:
                    res = True
                    break
            if res == False: break
        return res
        
        
    def getVariants(self):
        # returns the number of unique variants
        
        variants = []
        variants.append(self)
        
        b = self.__rotatedCopy__()
        if self.__eq__( b ): return 1
        variants.append(b)
        
        b = b.__rotatedCopy__()
        if self.__eq__( b ): 
            b = self.__simCopy__()
            if self.__eq__(b): return 2
            else: return 4
        
        variants.append(b)
        variants.append(b.__rotatedCopy__())
        
        bSim = self.__simCopy__()
        
        for b in variants:
            if bSim.__eq__(b): return 4
        
        return 8
        
           
               
def isOut(x, y):
    # returns True if (x, y) is out of the game field
    
    if x + y > 4: return True
    if y - x < -6: return True
    if y + x < -4: return True
    if y - x > 4: return True
    
    return False

       
