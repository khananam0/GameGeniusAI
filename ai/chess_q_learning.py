# ai/chess_q_learning.py
import pickle
import random
import os

class ChessQLearningAgent:
    def __init__(self, learning_rate=0.1, discount_factor=0.95, epsilon=0.2):
        self.q_table = {}  # {state (FEN): {action (UCI): value}}
        self.alpha = learning_rate
        self.gamma = discount_factor
        self.epsilon = epsilon

    def get_q(self, state, action):
        return self.q_table.get(state, {}).get(action, 0.0)

    # def choose_action(self, state, available_actions):
    #     if random.uniform(0, 1) < self.epsilon:
    #         return random.choice(available_actions).uci()

    #     state_qs = self.q_table.get(state, {})
    #     if not state_qs:
    #         return random.choice(available_actions).uci()

    #     # Pick best known action
    #     best_action = max(state_qs.items(), key=lambda x: x[1])[0]
    #     return best_action

    # def update_q(self, state, action, reward, next_state, next_actions):
    #     action = action.uci() if hasattr(action, "uci") else action
    #     next_action_values = [self.get_q(next_state, a.uci()) for a in next_actions]
    #     max_future_q = max(next_action_values) if next_action_values else 0.0

    #     current_q = self.get_q(state, action)
    #     new_q = current_q + self.alpha * (reward + self.gamma * max_future_q - current_q)

    #     if state not in self.q_table:
    #         self.q_table[state] = {}
    #     self.q_table[state][action] = new_q


    def choose_action(self, state, available_actions):
        if not available_actions:
            return None

        # Explore
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(available_actions)

        # Exploit
        state_qs = self.q_table.get(state, {})
        if not state_qs:
            return random.choice(available_actions)

        # Pick best known action
        best_action = max(state_qs.items(), key=lambda x: x[1])[0]
        return best_action

    def update_q(self, state, action, reward, next_state, next_actions):
        next_action_values = [self.get_q(next_state, a) for a in next_actions]
        max_future_q = max(next_action_values) if next_action_values else 0.0

        current_q = self.get_q(state, action)
        new_q = current_q + self.alpha * (reward + self.gamma * max_future_q - current_q)

        if state not in self.q_table:
            self.q_table[state] = {}
        self.q_table[state][action] = new_q

    def save_q_table(self, filename="data/chess_q_table.pkl"):
        with open(filename, "wb") as f:
            pickle.dump(self.q_table, f)

    def load_q_table(self, filename="data/chess_q_table.pkl"):
        if os.path.exists(filename):
            with open(filename, "rb") as f:
                self.q_table = pickle.load(f)
        else:
            print("⚠️ Chess Q-table not found. Please train the agent first.")


