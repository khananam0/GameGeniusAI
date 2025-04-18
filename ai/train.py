# ai/train.py

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



""" This code is the part of tinker module where we trained the model and it was supporting but in ui it is causing some issue.
      That is why commenting it."""


from engines.tictactoe_engine import TicTacToe
from ai.q_learning import QLearningAgent
import numpy as np
import random

# Make sure data folder exists
os.makedirs("data", exist_ok=True)

def train_agent(episodes=10000):
    game = TicTacToe()
    agent = QLearningAgent()
    total_wins = 0
    total_draws = 0
    total_losses = 0

    for ep in range(episodes):
        state = game.reset()
        done = False
        current_player = 1  # 1 = AI, -1 = opponent (random)

        while not done:
            available_actions = game.get_available_actions()

            if current_player == 1:
                # AI agent's turn
                action = agent.choose_action(state, available_actions)
            else:
                # Opponent (random moves)
                action = random.choice(available_actions)

            valid = game.make_move(action[0], action[1], current_player)
            next_state = game.get_state()
            done = game.game_over()
            next_available = game.get_available_actions()

            if current_player == 1:
                if done:
                    if game.current_winner == 1:
                        reward = 1
                        total_wins += 1
                    elif game.current_winner == -1:
                        reward = -1
                        total_losses += 1
                    else:
                        reward = 0.5
                        total_draws += 1
                else:
                    reward = 0
                agent.learn(state, action, reward, next_state, next_available, done)

            state = next_state
            current_player *= -1  # Switch turns

        if (ep + 1) % 1000 == 0:
            print(f"Episode {ep+1}/{episodes} — Wins: {total_wins}, Draws: {total_draws}, Losses: {total_losses}")

    agent.save_q_table()
    print("\n✅ Training complete. Q-table saved to data/q_table.pkl")

if __name__ == "__main__":
    import random
    train_agent()


"""
run the train file using command = python -m ai.train
"""



# """ This code is used for streamlit, it is not used in tinker module. wrting this new code for streamlit module."""

# # ai/train_tictactoe_q.py

# import numpy as np
# import random
# from engines.tictactoe_engine import TicTacToeGame
# from ai.q_learning import QLearningAgent

# EPISODES = 10000
# game = TicTacToeGame()
# agent = QLearningAgent(alpha=0.1, gamma=0.9, epsilon=0.2)

# for episode in range(EPISODES):
#     board = ["-"] * 9
#     done = False

#     while not done:
#         state = "".join(board)
#         move = agent.choose_action(state, board)
#         new_board = board.copy()
#         game.make_move(new_board, move, "X")
#         winner = game.check_winner(new_board)

#         if winner:
#             reward = 1 if winner == "X" else -1 if winner == "O" else 0.5
#             agent.learn(state, move, "".join(new_board), reward)
#             done = True
#         else:
#             # Let opponent (random) move
#             opponent_moves = game.available_moves(new_board)
#             if opponent_moves:
#                 opp_move = random.choice(opponent_moves)
#                 game.make_move(new_board, opp_move, "O")
#                 winner = game.check_winner(new_board)
#                 if winner:
#                     reward = 1 if winner == "X" else -1 if winner == "O" else 0.5
#                     agent.learn(state, move, "".join(new_board), reward)
#                     done = True
#                 else:
#                     reward = 0
#                     agent.learn(state, move, "".join(new_board), reward)
#             else:
#                 done = True

# # Save the trained Q-table
# agent.save("data/tictactoe_q_table.npy")
# print("✅ Training complete. Q-table saved to data/tictactoe_q_table.npy")



