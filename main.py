from game import player
from game import utils



if __name__ == "__main__":
    # Display start
    utils.Utils.display_game_name()
    utils.Utils.display_welcome()

    # Character creation
    classe_name = utils.Utils.display_classes_choices()
    player_name = utils.Utils.display_name_choice()

    plr1 = player.Character(player_name, classe_name)
    plr2 = player.Character("Lou-anne", "Magicien")
    utils.Utils.display_intersection()

    plr2.display_life()

    plr1.attack(plr2)

    # Game loop

    