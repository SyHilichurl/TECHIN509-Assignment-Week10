from models.board import Board

def test_check_winner():
    board = Board()
    board.grid = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["X", "O", "X"]
    ]
    assert board.check_winner() == "X"

    board.grid = [
        ["O", "O", "X"],
        ["O", "X", "X"],
        ["O", "X", "O"]
    ]
    assert board.check_winner() == "O"

    board.grid = [
        ["O", "X", "O"],
        ["X", "O", "X"],
        ["X", "O", "X"]
    ]
    assert board.check_winner() == ""

    board.grid = [
        ["", "X", "O"],
        ["X", "O", "X"],
        ["X", "O", "O"]
    ]
    assert board.check_winner() == ""
    
