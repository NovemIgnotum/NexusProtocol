from game import player
from termcolor import colored, cprint


def display_game_name() :
    cprint("###############################################################", "red", attrs=["bold"])
    cprint("#                                                             #","red", attrs=["bold"])
    cprint("#" , "red", end="", attrs=["bold"])
    cprint("  ###   ####  ########   ###   ###  ###     ###   ########   ", "red", end="")
    cprint("#" , "red", attrs=["bold"])
    cprint("#" , "red", end="", attrs=["bold"])
    cprint("  ###  #####  ##          ### ###   ###     ###   #          ", "blue", end="" )
    cprint("#" , "red", attrs=["bold"])
    cprint("#" , "red", end="", attrs=["bold"])
    cprint("  ### ## ###  ########      ###     ###     ###   ########   ", "green", end="")
    cprint("#" , "red", attrs=["bold"])
    cprint("#" , "red", end="", attrs=["bold"])
    cprint("  #####  ###  ##         ###  ###   ###     ###          #   ", "magenta", end="")
    cprint("#" , "red", attrs=["bold"])
    cprint("#" , "red", end="", attrs=["bold"])
    cprint("  ###    ###  ########  ###    ###     #####      ########   ", "cyan", end="")
    cprint("#" , "red", attrs=["bold"])
    cprint("#                                                             #","red", attrs=["bold"])
    cprint("###############################################################","red", attrs=["bold"])

if __name__ == "__main__":
    player1 = player.Character("Nicolas", "elfe")
    player1.dipaly_life()
    