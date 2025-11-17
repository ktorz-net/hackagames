import sys
workDir= __file__.split('/tests/')[0]
sys.path.insert( 1, workDir )

# Import a game and player(s):
from hacka import Pod
import hacka
from src.hackagames.connect4 import Game, Connect4Master
from src.hackagames.connect4.firstBot import Bot

# ------------------------------------------------------------------------ #
#              T E S T   4 2 1 - F I R S T   P L A Y E R
# ------------------------------------------------------------------------ #

def test_connect4_firstbot_functions():
    # Instanciate them:
    game= Game()
    bot= Bot()
    
    bot.wakeUp( 1, 1, game.initialize() )
    bot.perceive( game.playerHand(1) )
    action= bot.decide()
    assert type(action) == Pod

def test_connect4_launch():
    # Instanciate them:
    game= Game()
    bot= Bot()

    # Start 10 games on a player to test:
    gameMaster= hacka.SequentialGameMaster( game, 2 )
    game.initialize()

    # LaunchLocal:
    tabletop= hacka.interprocess.TabletopLocal( [bot, bot] )
    #launchWithTabletop
    print( f'HackaGame: wait for 2 players' )
    tabletop.waitForPlayers(1)
    tabletop.waitForPlayers(2)
    print( f'HackaGame: process one game' )

    action= tabletop.activatePlayer( 1, game.playerHand(1) )
    assert type(action) == hacka.Pod
    print( f"Action: {action}" )

    assert game.applyAction(1, action)
    gameMaster.play(tabletop)
    
    action= tabletop.activatePlayer( 2, game.playerHand(2) )
    assert type(action) == hacka.Pod
    print( f"Action: {action}" )

    assert game.applyAction(2, action)
    gameMaster.play(tabletop)
    

    print( f'HackaGame: stop player-clients' )
    tabletop.stopPlayer(1)
    tabletop.stopPlayer(2)
    print( tabletop.results() )

def test_421_GameMaster():
    gameMaster= Connect4Master()
    results= gameMaster.launchLocal( [Bot(), Bot()], 100 )

    results= results[0]
    print( results )
    print( f"Average score: {sum(results)/len(results)}" )
    
    assert len(results) == 100
    average= sum(results)/len(results)
    assert -0.2 < average and average < +0.2
