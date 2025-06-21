from game import player
from game import utils



if __name__ == "__main__":
    # Display start
    utils.Utils.display_game_name()
    utils.Utils.display_welcome()

    # Character creation
    classe_name = utils.Utils.display_classes_choices()
    player_name = utils.Utils.display_name_choice()

    plr = player.Character(player_name, classe_name)

    utils.Utils.display_intersection()

    # Game loop

    