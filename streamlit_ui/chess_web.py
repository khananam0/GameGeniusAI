"""" This code is just the basic simple code."""

# # streamlit_ui/chess_web.py

# import sys, os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import streamlit as st
# import chess
# from engines.chess_engine import ChessGame
# from ai.chess_q_learning import ChessQLearningAgent
# from nlp.chess_move_explainer import explain_move

# # Unicode symbols for chess pieces
# unicode_pieces = {
#     'P': '♙', 'N': '♘', 'B': '♗', 'R': '♖', 'Q': '♕', 'K': '♔',
#     'p': '♟', 'n': '♞', 'b': '♝', 'r': '♜', 'q': '♛', 'k': '♚'
# }

# st.set_page_config(page_title="♟ Chess Genius AI", layout="wide")
# st.title("♟ GameGeniusAI: Chess")
# st.caption("Play against an AI trained using Q-Learning.")

# # Session state initialization
# if "game" not in st.session_state:
#     st.session_state.game = ChessGame()
#     st.session_state.ai = ChessQLearningAgent()
#     st.session_state.selected_square = None
#     st.session_state.replay = []
#     st.session_state.last_nlp = ""
#     st.session_state.manual_move = ""

# game = st.session_state.game
# ai = st.session_state.ai

# # Function to make a move (UCI format)

# def make_move(move_uci):
#     try:
#         move = chess.Move.from_uci(move_uci)
#         if move in game.board.legal_moves:
#             # ⏱ Call NLP before pushing the move (to capture correct context)
#             st.session_state.last_nlp = explain_move(game.board, move_uci)
#             game.board.push(move)
#             st.session_state.replay.append(game.board.fen())
#             return True
#         else:
#             st.warning("❌ Illegal move.")
#             return False
#     except:
#         st.warning("⚠️ Invalid move format.")
#         return False


# # AI response move

# def ai_move():
#     if not game.board.is_game_over():
#         move = ai.choose_action(game.board.fen(), list(game.board.legal_moves))
#         if move:
#             try:
#                 # ⏱ Call NLP before pushing the move
#                 st.session_state.last_nlp = explain_move(game.board, move.uci())
#                 game.board.push(move)
#                 st.session_state.replay.append(game.board.fen())
#                 st.rerun()
#             except Exception as e:
#                 st.error(f"Explain error: {e}")


# # Handle board square click
# def handle_click(clicked_square):
#     if st.session_state.selected_square is None:
#         piece = game.board.piece_at(chess.parse_square(clicked_square))
#         if piece and piece.color == game.board.turn:
#             st.session_state.selected_square = clicked_square
#     else:
#         move_uci = st.session_state.selected_square + clicked_square
#         if make_move(move_uci):
#             st.session_state.selected_square = None
#             ai_move()
#         else:
#             st.session_state.selected_square = None

# # Render chess board UI


# def render_board():
#     board = game.board
#     st.markdown("### 📋 Board")
#     for rank in range(8):
#         cols = st.columns(8)
#         for file in range(8):
#             square = chess.square(file, 7 - rank)
#             piece = board.piece_at(square)
#             symbol = unicode_pieces.get(piece.symbol(), "") if piece else " "
#             square_name = chess.square_name(square)

#             is_selected = square_name == st.session_state.selected_square
#             display = f"🔷 {symbol}" if is_selected else symbol or " "

#             if cols[file].button(display, key=square_name):
#                 handle_click(square_name)

# # Render board
# render_board()

# # Text input for move
# st.markdown("### ⌨️ Enter Move")
# move_input = st.text_input("Enter your move in UCI format (e.g., e2e4)", key="uci_input")
# if st.button("✅ Submit Move"):
#     if make_move(move_input):
#         ai_move()

# # Show game status
# if game.board.is_checkmate():
#     winner = "You" if game.board.turn == chess.BLACK else "AI"
#     st.success(f"🏁 Checkmate! {winner} wins!")
# elif game.board.is_stalemate():
#     st.info("🤝 Stalemate!")
# elif game.board.is_insufficient_material():
#     st.info("🤝 Draw by insufficient material.")
# elif game.board.is_check():
#     st.warning("⚠️ Check!")

