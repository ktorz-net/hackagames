import sys
workDir= __file__.split('/tests/')[0]
sys.path.insert( 1, workDir )

from src.hackagames.bi421 import d6, GameMaster, GameSolo as Game

# ------------------------------------------------------------------------ #
#                   T E S T   4 2 1 - S O L O   G A M E
# ------------------------------------------------------------------------ #

def test_421solo_init():
    game= Game(False)
    aPod= game.initialize()
    assert str(aPod) == '421-Solo : :'
    assert game.numberOfPlayer() == 1

    dices= game.engine.dices()

    assert dices[0] in [1, 2, 3, 4, 5, 6]
    assert dices[1] in [1, 2, 3, 4, 5, 6]
    assert dices[2] in [1, 2, 3, 4, 5, 6]

    diceCount= [ 0 for i in range(7) ]
    for i in range(100000) :
        game.initialize()
        for dValue in game.engine.dices() :
            diceCount[dValue]+= 1
    
    diceCount= [ round(x/100000.0, 1) for x in diceCount ]
    assert diceCount == [0.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

    game.engine.setOnStateStr( "2-6-3-1" )
    assert game.engine.stateStr() == "2-6-3-1"

    print( game.playerHand(1) )
    assert str( game.playerHand(1) ).splitlines() == [
        "421-Solo : 9 9 :",
        "- Status : 2 : 106",
        "- Img : 1 1 1 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1 1 :",
        "- Img : 1 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 1 :",
        "- Img : 1 0 1 0 0 0 1 0 1 0 1 0 1 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 1 :",
        "- Img : 1 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 1 :",
        "- Img : 1 0 1 0 0 0 1 0 1 0 1 0 0 0 1 0 0 0 1 0 1 0 0 0 1 0 0 0 1 :",
        "- Img : 1 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 1 :",
        "- Img : 1 0 1 0 0 0 1 0 1 0 1 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 0 1 :",
        "- Img : 1 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 1 :",
        "- Img : 1 1 1 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1 1 :"
    ]


def test_421solo_perceive():
    game= Game(False)
    game.initialize()
    game.engine.setOnStateStr( "2-6-3-1" )
    assert game.engine.stateStr() == "2-6-3-1"

    gameState= game.playerHand(1)
    imgSize= gameState.integer(1)

    assert len( gameState.children() ) == 1+imgSize

    horizon= gameState.child(1).integer(1)
    score= gameState.child(1).value(1)

    assert horizon == 2
    assert score == 106

    diceImage= [
        line.integers() for line in gameState.children()[1:2+imgSize]
    ]

    shellImg= d6.shell( diceImage )
    
    for l in diceImage :
        print( l )
    print( ">\n" + shellImg )

    assert shellImg.splitlines() == [
        "┌─────────────────────────────┐",
        "│█▀▀▀▀▀▀▀█ █▀▀▀▀▀▀▀█ █▀▀▀▀▀▀▀█│",
        "│█ ▀   ▀ █ █ ▀     █ █       █│",
        "│█ ▀   ▀ █ █   ▀   █ █   ▀   █│",
        "│█ ▀   ▀ █ █     ▀ █ █       █│",
        "│▀▀▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀▀▀│",
        "└─────────────────────────────┘"
    ]

# Test firstAI launch
def test_421solo_gameMaster():
    gameMaster= GameMaster()

    assert gameMaster.game().diceBox() == (11, 12)
    
    assert gameMaster.numberOfPlayers() == 1
    aPod= gameMaster.game().initialize()
    assert str(aPod) == '421-Solo : :'
    
    gameMaster= GameMaster("Solo")

    assert gameMaster.numberOfPlayers() == 1
    aPod= gameMaster.game().initialize()
    assert str(aPod) == '421-Solo : :'

# Test firstAI launch
def test_421solo_atRandom():
    game= Game(42)
    game.initialize()
    game.engine.setOnStateStr( "2-6-3-1" )

    gameState= game.playerHand(1)
    imgSize= gameState.integer(1)
    diceImage= [
        line.integers() for line in gameState.children()[1:2+imgSize]
    ]

    shellImg= d6.shell( diceImage )
    print( ">\n" + shellImg )
    assert shellImg.splitlines() == [
        "┌─────────────────────────────┐",
        "│█▀▀▀▀▀▀▀█ █▀▀▀▀▀▀▀█ █▀▀▀▀▀▀▀█│",
        "│█ ▀     █ █       █ █ ▀   ▀ █│",
        "│█   ▀   █ █   ▀   █ █ ▀   ▀ █│",
        "│█     ▀ █ █       █ █ ▀   ▀ █│",
        "│▀▀▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀▀▀│",
        "└─────────────────────────────┘"
    ]

    gameState= game.playerHand(1)
    imgSize= gameState.integer(1)
    diceImage= [
        line.integers() for line in gameState.children()[1:2+imgSize]
    ]

    shellImg= d6.shell( diceImage )
    print( ">\n" + shellImg )
    assert shellImg.splitlines() == [
        "┌─────────────────────────────┐",
        "│█▀▀▀▀▀▀▀█ █▀▀▀▀▀▀▀█ █▀▀▀▀▀▀▀█│",
        "│█ ▀     █ █ ▀   ▀ █ █       █│",
        "│█   ▀   █ █ ▀   ▀ █ █   ▀   █│",
        "│█     ▀ █ █ ▀   ▀ █ █       █│",
        "│▀▀▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀▀▀│",
        "└─────────────────────────────┘"
    ]

    gameState= game.playerHand(1)
    imgSize= gameState.integer(1)
    diceImage= [
        line.integers() for line in gameState.children()[1:2+imgSize]
    ]

    shellImg= d6.shell( diceImage )
    print( ">\n" + shellImg )
    assert shellImg.splitlines() == [
        "┌─────────────────────────────┐",
        "│█▀▀▀▀▀▀▀█ █▀▀▀▀▀▀▀█ █▀▀▀▀▀▀▀█│",
        "│█ ▀     █ █ ▀   ▀ █ █       █│",
        "│█   ▀   █ █ ▀   ▀ █ █   ▀   █│",
        "│█     ▀ █ █ ▀   ▀ █ █       █│",
        "│▀▀▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀▀▀│",
        "└─────────────────────────────┘"
    ]

    gameState= game.playerHand(1)
    imgSize= gameState.integer(1)
    diceImage= [
        line.integers() for line in gameState.children()[1:2+imgSize]
    ]

    shellImg= d6.shell( diceImage )
    print( ">\n" + shellImg )
    assert shellImg.splitlines() == [
        "┌─────────────────────────────┐",
        "│█▀▀▀▀▀▀▀█ █▀▀▀▀▀▀▀█ █▀▀▀▀▀▀▀█│",
        "│█ ▀   ▀ █ █ ▀     █ █       █│",
        "│█ ▀   ▀ █ █   ▀   █ █   ▀   █│",
        "│█ ▀   ▀ █ █     ▀ █ █       █│",
        "│▀▀▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀▀▀│",
        "└─────────────────────────────┘"
    ]

def test_421solo_floating():
    game= Game(42, 12)
    game.initialize()
    game.engine.setOnStateStr( "2-6-3-1" )

    assert game.diceBox() == (12, 12)
    game.setBox(11, 10)
    assert game.diceBox() == (11, 10)
    game.setBox(8, 11)
    assert game.diceBox() == (9, 11)
    game.setBox(3)
    assert game.diceBox() == (9, 9)
    game.setBox(11, 13)
    assert game.diceBox() == (11, 13)

    img= d6.floatingImage( [4, 2, 1], 11, 13 )
    assert len(img) == 13
    for line in img :
        assert len(line) == 11*3+2

    shellImg= d6.shell( d6.fullFloatingImage( [4, 2, 1], 11, 13 ) )
    print( ">\n" + shellImg )

    assert shellImg.splitlines() == [
        "┌───────────────────────────────────────┐",
        "│           █▀▀▀▀▀▀▀█                   │",
        "│           █ ▀     █  ▄▄▄▄▄▄▄▄▄        │",
        "│           █       █  █       █        │",
        "│█▀▀▀▀▀▀▀█  █     ▀ █  █   ▄   █        │",
        "│█ ▀   ▀ █  ▀▀▀▀▀▀▀▀▀  █       █        │",
        "│█       █             █▄▄▄▄▄▄▄█        │",
        "│█ ▀   ▀ █                              │",
        "│▀▀▀▀▀▀▀▀▀                              │",
        "│                                       │",
        "└───────────────────────────────────────┘"
    ]

    
    shellImg= d6.shell( d6.floatingImage( [3, 6, 5], 11, 12 ) )
    print( ">\n" + shellImg )

    assert shellImg.splitlines() == [
        "┌───────────────────────────────────┐",
        "│ ▀     █     ▄▄▄▄▄▄▄▄▄             │",
        "│   ▀   █     █ ▄   ▄ █             │",
        "│     ▀ █     █ ▄   ▄ █   █▀▀▀▀▀▀▀█ │",
        "│▀▀▀▀▀▀▀▀     █ ▄   ▄ █   █ ▀   ▀ █ │",
        "│             █▄▄▄▄▄▄▄█   █   ▀   █ │",
        "│                         █ ▀   ▀ █ │",
        "└───────────────────────────────────┘"
    ]


    shellImg= d6.shell( d6.floatingImage( [1, 1, 1], 11, 12 ) )
    print( ">\n" + shellImg )

    assert shellImg.splitlines() == [
        "┌───────────────────────────────────┐",
        "│                          █       █│",
        "│             █▀▀▀▀▀▀▀█    █   ▀   █│",
        "│▄▄▄▄▄▄▄▄     █       █    █       █│",
        "│       █     █   ▀   █    ▀▀▀▀▀▀▀▀▀│",
        "│   ▄   █     █       █             │",
        "│       █     ▀▀▀▀▀▀▀▀▀             │",
        "└───────────────────────────────────┘"
    ]


    shellImg= d6.shell( d6.floatingImage( [2, 4, 3], 11, 12 ) )
    print( ">\n" + shellImg )

    assert shellImg.splitlines() == [
        "┌───────────────────────────────────┐",
        "│    █▀▀▀▀▀▀▀█                      │",
        "│    █ ▀     █         █▀▀▀▀▀▀▀█    │",
        "│    █       █ █▀▀▀▀▀▀▀█ ▀     █    │",
        "│    █     ▀ █ █ ▀   ▀ █   ▀   █    │",
        "│    ▀▀▀▀▀▀▀▀▀ █       █     ▀ █    │",
        "│              █ ▀   ▀ █▀▀▀▀▀▀▀▀    │",
        "└───────────────────────────────────┘"
    ]


    shellImg= d6.shell( d6.floatingImage( [6, 1, 2], 11, 12 ) )
    print( ">\n" + shellImg )

    assert shellImg.splitlines() == [
        "┌───────────────────────────────────┐",
        "│▄▄▄▄▄▄▄▄            █ ▄     █      │",
        "│ ▄   ▄ █       ▄▄▄▄▄█       █      │",
        "│ ▄   ▄ █       █    █     ▄ █      │",
        "│ ▄   ▄ █       █   ▄█▄▄▄▄▄▄▄█      │",
        "│▄▄▄▄▄▄▄█       █       █           │",
        "│               █▄▄▄▄▄▄▄█           │",
        "└───────────────────────────────────┘"
    ]