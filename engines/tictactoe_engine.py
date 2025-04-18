# engines/tictactoe_engine.py

""" This code is the part of tinker module where we trained the model and it was supporting but in ui it is causing some issue.
      That is why commenting it."""


import numpy as np

class TicTacToe:
    def __init__(self):
        self.reset()

    def reset(self):
        # 3x3 board initialized to zeros (0 = empty, 1 = player, -1 = opponent)
        self.board = np.zeros((3, 3), dtype=int)
        self.current_winner = None
        return self.get_state()

    def get_state(self):
        # Returns a flattened version of the board
        return self.board.flatten()

    def get_available_actions(self):
        # Returns list of (row, col) tuples where moves can be made
        return [(i, j) for i in range(3) for j in range(3) if self.board[i, j] == 0]

    def make_move(self, row, col, player):
        if self.board[row, col] == 0:
            self.board[row, col] = player
            if self.check_winner(player):
                self.current_winner = player
            return True
        return False

    def check_winner(self, player):
        # Rows and columns
        for i in range(3):
            if all(self.board[i, :] == player) or all(self.board[:, i] == player):
                return True
        # Diagonals
        if all([self.board[i, i] == player for i in range(3)]):
            return True
        if all([self.board[i, 2 - i] == player for i in range(3)]):
            return True
        return False
    
    def is_draw(self):
        return len(self.get_available_actions()) == 0 and self.current_winner is None

    def game_over(self):
        return self.current_winner is not None or self.is_draw()

    def print_board(self):
        # For debugging
        print(self.board)


# """ This code is used for streamlit, it is not used in tinker module. wrting this new code for streamlit module."""

# # engines/tictactoe_engine.py

# class TicTacToeGame:
#     def __init__(self):
#         self.board = ["-"] * 9

#     def available_moves(self, board):
#         return [i for i, x in enumerate(board) if x == "-"]

#     def check_winner(self, board):
#         wins = [(0,1,2),(3,4,5),(6,7,8),
#                 (0,3,6),(1,4,7),(2,5,8),
#                 (0,4,8),(2,4,6)]
#         for i, j, k in wins:
#             if board[i] == board[j] == board[k] and board[i] != "-":
#                 return board[i]
#         if "-" not in board:
#             return "Draw"
#         return None

#     def make_move(self, board, move, player):
#         board[move] = player
#         return board