# # NLP explanation display
# if st.session_state.last_nlp:
#     st.markdown("### 🧠 Move Explanation")
#     st.info(st.session_state.last_nlp)

# # Game control buttons
# col1, col2 = st.columns(2)
# if col1.button("♻ Restart Game"):
#     st.session_state.game = ChessGame()
#     st.session_state.selected_square = None
#     st.session_state.replay = []
#     st.session_state.last_nlp = ""
#     st.rerun()

# if col2.button("📽 View Replay"):
#     st.markdown("### 🕹 Replay States (FEN Notation)")
#     for idx, fen in enumerate(st.session_state.replay):
#         st.code(f"Move {idx + 1}: {fen}", language="text")




# ========================================================================================================================
# -----------------------------Perfect and final---------------------------------------------------------
"""" This code is for the streamlit ui which is integrated simply. sepertoely file. You can run sepeertely this uing the file sepeartely. 
Using this file you can run the chess game using streamlit. Command-  streamlit run .\streamlit_ui\chess_web.py
"""


# streamlit_ui/chess_web.py
# Function to convert a board state to an image

# def board_to_svg(board, size=500):
#     import chess.svg
#     return chess.svg.board(board=board, size=size)


# import sys, os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import streamlit as st
# import chess
# from engines.chess_engine import ChessGame
# from ai.chess_q_learning import ChessQLearningAgent
# from nlp.chess_move_explainer import explain_move


# # Unicode symbols for chess pieces
# unicode_pieces = {
#     'P': '♙', 'N': '♘', 'B': '♗', 'R': '♖', 'Q': '♕', 'K': '♔',
#     'p': '♟', 'n': '♞', 'b': '♝', 'r': '♜', 'q': '♛', 'k': '♚'
# }

# st.set_page_config(page_title="♟ Chess Genius AI", layout="wide")
# st.title("♟ GameGeniusAI: Chess")
# st.caption("Play against an AI trained using Q-Learning.")

# # Session state initialization
# if "game" not in st.session_state:
#     st.session_state.game = ChessGame()
#     st.session_state.ai = ChessQLearningAgent()
#     st.session_state.selected_square = None
#     st.session_state.replay = []
#     st.session_state.last_nlp = ""
#     st.session_state.manual_move = ""

# game = st.session_state.game
# ai = st.session_state.ai

# # Function to make a move (UCI format)
# def make_move(move_uci):
#     try:
#         move = chess.Move.from_uci(move_uci)
#         if move in game.board.legal_moves:
#             # ⏱ Call NLP before pushing the move (to capture correct context)
#             st.session_state.last_nlp = explain_move(game.board, move_uci)
#             game.board.push(move)
#             st.session_state.replay.append(game.board.fen())  # Save FEN notation
#             return True
#         else:
#             st.warning("❌ Illegal move.")
#             return False
#     except:
#         st.warning("⚠️ Invalid move format.")
#         return False

# # AI response move
# def ai_move():
#     if not game.board.is_game_over():
#         move = ai.choose_action(game.board.fen(), list(game.board.legal_moves))
#         if move:
#             try:
#                 # ⏱ Call NLP before pushing the move
#                 st.session_state.last_nlp = explain_move(game.board, move.uci())
#                 game.board.push(move)
#                 st.session_state.replay.append(game.board.fen())  # Save FEN notation
#                 st.rerun()
#             except Exception as e:
#                 st.error(f"Explain error: {e}")

# # Handle board square click
# def handle_click(clicked_square):
#     if st.session_state.selected_square is None:
#         piece = game.board.piece_at(chess.parse_square(clicked_square))
#         if piece and piece.color == game.board.turn:
#             st.session_state.selected_square = clicked_square
#     else:
#         move_uci = st.session_state.selected_square + clicked_square
#         if make_move(move_uci):
#             st.session_state.selected_square = None
#             ai_move()
#         else:
#             st.session_state.selected_square = None

