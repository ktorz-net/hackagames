import sys, pathlib
workdir= __file__.split('/tests/')[0]
sys.path.insert( 1, workdir )

from src.hackagames.connect4 import shell

"""
Test - Connect4.Shell
"""

def test_PlayerShell():
    player= shell.PlayerShell()