# Support:
class SupportVoid():

    # Accessor:
    def width(self):
        return 1200
    
    def height(self):
        return 800
    
    # Control:
    def clear(self):
        pass
    
    def render( self ):
        return None
    
    def flip( self ):
        rendering= self.render()
        self.clear()
        return rendering
    
    # Drawing primitives:
    def traceLine( self, pixxA, pixyA, pixxB, pixyB, strokeColor, strokeWidth ):
        pass

    def traceCircle( self, pixx, pixy, radius, strokeColor, strokeWidth ):
        pass

    def fillCircle( self, pixx, pixy, radius, fillColor ):
        pass

    def drawCircle( self, pixx, pixy, radius, fillColor, strokeColor, strokeWidth):
        pass

    def tracePolygon( self, pixXs, pixYs, strokeColor, strokeWidth ):
        pass

    def fillPolygon( self, pixXs, pixYs, fillColor ):
        pass

    def drawPolygon( self, pixXs, pixYs, fillColor, strokeColor, strokeWidth ):
        pass

    # Writting primitives:
    def write( self, pixXs, pixYs, text, color, fontSize ):
        pass

# Artist:
class Brush():
    def __init__(self, fill= 0xff6644, stroke= 0x991100, width= 4 ):
        self.fill= fill
        self.stroke= stroke
        self.width= width

