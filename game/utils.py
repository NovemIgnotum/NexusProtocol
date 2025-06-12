from termcolor import colored, cprint
from game import player

class Utils :
    def display_game_name() :
        cprint("#################################################################", "red", attrs=["bold"])
        cprint("#################################################################", "red", attrs=["bold"])
        cprint("##                                                             ##","red", attrs=["bold"])
        cprint("##" , "red", end="", attrs=["bold"])
        cprint("  ###   ####  ########   ###   ###  ###     ###   ########   ", "red", end="")
        cprint("##" , "red", attrs=["bold"])
        cprint("##" , "red", end="", attrs=["bold"])
        cprint("  ###  #####  ##          ### ###   ###     ###   #          ", "blue", end="" )
        cprint("##" , "red", attrs=["bold"])
        cprint("##" , "red", end="", attrs=["bold"])
        cprint("  ### ## ###  ########      ###     ###     ###   ########   ", "green", end="")
        cprint("##" , "red", attrs=["bold"])
        cprint("##" , "red", end="", attrs=["bold"])
        cprint("  #####  ###  ##         ###  ###   ###     ###          #   ", "magenta", end="")
        cprint("##" , "red", attrs=["bold"])
        cprint("##" , "red", end="", attrs=["bold"])
        cprint("  ###    ###  ########  ###    ###     #####      ########   ", "cyan", end="")
        cprint("##" , "red", attrs=["bold"])
        cprint("##                                                             ##","red", attrs=["bold"])
        cprint("#################################################################","red", attrs=["bold"])
        cprint("#################################################################","red", attrs=["bold"])

    def display_welcome() :
        print("----------------------------------")
        print("| Bienvenue dans Nexus Protocole |")
        print("----------------------------------")

    def login_choice() -> int :
        print("1. You already have an account")
        print("2. You don't have an account")

        choice = input()
        while choice.isnumeric() == False:
            print("Merci de choisir une valeurs parmis les suivantes : ")
            print("1. You already have an account")
            print("2. You don't have an account")
            choice = input()

            if choice.isnumeric() and (int(choice) <= 0 or int(choice) > 2) :
                choice = "string to continue loop"

        
        return int(choice)


    def dipaly_life(p : player.Character):
        print("[", end="")
        life_percent = (p.health / p.max_health) * 100
        life_cube = "■" * int(life_percent / 5) + " " * int((100-life_percent) / 5)

        if life_percent < 20 : color = "red"
        elif life_percent < 50 : color = "light_red"
        else : color = "green"

        cprint(life_cube, color, attrs=["bold"], end="")
        print(f"] {p.health} / {p.max_health}")