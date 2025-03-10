#!env python3
"""
HackaGame - Game - Connect4
"""
import sys
sys.path.insert( 1, __file__.split('play')[0] )

import src.hacka.games.connect4 as c4
from src.hacka.command import Command, Option
from src.hacka.games.connect4.shell import Interface as Player
from src.hacka.games.connect4.firstBot import Bot as Oponent

# Define a command interpreter: 2 options: host address and port:
cmd= Command(
    "start-interactive",
    [
        Option( "number", "n", 1, "number of games" )
    ],
    "Start interactive gameConnect4. gameConnect4 do not take ARGUMENT." )

# Process the command line: 
cmd.process()
if not cmd.ready() :
    print( cmd.help() )
    exit()

game= c4.GameConnect4()
player= Player()

game.launch( [player, Oponent()], cmd.option("number") )
