from game import player
from game import utils


if __name__ == "__main__":
    player1 = player.Character("Nicolas", "elfe")
    utils.Utils.display_game_name()
    utils.Utils.display_welcome()
    utils.Utils.login_choice()
    utils.Utils.dipaly_life(player1)
    