def explain_move(state_before, state_after, player):
    import numpy as np

    board_before = np.array(state_before).reshape(3, 3)
    board_after = np.array(state_after).reshape(3, 3)
    
    diff = board_after - board_before
    move = np.argwhere(diff != 0)

    if move.size == 0:
        return "No move detected."

    row, col = move[0]
    symbol = "X" if player == 1 else "O"
    explanation = f"Player {symbol} placed at row {row + 1}, column {col + 1}."
    return explanation
