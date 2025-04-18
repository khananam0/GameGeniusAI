# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# import streamlit as st
# # Dynamically import the respective UIs
# print("============two==============")

# # Set Streamlit page config
# st.set_page_config(page_title="GameGenius AI", layout="centered")


# st.title("🎮 GameGenius AI")
# # Dropdown to select game
# game = st.selectbox("Choose a Game", ["Tic-Tac-Toe", "Chess"])


# # Conditional rendering based on selection

# if game == "Tic-Tac-Toe":
#     print("========Tic-Tac-Toe========")
#     import tictactoe_web
#     tictactoe_web.run()

# elif game == "Chess":
#     print("========Chess========")
#     import chess_web
#     chess_web.run()






import streamlit as st
from streamlit_option_menu import option_menu

# Import the game UI files
from chess_web import run as chess_run
from tictactoe_web import run as tictactoe_run

def main():
    # Set up the page layout and title
    st.set_page_config(page_title="GameGenius AI", layout="wide")
    st.title("GameGenius AI: Choose Your Game")
    st.caption("Select a game to play and enjoy!")

    # Sidebar navigation menu for game selection
    with st.sidebar:
        selected_game = option_menu("Select a Game", ["Chess", "Tic-Tac-Toe"], default_index=0, menu_icon="cast", orientation="vertical")

    # Clear previous game session state when switching games
    if selected_game == "Chess":
        # Clear Tic-Tac-Toe session state to ensure a fresh start
        if "tictactoe_game" in st.session_state:
            del st.session_state["tictactoe_game"]
        # Call the Chess game function
        chess_run()

    elif selected_game == "Tic-Tac-Toe":
        # Clear Chess session state to ensure a fresh start
        if "chess_game" in st.session_state:
            del st.session_state["chess_game"]
        # Call the Tic-Tac-Toe game function
        tictactoe_run()

if __name__ == "__main__":
    main()


