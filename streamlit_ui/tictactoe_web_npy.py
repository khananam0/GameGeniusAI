# streamlit_ui/tictactoe_web.py

import streamlit as st
import numpy as np
from engines.tictactoe_engine import TicTacToeGame
from ai.q_learning import QLearningAgent
import random

st.set_page_config(page_title="Tic-Tac-Toe Genius", layout="centered")

st.title("🎮 Tic-Tac-Toe Genius AI")
st.markdown("Play against the AI with adjustable difficulty.")

difficulty = st.radio("Select AI difficulty:", ["Easy (Random)", "Hard (Q-Learning)"])
game = TicTacToeGame()

# Load Q-learning agent
agent = QLearningAgent()
agent.load("data/tictactoe_q_table.npy")  # Replace with your actual Q-table file

# State session
if "state" not in st.session_state:
    st.session_state.state = game.board.copy()
    st.session_state.moves = []

def render_board():
    cols = st.columns(3)
    for i in range(3):
        for j in range(3):
            idx = 3 * i + j
            label = st.session_state.state[idx]
            if cols[j].button(label if label != "-" else " ", key=f"{idx}"):
                if st.session_state.state[idx] == "-":
                    st.session_state.state[idx] = "X"
                    st.session_state.moves.append(st.session_state.state.copy())

                    if game.check_winner(st.session_state.state) is None:
                        ai_move()

def ai_move():
    board = st.session_state.state.copy()
    if difficulty == "Easy (Random)":
        move = random.choice([i for i, x in enumerate(board) if x == "-"])
    else:
        state_str = "".join(board)
        move = agent.choose_action(state_str, board)

    if board[move] == "-":
        board[move] = "O"
        st.session_state.moves.append(board.copy())
    st.session_state.state = board

def restart():
    st.session_state.state = game.board.copy()
    st.session_state.moves = []

def replay():
    st.markdown("### 🕰️ Game Replay")
    for idx, move in enumerate(st.session_state.moves):
        st.text(f"Move {idx+1}: {''.join(move)}")

render_board()

winner = game.check_winner(st.session_state.state)
if winner:
    st.success(f"{winner} wins!" if winner != "Draw" else "It's a Draw!")
    if st.button("Restart Game"):
        restart()
else:
    if st.button("Restart"):
        restart()

if st.button("📽 View Replay"):
    replay()
