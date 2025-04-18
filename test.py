# from engines.tictactoe_engine import TicTacToe

# game = TicTacToe()
# game.print_board()

# game.make_move(0, 0, 1)  # Player 1
# game.make_move(1, 1, -1)  # Opponent
# game.make_move(0, 1, 1)
# game.make_move(2, 2, -1)
# game.make_move(0, 2, 1)  # Player wins

# game.print_board()

# if game.game_over():
#     if game.current_winner:
#         print(f"Winner: {game.current_winner}")
#     else:
#         print("It's a draw!")



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""How to run this code:"""
# this is directory
# gamegenius_ai/
# ├── engines/
# │   └── tictactoe_engine.py
# ├── test_engine.py



# Then run from terminal:

# cd gamegenius_ai
# python test_engine.py





# ========================For chess to test use this============================
# test_chess_engine.py
from engines.chess_engine import ChessGame

game = ChessGame()
game.reset()
game.render()

while not game.game_over():
    moves = game.get_available_actions()
    move = input("Your move (in UCI format, e.g., e2e4): ")
    if not game.make_move(move):
        print("Invalid move!")
    game.render()

print("Game Over:", game.get_result())
