# # streamlit_ui/tictactoe_web.py

# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# streamlit_ui/tictactoe_web.py

# import streamlit as st
# import numpy as np
# import random
# import os
# import pickle
# from engines.tictactoe_engine import TicTacToe
# from ai.q_learning import QLearningAgent

# st.set_page_config(page_title="Tic-Tac-Toe Genius", layout="centered")
# st.title("🎮 Tic-Tac-Toe Genius AI")
# st.markdown("Play against the AI trained via Q-Learning.")

# # Load Q-table
# Q_TABLE_PATH = "data/q_table.pkl"
# agent = QLearningAgent()
# if os.path.exists(Q_TABLE_PATH):
#     agent.load_q_table(Q_TABLE_PATH)

# # Game state in session
# if "game" not in st.session_state:
#     st.session_state.game = TicTacToe()
#     st.session_state.board = st.session_state.game.board.copy()
#     st.session_state.state = st.session_state.game.get_state()
#     st.session_state.msg = ""
#     st.session_state.replay = []

# game = st.session_state.game

# def reset_game():
#     st.session_state.game = TicTacToe()
#     st.session_state.board = st.session_state.game.board.copy()
#     st.session_state.state = st.session_state.game.get_state()
#     st.session_state.msg = ""
#     st.session_state.replay = []

# def render_board():
#     board = st.session_state.board
#     cols = st.columns(3)
#     for i in range(3):
#         for j in range(3):
#             idx = 3 * i + j
#             cell = board[i][j]
#             symbol = "X" if cell == 1 else "O" if cell == -1 else ""
#             if cols[j].button(symbol or " ", key=f"{i}-{j}"):
#                 if cell == 0 and not game.game_over():
#                     player_move(i, j)

# def player_move(row, col):
#     moved = game.make_move(row, col, player=1)
#     if moved:
#         st.session_state.replay.append(game.get_state().copy())
#         st.session_state.board = game.board.copy()
#         if not game.game_over():
#             ai_turn()

# def ai_turn():
#     state = game.get_state()
#     available = game.get_available_actions()
#     action = agent.choose_action(state, available)
#     moved = game.make_move(action[0], action[1], player=-1)
#     if moved:
#         st.session_state.replay.append(game.get_state().copy())
#     st.session_state.board = game.board.copy()

# # Game status
# render_board()

# if game.current_winner == 1:
#     st.success("🎉 You Win!")
# elif game.current_winner == -1:
#     st.error("💀 AI Wins!")
# elif game.is_draw():
#     st.info("🤝 It's a Draw!")

# col1, col2 = st.columns(2)
# if col1.button("🔄 Restart"):
#     reset_game()

# if col2.button("📽 View Replay"):
#     st.markdown("### Replay Steps")
#     for idx, state in enumerate(st.session_state.replay):
#         formatted = state.reshape((3, 3))
#         st.write(f"Move {idx+1}")
#         st.table(formatted)


# ============================PEfect and final last ========================================================================

# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import streamlit as st
# import numpy as np
# import random
# import pickle
# from engines.tictactoe_engine import TicTacToe
# from ai.q_learning import QLearningAgent
# from nlp.tictactoe_move_explainer import explain_move


# st.set_page_config(page_title="Tic-Tac-Toe Genius", layout="centered")
# st.title("🎮 Tic-Tac-Toe Genius AI")
# st.markdown("Play against the AI trained via Q-Learning.")

# # Load Q-table
# Q_TABLE_PATH = "data/q_table.pkl"
# agent = QLearningAgent()
# if os.path.exists(Q_TABLE_PATH):
#     agent.load_q_table(Q_TABLE_PATH)



# # --- AI Difficulty Selection ---
# st.sidebar.title("🧠 AI Settings")
# difficulty = st.sidebar.radio("Choose Difficulty", ["Easy (Random)", "Hard (Trained)"])

# use_trained_ai = difficulty == "Hard (Trained)"



# # Initialize game state
# if "game" not in st.session_state:
#     st.session_state.game = TicTacToe()
#     st.session_state.board = st.session_state.game.board.copy()
#     st.session_state.state = st.session_state.game.get_state()
#     st.session_state.msg = ""
#     st.session_state.replay = []

# game = st.session_state.game

# def reset_game():
#     st.session_state.game = TicTacToe()
#     st.session_state.board = st.session_state.game.board.copy()
#     st.session_state.state = st.session_state.game.get_state()
#     st.session_state.msg = ""
#     st.session_state.replay = []
#     st.rerun()  # Refresh UI instantly

