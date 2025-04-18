# ai/train_chess.py
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engines.chess_engine import ChessGame
from ai.chess_q_learning import ChessQLearningAgent
import random
from tqdm import tqdm

def train_chess_agent(episodes=10000):
    agent = ChessQLearningAgent()
    game = ChessGame()

    for episode in tqdm(range(episodes)):
        state = game.reset()
        done = False
        moves = []

        while not game.game_over():
            actions = game.get_available_actions()
            action = agent.choose_action(state, actions)

            # Save move history for reward updates
            moves.append((state, action))

            valid = game.make_move(action)
            if not valid:
                continue

            next_state = game.get_state()
            next_actions = game.get_available_actions()
            state = next_state

        # Assign rewards based on result
        result = game.get_result()
        if result == "checkmate":
            reward = 1 if len(moves) % 2 == 1 else -1  # last mover wins
        elif result == "draw" or result == "stalemate":
            reward = 0.5
        else:
            reward = 0  # unknown

        # Backpropagate reward
        for i in reversed(range(len(moves))):
            state_i, action_i = moves[i]
            next_state_i = moves[i + 1][0] if i + 1 < len(moves) else state
            next_actions_i = game.get_available_actions()
            agent.update_q(state_i, action_i, reward, next_state_i, next_actions_i)
            reward *= 0.9  # decay reward as we move backward

    agent.save_q_table()
    print("✅ Training complete! Q-table saved.")

if __name__ == "__main__":
    # train_chess_agent(episodes=10000)
    train_chess_agent(episodes=1000)
