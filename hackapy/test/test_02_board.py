# HackaGames UnitTest - `pytest`

import hackapy.board as sujet

# ------------------------------------------------------------------------ #
#         T E S T   H A C K A G A M E S - C O M P O N E N T
# ------------------------------------------------------------------------ #

def test_Cell_init():
    cell= sujet.Cell()
    assert cell.number() == 0
    assert cell.edges() == []
    assert cell.coordinates() == (0.0, 0.0)

def test_Cell_initFilled():
    cell= sujet.Cell(3, 2.5, 8.9)
    assert cell.number() == 3
    assert cell.edges() == []
    assert cell.coordinates() == (2.5, 8.9)

def test_Cell_construction():
    cell= sujet.Cell(3)
    assert cell.number() == 3
    assert cell.edges() == []
    
    cell.connect(2)
    cell.connect(3)
    cell.connect(1)
    cell.connect(2)

    assert cell.edges() == [ [3, 1], [3, 2], [3, 3] ]

def test_Cell_str():
    cell= sujet.Cell(3)

    print(f">>> {cell}")

    assert str(cell) == "Cell-3 coords: [0.0, 0.0] adjs: []"

    cell.connectAll( [1, 2, 3] )
    cell.setCoordinates(1.4, 2.0)
    
    print(f">>> {cell}")

    assert str(cell) == "Cell-3 coords: [1.4, 2.0] adjs: [1, 2, 3]"


def test_Cell_pod():
    cell= sujet.Cell(3, 1.4, 2.0)
    cell._adjacencies= [1, 2, 3]
    cellPod= cell.asPod()

    print(f">>> {cellPod}")

    assert str(cellPod) == "Cell-3: flags: [3, 1, 2, 3] values: [1.4, 2.0]"
    
    cellBis= sujet.Cell().fromPod(cellPod)

    assert cell.number() == 3
    assert cellBis.edges() == [ [3, 1], [3, 2], [3, 3] ]
    assert cellBis.coordinates() == ( 1.4, 2.0 )


def test_Cell_pieces():
    cell= sujet.Cell(3)
    cell._adjacencies= [1, 2, 3]

    assert cell.pieces() == []


def test_Board_init():
    board= sujet.Board(3)
    assert board.cell(1).number() == 1
    assert board.cell(2).number() == 2
    assert board.cell(3).number() == 3
    assert board.cells() == [ board.cell(1), board.cell(2), board.cell(3) ]
    assert board.edges() == []


def test_Board_construction():
    board= sujet.Board(3)
    assert board.cell(1).adjacencies() == []
    assert board.cell(2).adjacencies() == []
    assert board.cell(3).adjacencies() == []
    board.connect(1, 2)
    board.connect(1, 3)
    board.connect(2, 2)
    board.connect(2, 1)
    board.connect(3, 1)
    board.connect(3, 2)
    board.connect(3, 3)
    assert board.cell(1).adjacencies() == [2, 3]
    assert board.cell(2).adjacencies() == [1, 2]
    assert board.cell(3).adjacencies() == [1, 2, 3]
    assert board.edges() == [ [1, 2], [1, 3], [2, 1], [2, 2], [3, 1], [3, 2], [3, 3] ]
    idBoard= id(board)
    board.__init__(3)
    board.connectAll( [ [1, 3], [1, 1], [2, 2], [2, 1], [3, 2], [3, 2] ] )
    print(f">>> {board.edges()}")
    assert( idBoard == id(board) )
    assert board.edges() == [ [1, 1], [1, 3], [2, 1], [2, 2], [3, 2] ]


def test_Board_str():
    board= sujet.Board(3)
    board.connectAll( [ [1, 3], [1, 1], [2, 2], [2, 1], [3, 2], [3, 2] ] )

    print( f">>> {board}" )

    assert "\n"+str(board)+"\n" == """
Board:
- Cell-1 coords: [0.0, 0.0] adjs: [1, 3]
- Cell-2 coords: [0.0, 0.0] adjs: [1, 2]
- Cell-3 coords: [0.0, 0.0] adjs: [2]
"""

def test_Board_pod():
    board= sujet.Board(3)
    boardPod= board.asPod()

    print(f">>> {boardPod}")

    assert '\n'+ str(boardPod) +'\n' == """
Board:
- Cell-1: flags: [1] values: [0.0, 0.0]
- Cell-2: flags: [2] values: [0.0, 0.0]
- Cell-3: flags: [3] values: [0.0, 0.0]
"""

    boardBis= sujet.Board().fromPod(boardPod)

    assert boardBis.size() == 3
    assert boardBis.edges() == []

    board.connectAll( [ [1, 3], [1, 1], [2, 2], [2, 1], [3, 2], [3, 2] ] )

    boardPod= board.asPod()

    print(f">>> {boardPod}")

    assert '\n'+ str(boardPod) +'\n' == """
Board:
- Cell-1: flags: [1, 1, 3] values: [0.0, 0.0]
- Cell-2: flags: [2, 1, 2] values: [0.0, 0.0]
- Cell-3: flags: [3, 2] values: [0.0, 0.0]
"""

    boardBis= sujet.Board().fromPod(boardPod)

    assert boardBis.size() == 3
    assert boardBis.edges() == [ [1, 1], [1, 3], [2, 1], [2, 2], [3, 2] ]
   
def t_est_Board_connection():
    board= sujet.Board(3)
    board.connect(1, 2)
    board.connect(2, 2)
    board.connect(2, 3)
    board.connect(3, 2)
    assert "\n"+str(board) == """
Board
- Cell-1
- Edge-1 [2]
- Cell-2
- Edge-2 [2, 3]
- Cell-3
- Edge-3 [2]"""

    assert board.edgesFrom(1) == [2]
    assert board.edgesFrom(2) == [2, 3]
    assert board.edgesFrom(3) == [2]
    
    assert board.isEdge(1, 2)
    assert board.isEdge(2, 2)
    assert board.isEdge(3, 2)
    assert not board.isEdge(2, 1)
    assert not board.isEdge(1, 3)
    assert not board.isEdge(3, 1)
  
def t_est_Board_iterator():
    board= sujet.Board(3)
    board.connect(1, 2)
    board.connect(2, 2)
    board.connect(2, 3)
    board.connect(3, 2)

    ref= [
        [ "Cell-1", [2]],
        [ "Cell-2", [2, 3]],
        [ "Cell-3", [2] ]
    ]
    i= 0
    for cell, edges in board :
        assert board.iCell() == i+1
        assert str(cell) == ref[i][0]
        assert edges == ref[i][1]
        i+=1