# # Render chess board UI
# def render_board():
#     board = game.board
#     st.markdown("### 📋 Board")
#     for rank in range(8):
#         cols = st.columns(8)
#         for file in range(8):
#             square = chess.square(file, 7 - rank)
#             piece = board.piece_at(square)
#             symbol = unicode_pieces.get(piece.symbol(), "") if piece else " "
#             square_name = chess.square_name(square)

#             is_selected = square_name == st.session_state.selected_square
#             display = f"🔷 {symbol}" if is_selected else symbol or " "

#             if cols[file].button(display, key=square_name):
#                 handle_click(square_name)

# # Render board
# render_board()

# # Text input for move
# st.markdown("### ⌨️ Enter Move")
# move_input = st.text_input("Enter your move in UCI format (e.g., e2e4)", key="uci_input")
# if st.button("✅ Submit Move"):
#     if make_move(move_input):
#         ai_move()

# # Show game status
# if game.board.is_checkmate():
#     winner = "You" if game.board.turn == chess.BLACK else "AI"
#     st.success(f"🏁 Checkmate! {winner} wins!")
# elif game.board.is_stalemate():
#     st.info("🤝 Stalemate!")
# elif game.board.is_insufficient_material():
#     st.info("🤝 Draw by insufficient material.")
# elif game.board.is_check():
#     st.warning("⚠️ Check!")

# # NLP explanation display
# if st.session_state.last_nlp:
#     st.markdown("### 🧠 Move Explanation")
#     st.info(st.session_state.last_nlp)

# # Game control buttons
# col1, col2 = st.columns(2)
# if col1.button("♻ Restart Game"):
#     st.session_state.game = ChessGame()
#     st.session_state.selected_square = None
#     st.session_state.replay = []
#     st.session_state.last_nlp = ""
#     st.rerun()


# # Make sure to initialize it
# if "show_replay" not in st.session_state:
#     st.session_state.show_replay = False

# if col2.button("📽 View Replay"):
#     st.session_state.show_replay = True

# # Always render the radio option (it needs time to update from frontend interaction)
# display_option = st.radio("Select Replay Display Option", ("FEN Notation", "Visual Board"), key="replay_display")

# # Now actually show the replay only if toggled
# if st.session_state.show_replay:
#     st.markdown("### 🕹 Replay States")

#     for idx, fen in enumerate(st.session_state.replay):
#         if display_option == "Visual Board":
#             board = chess.Board(fen)
#             svg = board_to_svg(board, size=450)
#             st.markdown(f"#### Move {idx + 1}")
#             st.markdown(f'<div style="text-align:center">{svg}</div>', unsafe_allow_html=True)
#         elif display_option == "FEN Notation":
#             st.markdown(f"#### Move {idx + 1}")
#             st.code(f"FEN: {fen}", language="text")





# +++++++++++++++++++++++++++++++++++++Main ui code++++++++++++++++++++++++++++++++++++++++++++++++++++++++

""" This code is for the streamlit ui which is integrated with main.py file, In this file we have two project running simultaneously. """