# def player_move(row, col):
#     moved = game.make_move(row, col, player=1)
#     if moved:
#         st.session_state.replay.append(game.get_state().copy())
#         if not game.game_over():
#             ai_turn()
#         st.session_state.board = game.board.copy()
#         st.rerun()

# # def ai_turn():
# #     state = game.get_state()
# #     available = game.get_available_actions()  # FIXED
# #     action = agent.choose_action(state, available)
# #     moved = game.make_move(action[0], action[1], player=-1)
# #     if moved:
# #         st.session_state.replay.append(game.get_state().copy())
# #     st.session_state.board = game.board.copy().

# def ai_turn():
#     state_before = game.get_state().copy()
#     available = game.get_available_actions()
#     if use_trained_ai:
#         action = agent.choose_action(state_before, available)   # ← Trained agent
#     else:
#         action = random.choice(available)                       # ← Random (Easy)
#     moved = game.make_move(action[0], action[1], player=-1)     
#     if moved:
#         state_after = game.get_state().copy()
#         st.session_state.replay.append(state_after)
#         explanation = explain_move(state_before.reshape((3,3)), state_after.reshape((3,3)), -1)
#         st.session_state.msg = explanation
#     st.session_state.board = game.board.copy()



# def render_board():
#     board = st.session_state.board
#     cols = st.columns(3)
#     for i in range(3):
#         for j in range(3):
#             cell = board[i][j]
#             symbol = "❌" if cell == 1 else "⭕" if cell == -1 else ""
#             if cols[j].button(symbol or " ", key=f"{i}-{j}"):
#                 if cell == 0 and not game.game_over():
#                     player_move(i, j)

# render_board()
# if st.session_state.msg:
#     st.markdown(f"🧠 **AI says:** {st.session_state.msg}")

# # Display game result
# if game.current_winner == 1:
#     st.success("🎉 You Win!")
# elif game.current_winner == -1:
#     st.error("💀 AI Wins!")
# elif game.is_draw():
#     st.info("🤝 It's a Draw!")

# # Control buttons
# col1, col2, col3 = st.columns([1, 1, 1])
# if col1.button("🔄 Restart Game"):
#     reset_game()

# if col2.button("📽 View Replay"):
#     if st.session_state.replay:
#         st.markdown("### 🧠 Replay Steps (Visual Board)")
#         for idx, state in enumerate(st.session_state.replay):
#             st.write(f"**Move {idx+1}**")
#             formatted = state.reshape((3, 3))
#             board_html = "<table style='border-collapse: collapse;'>"
#             for row in formatted:
#                 board_html += "<tr>"
#                 for cell in row:
#                     symbol = "❌" if cell == 1 else "⭕" if cell == -1 else "&nbsp;"
#                     board_html += f"<td style='width: 40px; height: 40px; border: 1px solid black; text-align: center; font-size: 24px;'>{symbol}</td>"
#                 board_html += "</tr>"
#             board_html += "</table>"
#             st.markdown(board_html, unsafe_allow_html=True)


# st.sidebar.title("📂 Load Replay")
# replay_file = st.sidebar.file_uploader("Upload Replay File (.json)", type=["json"])
# if replay_file:
#     import json
#     replay_data = json.load(replay_file)
#     st.session_state.replay = [np.array(state) for state in replay_data]
#     st.sidebar.success("Replay loaded! Click 'View Replay' to see it.")


# if col3.button("🗑 Clear Replay"):
#     st.session_state.replay = []
#     st.rerun()

# import json

# if st.sidebar.button("💾 Save Replay"):
#     if st.session_state.replay:
#         file_path = "saved_replay.json"
#         with open(file_path, "w") as f:
#             json.dump([state.tolist() for state in st.session_state.replay], f)
#         st.sidebar.success(f"Replay saved as `{file_path}`.")
#     else:
#         st.sidebar.warning("No replay data to save.")







# ==================================main ui code=================================


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import numpy as np
import random
import pickle
import json

from engines.tictactoe_engine import TicTacToe
from ai.q_learning import QLearningAgent
from nlp.tictactoe_move_explainer import explain_move

