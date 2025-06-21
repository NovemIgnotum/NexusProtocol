from game import player
from game import utils



if __name__ == "__main__":
    # Display start
    utils.Utils.display_game_name()
    utils.Utils.display_welcome()

    classe_name = utils.Utils.display_classes_choices()
    
    print(classe_name)