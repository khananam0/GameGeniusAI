# ai/q_learning.py



""" This code is the part of tinker module where we trained the model and it was supporting but in ui it is causing some issue.
      That is why commenting it."""


import random
import numpy as np
import pickle

class QLearningAgent:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=1.0, epsilon_decay=0.995, epsilon_min=0.01):
        self.q_table = {}  # key: (state, action), value: Q-value
        self.alpha = alpha  # learning rate
        self.gamma = gamma  # discount factor
        self.epsilon = epsilon  # exploration rate
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min

    def get_q_value(self, state, action):
        return self.q_table.get((tuple(state), action), 0.0)

    def choose_action(self, state, available_actions):
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(available_actions)
        q_values = [self.get_q_value(state, a) for a in available_actions]
        max_q = max(q_values)
        best_actions = [a for a, q in zip(available_actions, q_values) if q == max_q]
        return random.choice(best_actions)

    def learn(self, state, action, reward, next_state, next_available_actions, done):
        current_q = self.get_q_value(state, action)
        future_q = 0

        if not done and next_available_actions:
            future_q = max([self.get_q_value(next_state, a) for a in next_available_actions])

        updated_q = (1 - self.alpha) * current_q + self.alpha * (reward + self.gamma * future_q)
        self.q_table[(tuple(state), action)] = updated_q

        if done:
            self.epsilon = max(self.epsilon * self.epsilon_decay, self.epsilon_min)

    def save_q_table(self, path='data/q_table.pkl'):
        with open(path, 'wb') as f:
            pickle.dump(self.q_table, f)

    def load_q_table(self, path='data/q_table.pkl'):
        with open(path, 'rb') as f:
            self.q_table = pickle.load(f)




""" This code is used for streamlit, it is not used in tinker module. wrting this new code for streamlit module."""


# # ai/q_learning.py

# import numpy as np
# import random

# class QLearningAgent:
#     def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.2):
#         self.q_table = {}
#         self.alpha = alpha
#         self.gamma = gamma
#         self.epsilon = epsilon

#     def choose_action(self, state, board):
#         if random.random() < self.epsilon:
#             return random.choice([i for i, x in enumerate(board) if x == "-"])
#         self.q_table.setdefault(state, [0]*9)
#         q_values = self.q_table[state]
#         available = [i for i, x in enumerate(board) if x == "-"]
#         best_move = max(available, key=lambda x: q_values[x])
#         return best_move

#     def learn(self, state, action, next_state, reward):
#         self.q_table.setdefault(state, [0]*9)
#         self.q_table.setdefault(next_state, [0]*9)
#         predict = self.q_table[state][action]
#         target = reward + self.gamma * max(self.q_table[next_state])
#         self.q_table[state][action] += self.alpha * (target - predict)

#     def save(self, path):
#         np.save(path, self.q_table)

#     def load(self, path):
#         self.q_table = np.load(path, allow_pickle=True).item()