def run():
    import sys, os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

    import streamlit as st
    import chess
    from engines.chess_engine import ChessGame
    from ai.chess_q_learning import ChessQLearningAgent
    from nlp.chess_move_explainer import explain_move
    import chess.svg

    def board_to_svg(board, size=500):
        return chess.svg.board(board=board, size=size)

    unicode_pieces = {
        'P': '♙', 'N': '♘', 'B': '♗', 'R': '♖', 'Q': '♕', 'K': '♔',
        'p': '♟', 'n': '♞', 'b': '♝', 'r': '♜', 'q': '♛', 'k': '♚'
    }

    st.header("♟ GameGeniusAI: Chess")
    st.caption("Play chess against a Q-Learning AI with NLP-based move explanations.")

    # ✅ Safe session initialization
    st.session_state.setdefault("chess_game", ChessGame())
    st.session_state.setdefault("chess_ai", ChessQLearningAgent())
    st.session_state.setdefault("chess_selected_square", None)
    st.session_state.setdefault("chess_replay", [])
    st.session_state.setdefault("chess_last_nlp", "")
    st.session_state.setdefault("chess_manual_move", "")
    st.session_state.setdefault("chess_show_replay", False)

    game = st.session_state.chess_game
    ai = st.session_state.chess_ai

    def make_move(move_uci):
        try:
            move = chess.Move.from_uci(move_uci)
            if move in game.board.legal_moves:
                st.session_state.chess_last_nlp = explain_move(game.board, move_uci)
                game.board.push(move)
                st.session_state.chess_replay.append(game.board.fen())
                return True
            else:
                st.warning("❌ Illegal move.")
                return False
        except:
            st.warning("⚠️ Invalid move format.")
            return False

    def ai_move():
        if not game.board.is_game_over():
            move = ai.choose_action(game.board.fen(), list(game.board.legal_moves))
            if move:
                try:
                    st.session_state.chess_last_nlp = explain_move(game.board, move.uci())
                    game.board.push(move)
                    st.session_state.chess_replay.append(game.board.fen())
                    st.rerun()
                except Exception as e:
                    st.error(f"NLP error: {e}")

    def handle_click(clicked_square):
        if st.session_state.chess_selected_square is None:
            piece = game.board.piece_at(chess.parse_square(clicked_square))
            if piece and piece.color == game.board.turn:
                st.session_state.chess_selected_square = clicked_square
        else:
            move_uci = st.session_state.chess_selected_square + clicked_square
            if make_move(move_uci):
                st.session_state.chess_selected_square = None
                ai_move()
            else:
                st.session_state.chess_selected_square = None

    def render_board():
        board = game.board
        st.markdown("### 📋 Board")
        for rank in range(8):
            cols = st.columns(8)
            for file in range(8):
                square = chess.square(file, 7 - rank)
                piece = board.piece_at(square)
                symbol = unicode_pieces.get(piece.symbol(), "") if piece else " "
                square_name = chess.square_name(square)

                is_selected = square_name == st.session_state.chess_selected_square
                display = f"🔷 {symbol}" if is_selected else symbol or " "

                if cols[file].button(display, key=f"chess_{square_name}"):
                    handle_click(square_name)

    render_board()

    st.markdown("### ⌨️ Enter Move")
    move_input = st.text_input("Enter your move in UCI format (e.g., e2e4)", key="chess_uci_input", value="")
    if st.button("✅ Submit Move"):
        if make_move(move_input):
            ai_move()

    # Game status
    if game.board.is_checkmate():
        winner = "You" if game.board.turn == chess.BLACK else "AI"
        st.success(f"🏁 Checkmate! {winner} wins!")
    elif game.board.is_stalemate():
        st.info("🤝 Stalemate!")
    elif game.board.is_insufficient_material():
        st.info("🤝 Draw by insufficient material.")
    elif game.board.is_check():
        st.warning("⚠️ Check!")

    # NLP explanation
    if st.session_state.chess_last_nlp:
        st.markdown("### 🧠 Move Explanation")
        st.info(st.session_state.chess_last_nlp)

    # Controls
    col1, col2 = st.columns(2)
    
    if col1.button("♻ Restart Game"):
        # Reset the game and related session state variables
        st.session_state.chess_game = ChessGame()
        st.session_state.chess_ai = ChessQLearningAgent()
        st.session_state.chess_selected_square = None
        st.session_state.chess_replay = []
        st.session_state.chess_last_nlp = ""
        st.session_state.chess_manual_move = ""
        st.session_state.chess_show_replay = False
        st.rerun()  # Using experimental_rerun to trigger a fresh app restart


    if col2.button("📽 View Replay"):
        st.session_state.chess_show_replay = not st.session_state.chess_show_replay

    if st.session_state.chess_show_replay:
        st.markdown("### 🕹 Replay Viewer")
        display_option = st.radio("Display As", ("FEN Notation", "Visual Board"), key="chess_replay_display")
        for idx, fen in enumerate(st.session_state.chess_replay):
            st.markdown(f"#### Move {idx + 1}")
            if display_option == "Visual Board":
                board = chess.Board(fen)
                svg = board_to_svg(board)
                st.markdown(f'<div style="text-align:center">{svg}</div>', unsafe_allow_html=True)
            else:
                st.code(f"FEN: {fen}", language="text")



