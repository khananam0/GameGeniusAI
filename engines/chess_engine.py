
# engines/chess_engine.py
import chess
import random

class ChessGame:
    def __init__(self):
        self.board = chess.Board()

    def reset(self):
        self.board.reset()
        return self.get_state()

    def get_state(self):
        return self.board.fen()  # FEN notation as state

    # def get_available_actions(self):
    #     return list(self.board.legal_moves)
    
    def get_available_actions(self):
        return [move.uci() for move in self.board.legal_moves]

    def make_move(self, move_uci):
        try:
            move = chess.Move.from_uci(move_uci)
            if move in self.board.legal_moves:
                self.board.push(move)
                return True
            else:
                pass
        except:
            return False
        
        
    def get_board(self):
        """
        Return the current board state as a 2D list of piece symbols.
        Uppercase for White, lowercase for Black.
        Empty squares are '.'.
        """
        board_matrix = []
        for rank in range(8):
            row = []
            for file in range(8):
                square = chess.square(file, 7 - rank)  # Convert to rank/file index
                piece = self.board.piece_at(square)
                row.append(piece.symbol() if piece else '.')
            board_matrix.append(row)
        return board_matrix

        
    def get_piece_at(self, position):
        """Return the piece symbol at a given (row, col) position on the board."""
        row, col = position
        # Assuming you're using python-chess and your board is a chess.Board() object:
        square = chess.square(col, 7 - row)  # Convert (row, col) to chess.SQUARE
        piece = self.board.piece_at(square)
        return piece.symbol() if piece else " "


    def game_over(self):
        return self.board.is_game_over()

    # def get_result(self):
    #     if self.board.is_checkmate():
    #         return "checkmate"
    #     elif self.board.is_stalemate():
    #         return "stalemate"
    #     elif self.board.is_insufficient_material():
    #         return "draw"
    #     elif self.board.can_claim_draw():
    #         return "draw"
    #     else:
    #         return None

    def get_result(self):
        if self.board.is_checkmate():
            return "Checkmate"
        elif self.board.is_stalemate():
            return "Stalemate"
        elif self.board.is_insufficient_material():
            return "Draw - insufficient material"
        elif self.board.is_seventyfive_moves():
            return "Draw - 75 moves"
        elif self.board.is_fivefold_repetition():
            return "Draw - repetition"
        else:
            return "Game over"

    def render(self):
        print(self.board)


