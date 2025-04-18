# # play/chess_ui.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import tkinter as tk
# from tkinter import messagebox
# from engines.chess_engine import ChessGame
# from ai.chess_q_learning import ChessQLearningAgent

# class ChessGUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("GameGenius Chess")

#         self.game = ChessGame()
#         self.agent = ChessQLearningAgent()
#         self.agent.load_q_table()

#         self.board_frame = tk.Frame(self.root)
#         self.board_frame.pack()

#         self.buttons = {}
#         self.create_board()
#         self.display_board()

#     def create_board(self):
#         """Create the chessboard UI (8x8 grid of buttons)."""
#         for row in range(8):
#             for col in range(8):
#                 button = tk.Button(self.board_frame, text='', width=8, height=3, 
#                                    command=lambda r=row, c=col: self.on_square_click(r, c))
#                 button.grid(row=row, column=col)
#                 self.buttons[(row, col)] = button

#     def display_board(self):
#         """Display the chessboard based on the current game state."""
#         for row in range(8):
#             for col in range(8):
#                 piece = self.game.get_piece_at((row, col))
#                 self.buttons[(row, col)].config(text=piece)

#     def on_square_click(self, row, col):
#         """Handle square click to make a move."""
#         move = self.get_move_from_square(row, col)
#         if self.game.make_move(move):
#             self.display_board()
#             if not self.game.game_over():
#                 self.ai_move()

#     def get_move_from_square(self, row, col):
#         """Generate UCI-style move from row, col."""
#         # Assume the user will make valid moves (for simplicity)
#         # Convert click to UCI (e.g., e2e4)
#         piece = self.game.get_piece_at((row, col))
#         return f"{piece[0]}{row}{col}"  # Just an example for the click

#     def ai_move(self):
#         """Make AI move and update the board."""
#         state = self.game.get_state()
#         actions = self.game.get_available_actions()
#         ai_move = self.agent.choose_action(state, actions)
#         self.game.make_move(ai_move)
#         self.display_board()

#         if self.game.game_over():
#             self.show_game_over()

#     def show_game_over(self):
#         """Show game-over message."""
#         result = self.game.get_result()
#         messagebox.showinfo("Game Over", f"Result: {result}")

# if __name__ == "__main__":
#     root = tk.Tk()
#     gui = ChessGUI(root)
#     root.mainloop()



# ============================with emoji=======================================

import tkinter as tk
from engines.chess_engine import ChessGame
from ai.chess_q_learning import ChessQLearningAgent
from nlp.move_explainer import explain_move

SQUARE_SIZE = 60
BOARD_COLOR_LIGHT = "#F0D9B5"
BOARD_COLOR_DARK = "#B58863"

piece_symbols = {
    'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚', 'p': '♟',
    'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔', 'P': '♙',
    '.': ' '
}

class ChessGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("GameGeniusAI - Chess")
        self.canvas = tk.Canvas(root, width=8*SQUARE_SIZE, height=8*SQUARE_SIZE)
        self.canvas.pack()

        """
        for clicabale ui start:
        """
        self.status_label = tk.Label(root, text="🕹️ Click a piece to move.", font=("Arial", 14))
        self.status_label.pack(pady=10)
        """
        for clicabale ui end:
        """
        self.canvas.bind("<Button-1>", self.on_click)

        self.game = ChessGame()
        self.agent = ChessQLearningAgent()
        self.agent.load_q_table()

        self.selected_square = None
        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
        board = self.game.get_board()

        for row in range(8):
            for col in range(8):
                color = BOARD_COLOR_LIGHT if (row + col) % 2 == 0 else BOARD_COLOR_DARK
                x1, y1 = col * SQUARE_SIZE, row * SQUARE_SIZE
                x2, y2 = x1 + SQUARE_SIZE, y1 + SQUARE_SIZE
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

                piece = board[row][col]
                if piece != '.':
                    self.canvas.create_text(
                        x1 + SQUARE_SIZE // 2,
                        y1 + SQUARE_SIZE // 2,
                        text=piece_symbols.get(piece, '?'),
                        font=("Arial", 28)
                    )

    def get_square_from_click(self, event):
        col = event.x // SQUARE_SIZE
        row = event.y // SQUARE_SIZE
        return row, col

    def on_click(self, event):
        row, col = self.get_square_from_click(event)
        square = f"{chr(col + ord('a'))}{7 - row + 1}"

        if self.selected_square is None:
            self.selected_square = square
            """Start for clicking"""
            self.selected_coords = (row, col)
            print(f"🟨 Selected: {square}")
            self.status_label.config(text=f"🟨 Selected: {square}")
            """End for clicking"""
        else:
            move = self.selected_square + square
            print(f"🎯 Attempting Move: {self.selected_square} to {square}")

            # if self.game.make_move(move):
            #     """Start for clicking"""
            #     print(f"✅ Moved: {self.selected_square} to {square}")
            #     self.status_label.config(text=f"✅ Moved: {self.selected_square} → {square}")
            #     self.selected_square = None
            #     self.selected_coords = None
            #     """End for clicking"""
                
            #     self.draw_board()
            #     self.root.after(500, self.make_ai_move)  # delay AI move
            
            if self.game.make_move(move):
                print(f"✅ Moved: {self.selected_square} to {square}")
                explanation = explain_move(self.game.board, move)
                print(f"🧠 Move explained: {explanation}")
                self.status_label.config(text=f"✅ {explanation}")
                
                self.selected_square = None
                self.selected_coords = None
                self.draw_board()
                self.root.after(500, self.make_ai_move)

            else:
                print("❌ Invalid move")
                """Start for clicking"""
                self.status_label.config(text="❌ Invalid move! Try again.")
                self.selected_square = None
                self.selected_coords = None
                """End for clicking"""
            self.selected_square = None

    def make_ai_move(self):
        if self.game.game_over():
            print("🏁 Game Over:", self.game.get_result())
            return

        state = self.game.get_state()
        actions = self.game.get_available_actions()
        ai_move = self.agent.choose_action(state, actions)

        # print(f"🤖 AI move: {ai_move}")
        # self.game.make_move(ai_move)
        # self.draw_board()

        
        if self.game.make_move(ai_move):
            explanation = explain_move(self.game.board, ai_move)
            print(f"🤖 AI move: {ai_move}")
            print(f"🧠 AI explained: {explanation}")
            self.status_label.config(text=f"🤖 {explanation}")

        self.draw_board()


        

if __name__ == "__main__":
    root = tk.Tk()
    gui = ChessGUI(root)
    root.mainloop()