class Artist():
    def __init__(self, support= SupportVoid() ):
        #  Initialize support:
        self._support= support

        # Initialize brush :
        self._panel= [
            Brush(0xffbb55, 0xaa6606, 4), # Background
            Brush(0xff6644, 0x991100, 4), # Red
            Brush(0x44ff44, 0x119911, 4), # Green
            Brush(0x6666ff, 0x1111aa, 4), # Blue
            Brush(0xff9922, 0xdd5500, 4), # Orange
            Brush(0xdd77ff, 0x8800aa, 4), # Purple
            Brush(0x66ddee, 0x117799, 4), # Cian
        ]
        self._fontSize= 16

        # Initialize Frame :
        self._x= 0.0
        self._y= 0.0
        self._scale= 100.0
        self.flip()

    # Accessor:
    def support(self):
        return self._support

    def render( self ):
        return self._support.render()

    def camera( self ):
        return (self._x, self._y)
        
    def scale( self ):
        return (self._scale)
    
    # Setters:
    def setCamera( self, x, y ):
        self._x, self._y= x, y
        return self
        
    def setScale( self, scale ):
        self._scale= scale
        return self
    
    def fitBox( self, aBox, marge=10 ):
        marge= marge*2
        minx, miny= aBox[0]
        maxx, maxy= aBox[1]
        self.setCamera( (minx+maxx)*0.5, (miny+maxy)*0.5 )
        distx= maxx-minx
        disty= maxy-miny
        ratioX= (self._support.width()-marge)/distx
        ratioY= (self._support.height()-marge)/disty
        self.setScale( min(ratioX, ratioY) )
        return self

    # Panel managments:

    # Transformation World <-> Frame
    def toFrame(self, x, y ):
        dwidth= self._support.width()*0.5
        dheight= self._support.height()*0.5
        dx= (x-self._x)*self._scale
        dy= (y-self._y)*-self._scale
        return dx+dwidth, dy+dheight

    def xToFrame(self, x ):
        dwidth= self._support.width()*0.5
        return (x-self._x)*self._scale + dwidth

    def yToFrame(self, y ):
        dheight= self._support.height()*0.5
        return (y-self._y)*-self._scale + dheight

    def toWorld(self, pixx, pixy):
        return 0, 0

    # Drawing primitives:
    def tracePoint( self, x, y, brush= Brush() ):
        pixx, pixy= self.toFrame( x, y )
        self._support.fillCircle( pixx, pixy, brush.width, brush.stroke )
        return self

    def traceLine( self, ax, ay, bx, by, brush= Brush() ):
        pixxA, pixyA= self.toFrame( ax, ay )
        pixxB, pixyB= self.toFrame( bx, by )
        self._support.traceLine( pixxA, pixyA, pixxB, pixyB, brush.stroke, brush.width)
        return self

    def traceCircle( self, x, y, radius, brush= Brush()):
        pixx, pixy= self.toFrame(x, y)
        self._support.traceCircle( pixx, pixy, radius*self._scale, brush.stroke, brush.width)
        return self

    def fillCircle( self, x, y, radius, brush= Brush()):
        pixx, pixy= self.toFrame(x, y)
        self._support.fillCircle( pixx, pixy, radius*self._scale, brush.fill )
        return self

    def drawCircle( self, x, y, radius, brush= Brush() ):
        pixx, pixy= self.toFrame( x, y )
        self._support.drawCircle( pixx, pixy, radius*self._scale, brush.fill, brush.stroke, brush.width )
        return self

    def tracePolygon( self, coordXs, coordYs, brush= Brush() ):
        self._support.tracePolygon(
            [ self.xToFrame( x ) for x in coordXs ],
            [ self.yToFrame( y ) for y in coordYs ],
            brush.stroke, brush.width
        )
        return self

    def fillPolygon( self, coordXs, coordYs, brush= Brush() ):
        self._support.fillPolygon(
            [ self.xToFrame( x ) for x in coordXs ],
            [ self.yToFrame( y ) for y in coordYs ],
            brush.fill
        )
        return self

    def drawPolygon( self, coordXs, coordYs, brush= Brush() ):
        self._support.drawPolygon(
            [ self.xToFrame( x ) for x in coordXs ],
            [ self.yToFrame( y ) for y in coordYs ],
            brush.fill, brush.stroke, brush.width
        )
        return self

    # Writting primitives:
    def write( self, x, y, text, brush= Brush() ):
        self._support.write(
            self.xToFrame(x), self.yToFrame(y),
            text, brush.stroke, self._fontSize
        )
        return self

    # Drawing frame:
    def drawFrameGrid( self, step= 1.0, color=None ):
        
        pixX, pixY= self.toFrame( 0, 0 )
        pixStep= step*self._scale

        while pixX > pixStep :
            pixX-= pixStep
        
        while pixY > pixStep :
            pixY-= pixStep
        
        width= self._support.width()
        height= self._support.height()

        if not color :
            color= self._panel[0].stroke
        
        # Vertical
        for i in range( (int)(width/pixStep)+1 ) :
            self._support.traceLine( pixX+(pixStep*i), 10, pixX+(pixStep*i), height-10, color, 2 )
        # Horizontal
        for i in range( (int)(height/pixStep)+1 ) :
            self._support.traceLine( 10, pixY+(pixStep*i), width-10, pixY+(pixStep*i), color, 2 )
        return self

    def drawFrameAxes( self ):
        brush= Brush( 0xE26060,  0xE26060, 6 )
        self.traceLine(  0, 0, 1, 0, brush )
        brush.stroke= 0x60E260
        self.traceLine(  0, 0, 0, 1, brush )
        brush.stroke= 0x0606E2
        self.tracePoint( 0, 0, brush )
        return self
    
    # Drawing board:
    def drawShape( self, envelop, brushId=0, px=0, py=0 ):
        self.drawPolygon(
            [p[0]+px for p in envelop],
            [p[1]+py for p in envelop],
            self._panel[ brushId%len(self._panel) ]
        )
    
    def drawTile( self, aTile ):
        env= aTile.envelope()
        self.drawPolygon(
            [p[0] for p in env],
            [p[1] for p in env],
            self._panel[ aTile.type() ]
        )

    def writeTile( self, aTile ):
        minx, miny= aTile.box()[0]
        x, y= aTile.center()
        x= x+(minx-x)/2
        y= y+(miny-y)/2
        self.write( x, y, str(aTile.number()), self._panel[ aTile.type() ] )

    def drawBoardNetwork( self, aBoard ):
        for tile in aBoard.tiles() :
            cx, cy= tile.center()
            self.tracePoint( cx, cy, self._panel[ tile.type() ] )

        for fromId, toId in aBoard.edges() :
            fromX, fromY= aBoard.tile( fromId ).center()
            brush= self._panel[ aBoard.tile( fromId ).type() ]
            toX, toY= aBoard.tile( toId ).center()
            self.traceLine( fromX, fromY, toX, toY, brush )
        #    self.tracePoint( aBoard.tile(fromId) )

    def drawBoardTiles( self, aBoard ):
        for tile in aBoard.tiles() :
            self.drawTile( tile )

    def writeBoardTiles( self, aBoard ):
        for tile in aBoard.tiles() :
            self.writeTile( tile )

    def drawBoard( self, aBoard ):
        self.drawBoardNetwork(aBoard)
        self.drawBoardTiles(aBoard)
        self.writeBoardTiles(aBoard)

    # Control:
    def flip(self):
        h= self._support.height()
        w= self._support.width()
        ref= self._support.flip()
        self._support.fillPolygon(
            [0, 0, w, w],
            [0, h, h, 0],
            self._panel[0].fill
        )
        return ref
