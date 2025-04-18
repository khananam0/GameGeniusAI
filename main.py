# main.py

from engines.tictactoe_engine import TicTacToe
from ai.q_learning import QLearningAgent
import os

def print_board(board):
    symbols = {0: ".", 1: "O", -1: "X"}
    print("\nBoard:")
    for row in board:
        print(" ".join(symbols[val] for val in row))
    print()

def get_user_move(game):
    while True:
        try:
            move = input("Enter your move (row col): ").strip().split()
            if len(move) != 2:
                raise ValueError
            row, col = int(move[0]), int(move[1])
            if (row, col) in game.get_available_actions():
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter valid row and column numbers.")

def play_game():
    game = TicTacToe()
    agent = QLearningAgent()
    q_table_path = "data/q_table.pkl"

    if not os.path.exists(q_table_path):
        print("⚠️ Trained Q-table not found. Please run ai/train.py first.")
        return

    agent.load_q_table(q_table_path)
    print("🎮 Welcome to GameGeniusAI Tic-Tac-Toe!")
    print("You are X (Player -1). AI is O (Player 1).")
    
    state = game.reset()
    current_player = -1  # Human goes first

    while not game.game_over():
        print_board(game.board)
        available = game.get_available_actions()

        if current_player == -1:
            action = get_user_move(game)
        else:
            action = agent.choose_action(state, available)
            print(f"🤖 AI chooses: {action}")

        game.make_move(action[0], action[1], current_player)
        state = game.get_state()
        current_player *= -1

    print_board(game.board)

    if game.current_winner == 1:
        print("🤖 AI wins! Better luck next time.")
    elif game.current_winner == -1:
        print("🎉 You win! Great job!")
    else:
        print("🤝 It's a draw!")

if __name__ == "__main__":
    play_game()

