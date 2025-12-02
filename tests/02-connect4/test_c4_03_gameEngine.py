import sys, pathlib
workdir= __file__.split('/tests/')[0]
sys.path.insert( 1, workdir )

"""
Test - Connect4.Engine
"""

import hacka as hk
import src.hackagames.connect4 as connect4

def assert_multiline( text1, text2 ) :
    print( f"--- --- ---\n{text1}\nvs\n{text2}" )
    ml1= text1.split("\n")
    ml2= text2.split('\n')
    assert( len(ml1) == len(ml2) )
    for l1, l2 in zip(ml1, ml2) :
        assert( l1 == l2 )

def test_initialize():
    game= connect4.Game( 5, 4 )
    pod= game.initialize()

    test= ( "Connect4 : 5 4 :" )
    assert_multiline( str(pod), test )
    
    game= connect4.Game()
    pod= game.initialize()

    test= ( "Connect4 : 7 6 :" )
    assert_multiline( str(pod), test )

    grid= connect4.Grid().initializeFrom( game.playerHand(1) ) 

    test= ( "  A   B   C   D   E   F   G\n"
            "|   |   |   |   |   |   |   |\n"
            "|   |   |   |   |   |   |   |\n"
            "|   |   |   |   |   |   |   |\n"
            "|   |   |   |   |   |   |   |\n"
            "|   |   |   |   |   |   |   |\n"
            "|   |   |   |   |   |   |   |\n"
            "-----------------------------" )
    assert_multiline( str(grid), test )

def test_play():
    game= connect4.Game()
    pod= game.initialize()

    assert( game.applyAction(1, hk.Pod("B")) )
    assert( game.applyAction(2, hk.Pod("A")) )
    assert( game.applyAction(1, hk.Pod("A")) )
    assert( game.applyAction(2, hk.Pod("B")) )
    assert( game.applyAction(1, hk.Pod("G")) )
    assert( game.applyAction(2, hk.Pod("G")) )
    assert( game.applyAction(1, hk.Pod("E")) )
    assert( game.applyAction(2, hk.Pod("E")) )
    assert( game.applyAction(1, hk.Pod("B")) )
    assert( game.applyAction(2, hk.Pod("B")) )
    assert( game.applyAction(1, hk.Pod("B")) )
    assert( game.applyAction(2, hk.Pod("C")) )

    grid1= connect4.Grid().initializeFrom( game.playerHand(1) ) 
    grid2= connect4.Grid().initializeFrom( game.playerHand(2) ) 

    test= ( "  A   B   C   D   E   F   G\n"
            "|   |   |   |   |   |   |   |\n"
            "|   | O |   |   |   |   |   |\n"
            "|   | X |   |   |   |   |   |\n"
            "|   | O |   |   |   |   |   |\n"
            "| O | X |   |   | X |   | X |\n"
            "| X | O | X |   | O |   | O |\n"
            "-----------------------------" )
    
    assert_multiline( str(grid1), test )
    assert_multiline( str(grid2), test )

    assert( not game.isEnded() )
    assert( game.playerScore(1) == 0 )
    assert( game.playerScore(2) == 0 )

    assert( game.applyAction(1,  hk.Pod("F")) )
    assert( game.applyAction(2,  hk.Pod("C")) )
    assert( game.applyAction(1,  hk.Pod("D")) )

    grid1= connect4.Grid().initializeFrom( game.playerHand(1) ) 
    grid2= connect4.Grid().initializeFrom( game.playerHand(2) ) 

    test= ( "  A   B   C   D   E   F   G\n"
            "|   |   |   |   |   |   |   |\n"
            "|   | O |   |   |   |   |   |\n"
            "|   | X |   |   |   |   |   |\n"
            "|   | O |   |   |   |   |   |\n"
            "| O | X | X |   | X |   | X |\n"
            "| X | O | X | O | O | O | O |\n"
            "-----------------------------" )
    
    assert_multiline( str(grid1), test )
    assert_multiline( str(grid2), test )

    assert( game.isEnded() )
    assert( game.playerScore(1) == 1 )
    assert( game.playerScore(2) == -1 )

def test_statusquo():
    game= connect4.Game()
    game.initialize()

    game._grid._pos =[
        [2,1,2, 2,2,1],
        [1,1,2, 1,2,0],
        [1,2,1, 2,2,1],
        [1,2,2, 1,1,2],
        [2,1,1, 2,2,1],
        [2,1,2, 2,1,0],
        [2,1,1, 1,2,1]
    ]

    test= ( "      B               F    \n"
            "| O |   | O | X | O |   | O |\n"
            "| X | X | X | O | X | O | X |\n"
            "| X | O | X | O | X | X | O |\n"
            "| X | X | O | X | O | X | O |\n"
            "| O | O | X | X | O | O | O |\n"
            "| X | O | O | O | X | X | X |\n"
            "-----------------------------" )
    
    assert_multiline( str(game._grid), test )

    assert( not game.isEnded() )
    assert( game.playerScore(1) == 0 )
    assert( game.playerScore(2) == 0 )

    assert( game.applyAction(1, hk.Pod("F")) )
    assert( game.applyAction(2, hk.Pod("B")) )

    assert( game.isEnded() )
    assert( game.playerScore(1) == 0 )
    assert( game.playerScore(2) == 0 )