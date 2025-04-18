# play/play_chess_with_commentary.py

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import spacy
from engines.chess_engine import ChessGame
from ai.chess_q_learning import ChessQLearningAgent

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

def generate_commentary(move):
    """
    Generate basic commentary for each chess move.
    This is where the NLP magic happens!
    """
    doc = nlp(move)
    commentary = f"Move: {move}. "
    
    # Add basic commentary based on the move type
    if "e" in move or "d" in move:
        commentary += "Classic central control."
    elif "N" in move:
        commentary += "A knight leaps forward."
    elif "B" in move:
        commentary += "Bishop targeting the long diagonal."
    elif "Q" in move:
        commentary += "The Queen enters the action."
    elif "K" in move:
        commentary += "King making a cautious move."

    return commentary

def play_game_with_commentary():
    game = ChessGame()
    agent = ChessQLearningAgent()
    agent.load_q_table()

    state = game.reset()
    print("\n🎮 Chess Game with Commentary")
    print("You play as White. AI is Black.\n")

    game.render()

    while not game.game_over():
        # Human plays (White)
        user_move = input("\nYour move (in UCI format, e.g., e2e4): ")
        if not game.make_move(user_move):
            print("❌ Invalid move. Try again.")
            continue

        # Generate commentary for user move
        print(generate_commentary(user_move))
        game.render()

        if game.game_over():
            break

        # AI plays (Black)
        state = game.get_state()
        actions = game.get_available_actions()
        ai_move = agent.choose_action(state, actions)

        print(f"\n🤖 AI move: {ai_move}")
        print(generate_commentary(ai_move))
        game.make_move(ai_move)
        game.render()

    print("\n🏁 Game Over:", game.get_result())

if __name__ == "__main__":
    play_game_with_commentary()