def run():
    st.subheader("🎮 Tic-Tac-Toe Genius AI")
    st.markdown("Play against the AI trained via Q-Learning.")

    Q_TABLE_PATH = "data/q_table.pkl"
    agent = QLearningAgent()
    if os.path.exists(Q_TABLE_PATH):
        agent.load_q_table(Q_TABLE_PATH)

    st.sidebar.title("🧠 AI Settings")
    difficulty = st.sidebar.radio("Choose Difficulty", ["Easy (Random)", "Hard (Trained)"], key="ttt_difficulty")
    use_trained_ai = difficulty == "Hard (Trained)"

    # Namespaced session keys
    if "ttt_game" not in st.session_state:
        st.session_state.ttt_game = TicTacToe()
        st.session_state.ttt_board = st.session_state.ttt_game.board.copy()
        st.session_state.ttt_state = st.session_state.ttt_game.get_state()
        st.session_state.ttt_msg = ""
        st.session_state.ttt_replay = []

    game = st.session_state.ttt_game

    def reset_game():
        st.session_state.ttt_game = TicTacToe()
        st.session_state.ttt_board = st.session_state.ttt_game.board.copy()
        st.session_state.ttt_state = st.session_state.ttt_game.get_state()
        st.session_state.ttt_msg = ""
        st.session_state.ttt_replay = []
        st.rerun()

    def player_move(row, col):
        moved = game.make_move(row, col, player=1)
        if moved:
            st.session_state.ttt_replay.append(game.get_state().copy())
            if not game.game_over():
                ai_turn()
            st.session_state.ttt_board = game.board.copy()
            st.rerun()

    def ai_turn():
        state_before = game.get_state().copy()
        available = game.get_available_actions()
        if use_trained_ai:
            action = agent.choose_action(state_before, available)
        else:
            action = random.choice(available)
        moved = game.make_move(action[0], action[1], player=-1)
        if moved:
            state_after = game.get_state().copy()
            st.session_state.ttt_replay.append(state_after)
            explanation = explain_move(state_before.reshape((3, 3)), state_after.reshape((3, 3)), -1)
            st.session_state.ttt_msg = explanation
        st.session_state.ttt_board = game.board.copy()

    def render_board():
        board = st.session_state.ttt_board
        cols = st.columns(3)
        for i in range(3):
            for j in range(3):
                cell = board[i][j]
                symbol = "❌" if cell == 1 else "⭕" if cell == -1 else ""
                if cols[j].button(symbol or " ", key=f"ttt_{i}-{j}"):
                    if cell == 0 and not game.game_over():
                        player_move(i, j)

    render_board()

    if st.session_state.ttt_msg:
        st.markdown(f"🧠 **AI says:** {st.session_state.ttt_msg}")

    # Game Result
    if game.current_winner == 1:
        st.success("🎉 You Win!")
    elif game.current_winner == -1:
        st.error("💀 AI Wins!")
    elif game.is_draw():
        st.info("🤝 It's a Draw!")

    col1, col2, col3 = st.columns(3)
    if col1.button("🔄 Restart Game", key="ttt_restart"):
        reset_game()

    if col2.button("📽 View Replay", key="ttt_view_replay"):
        if st.session_state.ttt_replay:
            st.markdown("### 🧠 Replay Steps")
            for idx, state in enumerate(st.session_state.ttt_replay):
                st.write(f"**Move {idx + 1}**")
                formatted = state.reshape((3, 3))
                board_html = "<table style='border-collapse: collapse;'>"
                for row in formatted:
                    board_html += "<tr>"
                    for cell in row:
                        symbol = "❌" if cell == 1 else "⭕" if cell == -1 else "&nbsp;"
                        board_html += f"<td style='width: 40px; height: 40px; border: 1px solid black; text-align: center; font-size: 24px;'>{symbol}</td>"
                    board_html += "</tr>"
                board_html += "</table>"
                st.markdown(board_html, unsafe_allow_html=True)

    st.sidebar.title("📂 Load Replay")
    replay_file = st.sidebar.file_uploader("Upload Replay (.json)", type=["json"], key="ttt_replay_upload")
    if replay_file:
        replay_data = json.load(replay_file)
        st.session_state.ttt_replay = [np.array(state) for state in replay_data]
        st.sidebar.success("Replay loaded! Click 'View Replay' to see it.")

    if col3.button("🗑 Clear Replay", key="ttt_clear"):
        st.session_state.ttt_replay = []
        st.rerun()

    if st.sidebar.button("💾 Save Replay", key="ttt_save"):
        if st.session_state.ttt_replay:
            file_path = "saved_replay.json"
            with open(file_path, "w") as f:
                json.dump([state.tolist() for state in st.session_state.ttt_replay], f)
            st.sidebar.success(f"Replay saved as `{file_path}`.")
        else:
            st.sidebar.warning("No replay data to save.")


