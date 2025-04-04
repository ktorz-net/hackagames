import sys
workDir= __file__.split('/tests/')[0]
sys.path.insert( 1, workDir )

# Import a game and player(s):
from src.hacka.games.py421 import GameSolo, GameDuo
from src.hacka.games.py421.firstBot import Bot

# ------------------------------------------------------------------------ #
#                   T E S T   4 2 1 - D U O   G A M E
# ------------------------------------------------------------------------ #

# Test firstAI launch
def test_421duo_init():
    subject= GameDuo()
    aPod= subject.initialize()
    assert str(aPod) == 'Game: 421-Duo'

    assert subject.refDices() == [0, 0 ,0]
    assert subject._lastPlayer == 0

    dices= subject.engine.dices()

    assert dices[0] in [1, 2, 3, 4, 5, 6]
    assert dices[1] in [1, 2, 3, 4, 5, 6]
    assert dices[2] in [1, 2, 3, 4, 5, 6]

    diceCount= [ 0 for i in range(7) ]
    for i in range(100000) :
        subject.initialize()
        for dValue in subject.engine.dices() :
            diceCount[dValue]+= 1
    

    diceCount= [ round(x/100000.0, 1) for x in diceCount ]
    assert diceCount == [0.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

    subject.engine.setOnStateStr( "2-6-3-1" )
    assert subject.engine.stateStr() == "2-6-3-1"

    print( subject.playerHand(1) )
    assert str( subject.playerHand(1) ).splitlines() == [
        "Game: 421-Duo",
        "- Horizon: [2]",
        "- Dices: [6, 3, 1] [106]",
        "- Opponent: [0, 0, 0] [0]"]

    print( subject.playerHand(2) )

    assert str( subject.playerHand(2) ).splitlines() == [
        "Game: 421-Duo",
        "- Horizon: [0]",
        "- Dices: [0, 0, 0] [0]",
        "- Opponent: [6, 3, 1] [106]"]

def test_421duo_play():
    subject= GameDuo()
    aPod= subject.initialize()
    subject.engine.setOnStateStr( "2-6-3-1" )

    assert subject.applyPlayerAction( 1, "roll-keep-keep" ) == False
    assert subject._lastPlayer == 0
    assert subject.applyPlayerAction( 1, "roll-keep-keep" ) 
    assert subject._lastPlayer == 1
    assert subject.applyPlayerAction( 2, "r-r-r" ) == False
    assert subject._lastPlayer == 1
    assert subject.applyPlayerAction( 2, "keep-keep-keep" ) 
    assert subject._lastPlayer == 2

# Test firstAI launch
def test_421duo_score():
    subject= GameDuo()
    subject.initialize()
    subject._refDices= [1, 1 ,1]

    subject.engine.setOnStateStr( "0-4-2-1" )
    assert subject.playerScore( 1 ) == -1
    assert subject.playerScore( 2 ) == 1

    subject.engine.setOnStateStr( "0-6-2-1" )
    assert subject.playerScore( 1 ) == 1
    assert subject.playerScore( 2 ) == -1

    subject.engine.setOnStateStr( "0-6-1-1" )
    assert subject.playerScore( 1 ) == 1
    assert subject.playerScore( 2 ) == -1

    subject.engine.setOnStateStr( "0-6-5-4" )
    assert subject.playerScore( 1 ) == 1
    assert subject.playerScore( 2 ) == -1

    subject.engine.setOnStateStr( "0-1-1-1" )
    assert subject.playerScore( 1 ) == 0
    assert subject.playerScore( 2 ) == 0

def test_421_firstbot_functions():
    # Instanciate them:
    game= GameSolo()
    bot= Bot()
    
    bot.wakeUp( 1, 1, game.initialize() )
    bot.perceive( game.playerHand(1) )

def test_421_firstbot_launch():
    # Instanciate them:
    game= GameSolo()
    bot= Bot()

    # Start 1000 games on a player to test:
    results= game.testPlayer( bot, 1000 )
    print( f"Average score: {sum(results)/len(results)}" )

    assert len(results) == 1000
    average= sum(results)/len(results)
    assert 140 < average and average < 180
    # And analyze the result:
