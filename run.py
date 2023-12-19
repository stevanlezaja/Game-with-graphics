from src.const import *
from src.utils import *


if __name__ == "__main__":
    running, clock, screen = initialize_game()
    player = initialize_player()
    game_loop(running, clock, screen, player)


