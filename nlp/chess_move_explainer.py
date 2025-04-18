# nlp/move_explainer.py
import chess

piece_names = {
    chess.PAWN: "Pawn",
    chess.KNIGHT: "Knight",
    chess.BISHOP: "Bishop",
    chess.ROOK: "Rook",
    chess.QUEEN: "Queen",
    chess.KING: "King"
}

def explain_move(board, move_uci):
    move = chess.Move.from_uci(move_uci)
    piece = board.piece_at(move.from_square)

    if not piece:
        return "Invalid move or unknown piece."

    name = piece_names.get(piece.piece_type, "Piece")
    from_sq = chess.square_name(move.from_square)
    to_sq = chess.square_name(move.to_square)

    # Descriptive rules
    description = f"{name} moves from {from_sq} to {to_sq}."

    # Extra insights
    if name == "Pawn" and to_sq in ["d4", "e4", "d5", "e5"]:
        description += " Controlling the center!"
    elif name == "Knight":
        description += " Knights are great at jumping over pieces!"
    elif name == "Bishop" and abs(move.from_square - move.to_square) % 9 == 0:
        description += " Targeting a long diagonal."

    if board.is_capture(move):
        description += " It’s a capture!"

    return description
