import sys
workDir= __file__.split('/tests/')[0]
sys.path.insert( 1, workDir )

# Import a game and player(s):
from hacka import Pod
import hacka
from src.hackagames.bi421 import GameMaster, GameSolo as Game
from src.hackagames.bi421.firstBot import Bot

# ------------------------------------------------------------------------ #
#              T E S T   4 2 1 - F I R S T   P L A Y E R
# ------------------------------------------------------------------------ #

def test_421_firstbot_functions():
    # Instanciate them:
    game= Game()
    bot= Bot()
    
    bot.wakeUp( 1, 1, game.initialize() )
    bot.perceive( game.playerHand(1) )
    action= bot.decide()
    assert type(action) == Pod

def test_421_firstbot_launch():
    # Instanciate them:
    game= Game()
    bot= Bot()

    # Start 1000 games on a player to test:
    gameMaster= hacka.SequentialGameMaster( game, 1 )
    game.initialize()

    # LaunchLocal:
    tabletop= hacka.interprocess.TabletopLocal( [bot] )
    #launchWithTabletop
    print( f'HackaGame: wait for 1 players' )
    tabletop.waitForPlayers(1)
    print( f'HackaGame: process one game' )

    action= tabletop.activatePlayer( 1, game.playerHand(1) )
    assert type(action) == hacka.Pod
    print( f"Action: {action}" )

    assert game.applyAction(1, action)
    gameMaster.play(tabletop)
    
    print( f'HackaGame: stop player-clients' )
    tabletop.stopPlayer(1)
    print( tabletop.results() )

    gameMaster.launchLocal( [bot], 10 )

def test_421_firstbot_GameMaster():
    # Solo:
    gameMaster= GameMaster("Solo")
    results= gameMaster.launchLocal( [Bot()], 1000 )

    results= results[0]
    print( results )
    print( f"Average score: {sum(results)/len(results)}" )
    
    assert len(results) == 1000
    average= sum(results)/len(results)
    assert 140 < average and average < 180

    # Duo:
    gameMaster= GameMaster("Duo")
    results= gameMaster.launchLocal( [Bot(), Bot()], 1000 )

    assert len(results) == 2
    for r in results:
        assert len(r) == 1000
        average= sum(r)/len(r)
        assert -0.1 < average and average < +0.1
    