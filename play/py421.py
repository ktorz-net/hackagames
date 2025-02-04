#!python3
"""
HackaGames - Py421
"""
from hacka.py.player import PlayerIHM as Player
from hacka.command import Command, Option

from hacka.games.py421 import GameSolo, GameDuo
from hacka.games.py421.firstBot import Bot as Opponent

# Define a command interpreter: 2 options: host address and port:
cmd= Command(
    "play",
    [
        Option( "number", "n", 1, "number of games" )
    ],
    "Play to hackagames py421. ARGUMENTS can be: solo or duo" )

# Process the command line: 
cmd.process()
if not cmd.ready() :
    print( cmd.help() )
    exit()

# Start the player the command line: 
if cmd.argument() == "duo" :
  game= GameDuo()
  player1= Player()
  game.launch( [player1, Opponent()], cmd.option("number") )  
else :
  game= GameSolo()
  player1= Player()
  game.launch( [player1], cmd.option("number") )
