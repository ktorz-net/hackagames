import math

from ..pylib import pod

class Tile(pod.PodInterface):

    # Initialization Destruction:
    def __init__( self, num= 0, type= 0, center= (0.0, 0.0), size= 1.0, stamp=0 ):
        self._num= num
        self._type= type
        self._stamp= stamp
        self.setShapeSquare( center, size )
        self._adjacencies= []
        self._pieces= []
    
    # Accessor:
    def number(self):
        return self._num
    
    def type(self):
        return self._type
    
    def stamp(self):
        return self._stamp
        
    def center(self):
        return self._center

    def envelope(self):
        return self._envs
    
    def box(self):
        env= self.envelope()
        minx, miny= env[0]
        maxx, maxy= env[0]
        for x, y in env[1:] :
            if x < minx :
                minx= x
            if y < miny :
                miny= y
            if x > maxx :
                maxx= x
            if y > maxy :
                maxy= y
        return [(minx, miny), (maxx, maxy)]
    
    
    def adjacencies(self):
        return self._adjacencies
    
    def pieces(self) :
        return self._pieces
    
    def piece(self, i=1) :
        return self._pieces[i-1]
    
    # list accessors: 
    def envelopeAsList(self):
        l= []
        for x, y in self._envs :
            l+= [x, y]
        return l

    # Pod interface:
    def asPod(self, family="Tile"):
        tilePod= pod.Pod(
            family,
            "",
            [self.number(), self.stamp()] + self.adjacencies(),
            list( self.center() ) + self.envelopeAsList()
        )
        for p in self.pieces() :
            tilePod.append( p.asPod() )
        return tilePod
    
    def fromPod(self, aPod):
        # Convert flags:
        flags= aPod.flags()
        self._num= flags[0]
        self._stamp= flags[1]
        self._adjacencies= flags[2:]
        # Convert Values:
        vals= aPod.values()
        xs= [ vals[i] for i in range( 0, len(vals), 2 ) ]
        ys= [ vals[i] for i in range( 1, len(vals), 2 ) ]
        self._center= ( xs[0], ys[0] )
        self._envs= [ (x, y) for x, y in zip(xs[1:], ys[1:]) ]
        # Load pices:
        self.piecesFromChildren( aPod.children() )
        return self

    def piecesFromChildren(self, aListOfPod):
        self._pieces= aListOfPod
        return self

    # Construction:
    def setNumber(self, i):
        self._num= i
        return self

    def setCenter(self, x, y):
        self._center= (x, y)
        return self

    def setStamp(self, i):
        self._stamp= i
        return self
    
    def setLimits( self, limits ):
        self._envs= list(limits)
        return self
    
    # Shape Construction:
    def setShapeSquare(self, center, size):
        demi= size*0.5
        x, y= center
        self._envs= [
            ( x-demi, y+demi ),
            ( x+demi, y+demi ),
            ( x+demi, y-demi ),
            ( x-demi, y-demi )
        ]
        self._center= center
        return self

    def setShapeRegular(self, center, size, numberOfVertex= 6):
        radius= size*0.5
        x, y= center
        self._envs= []
        delta= math.pi/(numberOfVertex/2)
        angle= math.pi  - delta/2
        delta= math.pi/(numberOfVertex/2)
        for i in range(numberOfVertex) :
            self._envs.append( (
                x+math.cos(angle)*radius,
                y+math.sin(angle)*radius
            ) )
            angle+= -delta
        self._center= center
        return self
    
    # Tile comparison :
    def centerDistance(self, another):
        x1, y1= self.center()
        x2, y2= another.center()
        dx= x2-x1
        dy= y2-y1
        return math.sqrt( dx*dx + dy*dy )
    
    # Connection
    def connect(self, iTo):
        if iTo not in self._adjacencies :
            self._adjacencies.append(iTo)
            self._adjacencies.sort()
        return self

    def connectAll( self, aList ):
        for iTo in aList :
            self.connect( iTo )
        return self
    
    # Piece managment
    def append(self, aPiece ):
        self._pieces.append( aPiece )
        return self
    
    def clear(self):
        self._pieces = []
        return self

    # to str
    def str(self, name="Tile", ident=0): 
        # Myself :
        s= f"{name}-{self.number()}/{self.stamp()}"
        x, y = self._center
        x, y = round(x, 2), round(y, 2)
        s+= f" center: ({x}, {y})"
        s+= " adjs: "+ str(self._adjacencies)
        s+= f" pieces({ len(self.pieces()) })"
        return s
    
    def __str__(self): 
        return self.str()
    