# gui/tictactoe_gui.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from engines.tictactoe_engine import TicTacToe
from ai.q_learning import QLearningAgent

class TicTacToeGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("GameGeniusAI: Tic-Tac-Toe")
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.game = TicTacToe()
        self.agent = QLearningAgent()
        self.agent.load_q_table("data/q_table.pkl")
        self.state = self.game.reset()
        self.current_player = -1  # Human

        self.create_buttons()
        self.window.mainloop()

    def create_buttons(self):
        for row in range(3):
            for col in range(3):
                btn = tk.Button(self.window, text="", font=("Arial", 32), width=4, height=2,
                                command=lambda r=row, c=col: self.click(r, c))
                btn.grid(row=row, column=col)
                self.buttons[row][col] = btn

    def click(self, row, col):
        if self.game.board[row][col] == 0 and self.current_player == -1 and not self.game.game_over():
            self.game.make_move(row, col, -1)
            self.update_buttons()
            self.current_player = 1
            self.window.after(500, self.ai_move)

    def ai_move(self):
        if not self.game.game_over():
            available = self.game.get_available_actions()
            action = self.agent.choose_action(self.state, available)
            self.game.make_move(action[0], action[1], 1)
            self.update_buttons()
            self.current_player = -1

        if self.game.game_over():
            self.end_game()

    def update_buttons(self):
        symbols = {0: "", 1: "O", -1: "X"}
        for row in range(3):
            for col in range(3):
                val = self.game.board[row][col]
                self.buttons[row][col].config(text=symbols[val])
        self.state = self.game.get_state()

    def end_game(self):
        winner = self.game.current_winner
        msg = "Draw!"
        if winner == -1:
            msg = "🎉 You Win!"
        elif winner == 1:
            msg = "🤖 AI Wins!"
        result = tk.Label(self.window, text=msg, font=("Arial", 24))
        result.grid(row=3, column=0, columnspan=3)

if __name__ == "__main__":
    TicTacToeGUI()
