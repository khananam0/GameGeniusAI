# play/play_chess_vs_ai.py

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engines.chess_engine import ChessGame
from ai.chess_q_learning import ChessQLearningAgent

def play_game():
    game = ChessGame()
    agent = ChessQLearningAgent()
    agent.load_q_table()

    state = game.reset()
    print("\n🎮 Chess Game vs GameGenius AI")
    print("Enter your moves in UCI format (e.g., e2e4, g8f6)")
    print("You play as White. AI is Black.\n")

    game.render()

    while not game.game_over():
        # Human plays (White)
        user_move = input("\nYour move: ")
        if not game.make_move(user_move):
            print("❌ Invalid move. Try again.")
            continue

        game.render()
        if game.game_over():
            break

        # AI plays (Black)
        state = game.get_state()
        actions = game.get_available_actions()
        ai_move = agent.choose_action(state, actions)

        print(f"\n🤖 AI move: {ai_move}")
        game.make_move(ai_move)
        game.render()

    print("\n🏁 Game Over:", game.get_result())

if __name__ == "__main__":
    play_game()




"""python play/play_chess_vs_ai.py
"""