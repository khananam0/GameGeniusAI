# streamlit_ui/chess_web.py


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import streamlit as st
import chess
import chess.svg
import random
import base64
from engines.chess_engine import ChessGame
from ai.chess_q_learning import ChessQLearningAgent
from nlp.chess_move_explainer import explain_move

st.set_page_config(page_title="Chess Genius AI", layout="wide")
st.title("♟️ Chess Genius AI")

# Init game session
if "game" not in st.session_state:
    st.session_state.game = ChessGame()
    st.session_state.board = st.session_state.game.board
    st.session_state.selected_square = None

agent = ChessQLearningAgent()
agent.load_q_table("data/chess_q_table.npy")  # Your trained Q-table

def board_svg(board):
    return chess.svg.board(board=board, size=400)

def render_svg(svg_code):
    b64 = base64.b64encode(svg_code.encode("utf-8")).decode("utf-8")
    html = f'<img src="data:image/svg+xml;base64,{b64}"/>'
    st.write(html, unsafe_allow_html=True)

render_svg(board_svg(st.session_state.board))

# Move Input
move_input = st.text_input("Your move (e.g., e2e4):")

if st.button("Make Move"):
    try:
        move = chess.Move.from_uci(move_input)
        if move in st.session_state.board.legal_moves:
            st.session_state.board.push(move)
            st.success(f"✅ {explain_move(st.session_state.board, move.uci())}")

            if not st.session_state.board.is_game_over():
                state_fen = st.session_state.board.fen()
                ai_move = agent.choose_move(state_fen)
                if ai_move:
                    st.session_state.board.push(chess.Move.from_uci(ai_move))
                    st.info(f"🤖 AI played: {ai_move}")
        else:
            st.warning("Invalid or illegal move.")
    except:
        st.error("Invalid format. Use format like e2e4.")

if st.button("♻️ Reset Game"):
    st.session_state.board.reset()

if st.session_state.board.is_checkmate():
    st.error("💀 Checkmate!")
elif st.session_state.board.is_stalemate():
    st.warning("😐 Stalemate!")
elif st.session_state.board.is_insufficient_material():
    st.warning("Draw by insufficient material.")

