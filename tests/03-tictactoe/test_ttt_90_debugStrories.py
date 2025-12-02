# Local HackaGame:
import sys

sys.path.insert(1, __file__.split('tests')[0])
from src.hackagames.tictactoe import Game

# ------------------------------------------------------------------------ #
#                   T E S T   T I C T A C T O E    G A M E
# ------------------------------------------------------------------------ #

#------------------------------------------------------------------------------------------------
# Test Initialize
#------------------------
def test_risky_play():
  game= Game()
  game.initialize()
  assert True
