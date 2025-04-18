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
