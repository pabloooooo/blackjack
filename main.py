import sys

from blackjack import BlackjackGame
from player import HumanPlayer, AIPlayer

if __name__ == "__main__":
    # Default to AI player if no arguments are provided
    player_type = "ai" if len(sys.argv) == 1 else sys.argv[1].lower()

    if player_type == "human":
        player = HumanPlayer()
    else:  # Default case
        player = AIPlayer()

    game = BlackjackGame(player)
    game.play()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
