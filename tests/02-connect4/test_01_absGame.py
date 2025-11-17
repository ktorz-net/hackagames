import sys, pathlib
workdir= __file__.split('/tests/')[0]
sys.path.insert( 1, workdir )

"""
Test - Connect4.Engine
"""

import hacka as hk
import src.hackagames.connect4 as ge

def test_gameMethod():
    game= ge.Game()

    assert( type( game.initialize().asPod() ) is hk.Pod  )
    assert( type( game.playerHand(1).asPod() ) is hk.Pod )
    assert( game.applyAction( 1, hk.Pod("test") )  )
    game.tic()
    assert( not game.isEnded() )
    assert( game.playerScore(1) == 0 )
