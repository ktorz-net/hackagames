#!env python3
"""
HackaGame - Game - Single421 
"""
import sys

import warnings, hacka, random
from .. import py421

class d6 :
    _dots= [ [], [(4, 4)], [(2, 2), (6, 6)], [(2, 2), (4, 4), (6, 6)],
           [(2, 2), (2, 6), (6, 2), (6, 6)], [(2, 2), (2, 6), (4, 4), (6, 2), (6, 6)],
           [(2, 2), (2, 6), (4, 2), (4, 6), (6, 2), (6, 6)] ]

    def img( face ):
        img= [
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        for i, j in d6._dots[face] :
            img[i][j]= 1
        return img
    
    def shell( img ):
        pixs= [ [ ' ', '▄' ], ['▀', '█'] ]

        shellimg= ""
        for i in range( 1, len(img), 2 ) :
            for a, b in zip( img[i-1], img[i] ) :
                shellimg+= pixs[a][b]
            shellimg+='\n'

        if len( img ) % 2 == 1 :
            for a in img[-1] :
                shellimg+= pixs[a][0]
        else :
            shellimg= shellimg[:-1]
        
        return shellimg

class GameSolo( py421.GameSolo ) :

    def __init__( self, randomSeed= True ):
        super().__init__()
        self._random= randomSeed
        if type(self._random) == int :
            random.seed( self._random )

    def playerHand( self, iPlayer ):
        # Return the game elements in the player vision (an AbsGamel)
        gameElements= hacka.Pod( '421-Solo', [9, 9] )
        gameElements.append( hacka.Pod( 'Status', [ self.engine.turn() ], [ self.engine.currentScore() ] ) )

        handimg= [ [] for i in range(9) ]
        dices= [d for d in self.engine.dices()]
        if self._random :
            random.shuffle(dices)

        for d in dices :
            for line, handline in zip(d6.img(d), handimg) :
                handline+= line + [0]
        
        for handline in handimg :
            gameElements.append( hacka.Pod( 'Img', handline[:-1] ) )
        
        return gameElements

class GameDuo( py421.GameDuo ) :
    pass

class GameMaster( hacka.SequentialGameMaster ):
    def __init__( self, mode= "Solo" ):
        if mode == "Solo" :
            game= GameSolo()
        elif mode == "Duo" :
            game= GameDuo()
        else :
            warnings.warn('Py421::GameMaster: Unrecognized mode, should be "Solo" or "Duo"')
            game= GameSolo()
        super().__init__( game, game.numberOfPlayer() )

def command():
    from hacka.command import Command, Option

    cmd= Command( "play",
    [
        Option( "port", "p", default=1400 ),
        Option( "number", "n", 1, "number of games" )
    ],
    "Play to hackagames bi421. ARGUMENTS can be: Solo or Duo" )

    # Process the command line: 
    cmd.process()
    if not cmd.ready() :
        print( cmd.help() )
        return False
    return cmd

def play():
    from hacka.player import PlayerShell
    from .firstBot import Bot as Opponent

    # Process the command line: 
    cmd= command()
    if not cmd :
        exit()

    # Start the player the command line: 
    if cmd.argument() in [ "Duo", "duo" ] :
        gameMaster= GameMaster("Duo")
        gameMaster.launchLocal(  [PlayerShell(), Opponent()], cmd.option("number") )  
    else :
        gameMaster= GameMaster("Solo")
        gameMaster.launchLocal(  [PlayerShell()], cmd.option("number") )  

def launch():
    # Process the command line: 
    cmd= command()
    if not cmd :
        exit()

   # Start the player the command line: 
    mode= "Solo"
    if cmd.argument() in [ "Duo", "duo" ] :
        mode= "Duo"
    
    gameMaster= GameMaster(mode)
    gameMaster.launchOnNet( cmd.option("number"), cmd.option("port") )
