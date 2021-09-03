import random
import itertools
import time
import doctest


def GUNSLINGER_L1() -> dict:
    """Return Gunslinger level 1 info.

    :return: dictionary of the Gunslinger level 1 information
    """
    stats = {"class_name": "Gunslinger Apprentice",
             "class_id": 1,
             "attack_name": "Revolver",
             "max_hp": 25,
             "max_damage": 15,
             "crit_chance": 0,
             "min_crit": 0,
             "max_crit": 0,
             "accuracy": 9,
             "heal": 4}
    return stats


def GUNSLINGER_L2() -> dict:
    """Return Gunslinger level 2 info.

    :return: dictionary of the Gunslinger level 2 information
    """
    stats = {"class_name": "Gunslinger Adept",
             "class_id": 1,
             "attack_name": "Revolver",
             "max_hp": 30,
             "max_damage": 20,
             "crit_chance": 0,
             "min_crit": 0,
             "max_crit": 0,
             "accuracy": 9,
             "heal": 5}
    return stats


def GUNSLINGER_L3() -> dict:
    """Return Gunslinger level 3 info.

    :return: dictionary of the Gunslinger level 3 information
    """
    stats = {"class_name": "Gunslinger Master",
             "class_id": 1,
             "attack_name": "Revolver",
             "max_hp": 35,
             "max_damage": 25,
             "crit_chance": 0,
             "min_crit": 0,
             "max_crit": 0,
             "accuracy": 9,
             "heal": 6}
    return stats


def SCRAPPER_L1() -> dict:
    """Return Scrapper level 1 info.

    :return: dictionary of the Scrapper level 1 information
    """
    stats = {"class_name": "Scrapper Apprentice",
             "class_id": 2,
             "attack_name": "Rusty Shank",
             "max_hp": 20,
             "max_damage": 10,
             "crit_chance": 3,
             "min_crit": 10,
             "max_crit": 20,
             "accuracy": 8,
             "heal": 5}
    return stats


def SCRAPPER_L2() -> dict:
    """Return Scrapper level 2 info.

    :return: dictionary of the Scrapper level 2 information
    """
    stats = {"class_name": "Scrapper Adept",
             "class_id": 2,
             "attack_name": "Rusty Shank",
             "max_hp": 25,
             "max_damage": 15,
             "crit_chance": 3,
             "min_crit": 15,
             "max_crit": 25,
             "accuracy": 8,
             "heal": 6}
    return stats


def SCRAPPER_L3() -> dict:
    """Return Scrapper level 3 info.

    :return: dictionary of the Scrapper level 3 information
    """
    stats = {"class_name": "Scrapper Master",
             "class_id": 2,
             "attack_name": "Rusty Shank",
             "max_hp": 30,
             "max_damage": 20,
             "crit_chance": 3,
             "min_crit": 20,
             "max_crit": 30,
             "accuracy": 8,
             "heal": 7}
    return stats


def FIGHTER_L1() -> dict:
    """Return Fighter level 1 info.

    :return: dictionary of the Fighter level 1 information
    """
    stats = {"class_name": "Fighter Apprentice",
             "class_id": 3,
             "attack_name": "Brass Knuckles",
             "max_hp": 25,
             "max_damage": 25,
             "crit_chance": 1,
             "min_crit": 5,
             "max_crit": 10,
             "accuracy": 7,
             "heal": 3}
    return stats


def FIGHTER_L2() -> dict:
    """Return Fighter level 2 info.

    :return: dictionary of the Fighter level 2 information
    """
    stats = {"class_name": "Fighter Adept",
             "class_id": 3,
             "attack_name": "Brass Knuckles",
             "max_hp": 30,
             "max_damage": 25,
             "crit_chance": 1,
             "min_crit": 5,
             "max_crit": 10,
             "accuracy": 7,
             "heal": 4}
    return stats


def FIGHTER_L3() -> dict:
    """Return Fighter level 3 info.

    :return: dictionary of the Fighter level 3 information
    """
    stats = {"class_name": "Fighter Master",
             "class_id": 3,
             "attack_name": "Brass Knuckles",
             "max_hp": 35,
             "max_damage": 30,
             "crit_chance": 1,
             "min_crit": 5,
             "max_crit": 10,
             "accuracy": 7,
             "heal": 5}
    return stats


def ROGUE_L1() -> dict:
    """Return Rogue level 1 info.

    :return: dictionary of the Rogue level 1 information
    """
    stats = {"class_name": "Rogue Apprentice",
             "class_id": 4,
             "attack_name": "Sharpened Dagger",
             "max_hp": 20,
             "max_damage": 15,
             "crit_chance": 5,
             "min_crit": 1,
             "max_crit": 5,
             "accuracy": 10,
             "heal": 4}
    return stats


def ROGUE_L2() -> dict:
    """Return Rogue level 2 info.

    :return: dictionary of the Rogue level 2 information
    """
    stats = {"class_name": "Rogue Adept",
             "class_id": 4,
             "attack_name": "Sharpened Dagger",
             "max_hp": 25,
             "max_damage": 20,
             "crit_chance": 1,
             "min_crit": 1,
             "max_crit": 5,
             "accuracy": 10,
             "heal": 4}
    return stats


def ROGUE_L3() -> dict:
    """Return Rogue level 3 info.

    :return: dictionary of the Rogue level 3 information
    """
    stats = {"class_name": "Rogue Master",
             "class_id": 4,
             "attack_name": "Sharpened Dagger",
             "max_hp": 30,
             "max_damage": 25,
             "crit_chance": 1,
             "min_crit": 1,
             "max_crit": 5,
             "accuracy": 10,
             "heal": 5}
    return stats


def ENEMY_L1() -> dict:
    """Return tier 1 enemy info.

    :precondition: there must be a declared constant, RED()
    :precondition: there must be a declared constant, END()
    :return:  dictionary of the tier 1 enemy information
    """
    stats = {"name": f"{RED()}Dreamer of the Light{END()}",
             "saying": "With the righteous Light, I shall purge the world of your sin",
             "attack_name": "the Light of Repentance",
             "hp": 15,
             "max_damage": 10,
             "accuracy": 5,
             "exp": 35,
             "is_boss": False}
    return stats


def ENEMY_L2() -> dict:
    """Return tier 2 enemy info.

    :precondition: there must be a declared constant, RED()
    :precondition: there must be a declared constant, END()
    :return:  dictionary of the tier 2 enemy information
    """
    stats = {"name": f"{RED()}Acolyte of the Light{END()}",
             "saying": "May the Light have mercy on you, for I shall have none",
             "attack_name": "the Litany of the Faithful",
             "hp": 20,
             "max_damage": 15,
             "accuracy": 6,
             "exp": 50,
             "is_boss": False}
    return stats


def ENEMY_L3() -> dict:
    """Return tier 3 enemy info.

    :precondition: there must be a declared constant, RED()
    :precondition: there must be a declared constant, END()
    :return: a dictionary of the tier 3 enemy information
    """
    stats = {"name": f"{RED()}Brother of the Light{END()}",
             "saying": "Death is but the mildest torment that awaits you, vermin",
             "attack_name": "the Peon of Bitter Mercy",
             "hp": 25,
             "max_damage": 15,
             "accuracy": 7,
             "exp": 75,
             "is_boss": False}
    return stats


def ENEMY_STOCKADE() -> dict:
    """Return special encounter - stockade enemy info.

    :precondition: there must be a declared constant, RED()
    :precondition: there must be a declared constant, END()
    :return: a dictionary of the stockade enemy information
    """
    stats = {"name": f"{RED()}Prison Guard{END()}",
             "saying": "An escaped prisoner! I'll drag back your dead body myself",
             "attack_name": "a Stun Baton",
             "hp": 12,
             "max_damage": 10,
             "accuracy": 6,
             "exp": 25,
             "is_boss": False}
    return stats


def ENEMY_SHRINE() -> dict:
    """Return special encounter - shrine enemy info.

    :precondition: there must be a declared constant, RED()
    :precondition: there must be a declared constant, END()
    :return: a dictionary of the shrine enemy information
    """
    stats = {"name": f"{RED()}Crazed Fanatic{END()}",
             "saying": "I have seen the LIGHT and it is GOOD and I am AWAKE",
             "attack_name": "a Zealot's Devotion",
             "hp": 20,
             "max_damage": 25,
             "accuracy": 3,
             "exp": 75,
             "is_boss": False}
    return stats


def ENEMY_LIBRARY() -> dict:
    """Return special encounter - library enemy info.

    :precondition: there must be a declared constant, RED()
    :precondition: there must be a declared constant, END()
    :return: a dictionary of the library enemy information
    """
    stats = {"name": f"{RED()}Ancient Scribe{END()}",
             "saying": "You shall not have any of our secrets",
             "attack_name": "the Powers of Lost Knowledge",
             "hp": 12,
             "max_damage": 25,
             "accuracy": 5,
             "exp": 75,
             "is_boss": False}
    return stats


def BOSS() -> dict:
    """Return final boss info.

    :precondition: there must be a declared constant, YELLOW()
    :precondition: there must be a declared constant, END()
    :return: a dictionary of the final boss information
    """
    stats = {"name": f"{YELLOW()}High Priest of the Light{END()}",
             "saying": "All shall submit to the Light, or be scattered as dust in the wind. You have come far,\n "
                       "apostate, and killed many of the Children… but you shall not make it past me",
             "attack_name": "the Wrath of the Light",
             "hp": 50,
             "max_damage": 20,
             "accuracy": 8,
             "is_alive": True,
             "is_boss": True}
    return stats


def MAX_FLEE_DAMAGE() -> int:
    """Return max flee damage.

    :return: the max flee damage
    """
    return 3


def INITIATIVE_UPPERBOUND() -> int:
    """Return the upperbound of initiative roll.

    :return: the upperbound of initiative roll
    """
    return 100


def L2_EXP() -> int:
    """Return total exp needed to reach level 2.

    :return: total exp needed to reach level 2
    """
    return 100


def L3_EXP() -> int:
    """Return total exp needed to reach level 3.

    :return: the total exp needed to reach level 3
    """
    return 225


def RED() -> str:
    """Return string to color text red.

    :return:  string to color text red
    """
    return "\033[31m"


def GREEN() -> str:
    """Return string to color text green.

    :return: a string to color text green
    """
    return "\033[32m"


def BLUE() -> str:
    """Return string to color text blue.

    :return: a string to color text blue
    """
    return "\033[34m"


def YELLOW() -> str:
    """Return string to color text yellow.

    :return: a string to color text yellow
    """
    return "\033[33m"


def END() -> str:
    """Return string to end the text color.

    :return: a string that denotes an end to the text color
    """
    return "\033[0m"


def BOARD_LENGTH() -> int:
    """Return the length of the game board

    :return: an integer that represents the length of the game board.
    """
    return 25


def BOARD_WIDTH() -> int:
    """Return the width of the game board

    :return: an integer that represents the width of the game board.
    """
    return 25


def BOSS_POSITION() -> tuple:
    """Return the position of the final boss.

    :return: a tuple which represents the position of the final boss.
    """
    return 24, 24


def selection_text_color(text: str) -> str:
    """Color selection menu text.

    :param text: a string
    :precondition: there must be a declared constant, RED()
    :precondition: there must be a declared constant, BLUE()
    :precondition: there must be a declared constant, END()
    :postcondition: colors the text blue if the string is not "Quit", else color the text red
    :return: the text string, colored correctly

    >>> print(selection_text_color("Hello World")) # colors the string blue
    \033[34mHello World\033[0m

    >>> print(selection_text_color("Quit")) # colors the string red
    \033[31mQuit\033[0m
    """
    if text == "Quit":
        text = RED() + text + END()
    else:
        text = BLUE() + text + END()
    return text


def select_class() -> str:
    """Select a player class.

    :precondition: the only valid inputs are integers in range [1, 5] - will prompt user for another input otherwise
    :precondition: all conditions to successfully execute the function selection_text_color(text) must be met, so that
    it can be mapped onto the choices selection
    :postcondition: get a valid input from the user to determine the player character's class
    :postcondition: print out info describing the classes if "Info" is selected
    :return: the chosen input of the player if valid as a class selection
    """

    def class_details():
        """Print out class descriptions.

        :postcondition: print out the class descriptions
        """
        print()
        print("GUNSLINGERS: Gunslingers are highly accurate and do damage at a consistent rate. However, they cannot\n"
              "score critical hits. Gunslingers heal at a steady rate, and have moderate HP.\n")
        print("SCRAPPERS: Scrappers are able to score deadlier critical hits more often. However, their regular damage "
              "is\n quite low. Scrappers heal at a fast rate, and have low HP.\n")
        print("FIGHTERS: Fighters do larger amounts of damage in combat. However, they suffer from lower accuracy.\n"
              "Fighters heal at a slower rate, and have high HP.\n")
        print("ROGUES: Rogues will always win initiative checks and their attacks always hit. However, they do lower\n"
              "amounts of damage and critical damage. Rogues heal at a steady rate, and have low HP.\n")

    choices = ["Gunslinger", "Scrapper", "Fighter", "Rogue", "Info"]
    color_choices = map(selection_text_color, choices)
    for number, choice in enumerate(color_choices, 1):
        print(number, "-", choice)
    valid_inputs = ["1", "2", "3", "4"]
    input_chosen = False
    while not input_chosen:
        user_input = str(input("\nWhat class will you choose? Refer to 'Info' for details. "))
        class_details() if user_input == "5" else None
        input_chosen = True if user_input in valid_inputs else False
        if input_chosen:
            print(f"\nYou have chosen to be a {choices[int(user_input) - 1]}!")
            return user_input
        else:
            print("\nMake a selection.")


def make_character() -> dict:
    """Make a player character.

    :precondition: all conditions to successfully execute the function player_name() must be met
    :precondition: all conditions to successfully execute the function get_starting_stats() must be met
    :postcondition: correctly makes a player character
    :return: the player character's dictionary
    """

    def player_name() -> str:
        """Get the player name.

        :precondition: there must be a declared constant, GREEN()
        :precondition: there must be a declared constant, END()
        :postcondition: get the player's name based on the user input
        :return: the player character's name
        """
        character_name = input("\n...What is your name? ")
        print()
        character_name = GREEN() + character_name + END()
        return character_name

    def get_starting_stats() -> dict:
        """Get the starting stats from player's selected class.

        :precondition: all conditions to successfully execute the function select_class() must be met
        :precondition: there must be a declared constant, GUNSLINGER_L1()
        :precondition: there must be a declared constant, SCRAPPER_L1()
        :precondition: there must be a declared constant, FIGHTER_L1()
        :precondition: there must be a declared constant, ROGUE_L1()
        :postcondition: correctly get the dictionaries for a player's starting class after they make their selection
        :return: correct dictionary of the class stats
        """
        selection = select_class()
        if selection == "1":
            selected_class = GUNSLINGER_L1()
            return selected_class
        elif selection == "2":
            selected_class = SCRAPPER_L1()
            return selected_class
        elif selection == "3":
            selected_class = FIGHTER_L1()
            return selected_class
        else:
            selected_class = ROGUE_L1()
            return selected_class

    name = player_name()
    player_class = get_starting_stats()
    player_character = {"name": name,
                        "hp": player_class["max_hp"],
                        "class_name": player_class["class_name"],
                        "id": player_class["class_id"],
                        "level": 1,
                        "exp": 0,
                        "x_position": 0,
                        "y_position": 0,
                        "in_combat": False,
                        "is_alive": True
                        }
    print(f"\n{player_character['name']} is a {player_character['class_name']} at Level {player_character['level']}.")
    return player_character


def class_stats(player: dict) -> dict:  # stats are pulled from class dictionaries, with id's to identify which one
    """Get stats from the player's selected class.

    :param player: a dictionary
    :precondition: all conditions to successfully execute the function get_gunslinger_stats(player) must be met
    :precondition: all conditions to successfully execute the function get_scrapper_stats(player) must be met
    :precondition: all conditions to successfully execute the function get_fighter_stats(player) must be met
    :precondition: all conditions to successfully execute the function get_rogue_stats(player) must be met
    :postcondition: correctly gets the class stats of the player, depending on the player's class selection and their
    current level
    :return: correct dictionary of the class stats

    >>> test_character = {"id": 1, "level": 1}
    >>> class_stats(test_character)
    {'class_name': 'Gunslinger Apprentice', 'class_id': 1, 'attack_name': 'Revolver', 'max_hp': 25, 'max_damage': 15, \
'crit_chance': 0, 'min_crit': 0, 'max_crit': 0, 'accuracy': 9, 'heal': 4}

    >>> test_character = {"id": 2, "level": 2}
    >>> class_stats(test_character)
    {'class_name': 'Scrapper Adept', 'class_id': 2, 'attack_name': 'Rusty Shank', 'max_hp': 25, 'max_damage': 15, \
'crit_chance': 3, 'min_crit': 15, 'max_crit': 25, 'accuracy': 8, 'heal': 6}

    >>> test_character = {"id": 4, "level": 3}
    >>> class_stats(test_character)
    {'class_name': 'Rogue Master', 'class_id': 4, 'attack_name': 'Sharpened Dagger', 'max_hp': 30, 'max_damage': 25, \
'crit_chance': 1, 'min_crit': 1, 'max_crit': 5, 'accuracy': 10, 'heal': 5}
    """

    def get_gunslinger_stats(character: dict) -> dict:
        """Get stats if player is a Gunslinger class.

        :param character: a dictionary
        :precondition: character must be a dictionary containing the key ["id"] with a positive integer as a value
        :precondition: character must be a dictionary containing the key ["level"] with a positive integer as a value
        :precondition: there must be a declared constant, GUNSLINGER_L1()
        :precondition: there must be a declared constant, GUNSLINGER_L2()
        :precondition: there must be a declared constant, GUNSLINGER_L3()
        :postcondition: returns appropriate dictionaries of the Gunslinger class for the player's level
        :postcondition: if none of the conditionals are met, then return a False
        :return: correct dictionary if the character["id"] is 1 and character["level"] is 1, 2, or 3, else False
        """
        if character["level"] == 1:
            return GUNSLINGER_L1()
        elif character["level"] == 2:
            return GUNSLINGER_L2()
        elif character["level"] == 3:
            return GUNSLINGER_L3()

    def get_scrapper_stats(character: dict) -> dict:
        """Get stats if player is a Scrapper class.

        :param character: a dictionary
        :precondition: character must be a dictionary containing the key ["id"] with a positive integer as a value
        :precondition: character must be a dictionary containing the key ["level"] with a positive integer as a value
        :precondition: there must be a declared constant, SCRAPPER_L1()
        :precondition: there must be a declared constant, SCRAPPER_L2()
        :precondition: there must be a declared constant, SCRAPPER_L3()
        :postcondition: returns appropriate dictionaries of the Scrapper class for the player's level
        :postcondition: if none of the conditionals are met, then return a False
        :return: correct dictionary if the character["id"] is 2 and character["level"] is 1, 2, or 3, else False
        """
        if character["level"] == 1:
            return SCRAPPER_L1()
        elif character["level"] == 2:
            return SCRAPPER_L2()
        elif character["level"] == 3:
            return SCRAPPER_L3()

    def get_fighter_stats(character: dict) -> dict:
        """Get stats if player is a Fighter class.

        :param character: a dictionary
        :precondition: character must be a dictionary containing the key ["id"] with a positive integer as a value
        :precondition: character must be a dictionary containing the key ["level"] with a positive integer as a value
        :precondition: there must be a declared constant, FIGHTER_L1()
        :precondition: there must be a declared constant, FIGHTER_L2()
        :precondition: there must be a declared constant, FIGHTER_L3()
        :postcondition: returns appropriate dictionaries of the Fighter class for the player's level
        :postcondition: if none of the conditionals are met, then return a False
        :return: correct dictionary if the character["id"] is 3 and character["level"] is 1, 2, or 3, else False
        """
        if character["level"] == 1:
            return FIGHTER_L1()
        elif character["level"] == 2:
            return FIGHTER_L2()
        elif character["level"] == 3:
            return FIGHTER_L3()

    def get_rogue_stats(character: dict) -> dict:
        """Get stats if player is a Rogue class.

        :param character: a dictionary
        :precondition: character must be a dictionary containing the key ["id"] with a positive integer as a value
        :precondition: character must be a dictionary containing the key ["level"] with a positive integer as a value
        :precondition: there must be a declared constant, ROGUE_L1()
        :precondition: there must be a declared constant, ROGUE_L2()
        :precondition: there must be a declared constant, ROGUE_L3()
        :postcondition: returns appropriate dictionaries of the Rogue class for the player's level
        :postcondition: if none of the conditionals are met, then return a False
        :return: correct dictionary if the character["id"] is 4 and character["level"] is 1, 2, or 3, else False
        """
        if character["level"] == 1:
            return ROGUE_L1()
        elif character["level"] == 2:
            return ROGUE_L2()
        elif character["level"] == 3:
            return ROGUE_L3()

    if player["id"] == 1:
        stats = get_gunslinger_stats(player)
    elif player["id"] == 2:
        stats = get_scrapper_stats(player)
    elif player["id"] == 3:
        stats = get_fighter_stats(player)
    else:
        stats = get_rogue_stats(player)
    return stats


def make_board() -> dict:
    """Make the game board.

    The game board has unique areas, which have different descriptions. Usual areas will have generic descriptions.
    :postcondition: creates a 25x25 game board with coordinates and descriptions.
    :return: a dictionary containing room coordinates for keys and room descriptions for values.
    """

    def stockade_room_description(game_board: dict):
        """Write description for the stockade room area on the game board.

        :param game_board: a dictionary
        :precondition: game_board must be a dictionary with keys that are tuples representing coordinates from (0, 0) to
        (24, 24)
        :precondition: game_board must be a dictionary with values that are strings
        :postcondition: assigns stockade room descriptions as values to all matching coordinate keys
        """
        for key, value in game_board.items():
            x, y = key
            if x in range(5) and y in range(5):
                game_board[key] = "This is the stockade. You should get out of here, more guards might be coming..."

    def library_description(game_board: dict):
        """Write description for the library area on the game board.

        :param game_board: a dictionary
        :precondition: game_board must be a dictionary with keys that are tuples representing coordinates from (0, 0) to
        (24, 24)
        :precondition: game_board must be a dictionary with values that are strings
        :postcondition: assigns library room descriptions as values to all matching coordinate keys
        """
        for key, value in game_board.items():
            x, y = key
            if x in range(10) and y in range(10, 15):
                game_board[key] = "Thousands of books line the walls, and you can’t help but admire them. A wealth of" \
                                  "\ninformation like this, in the middle of this godforsaken place..."

    def shrine_description(game_board: dict):
        """Write description for the shrine area on the game board.

        :param game_board: a dictionary
        :precondition: game_board must be a dictionary with keys that are tuples representing coordinates from (0, 0) to
        (24, 24)
        :precondition: game_board must be a dictionary with values that are strings
        :postcondition: assigns shrine room descriptions as values to all matching coordinate keys
        """
        for key, value in game_board.items():
            x, y = key
            if x in range(16, 25) and y in range(0, 5):
                game_board[key] = "Beautiful stained glass windows send light bouncing around the room, a visual " \
                           "cornucopia.\nThis must be a shrine of some sort..."

    def final_area_description(game_board: dict):
        """Write description for the final area on the game board.

        :param game_board: a dictionary
        :precondition: game_board must be a dictionary with keys that are tuples representing coordinates from (0, 0) to
        (24, 24)
        :precondition: game_board must be a dictionary with values that are strings
        :postcondition: assigns final room descriptions as values to all matching coordinate keys
        """
        for key, value in game_board.items():
            x, y = key
            if x in range(20, 25) and y in range(20, 25):
                game_board[key] = "You sense that you are close to the exit, however you see a man in the distance… " \
                                  "his eyes\n pass over you, even though you are out of his line of sight. You feel " \
                                  "like you are being watched."

    rooms = itertools.cycle(["The air smells like must and ancient things long forgotten...",
                             "Your steps echo ominously off the stone walls...",
                             "Shadows dance on the dark walls, like raindrops on top of snow...",
                             "A strange but haunting hymn echoes around you..."])
    cords = [(x, y) for x in range(25) for y in range(25)]
    unscrambled_board = {cord: next(rooms) for cord in cords}
    scrambled_board_values = list(unscrambled_board.values())
    random.shuffle(scrambled_board_values)
    board = dict(zip(unscrambled_board, scrambled_board_values))
    stockade_room_description(board)
    library_description(board)
    shrine_description(board)
    final_area_description(board)
    board[(24, 24)] = "This is the final room. You see that man walking towards you, a hideous grin on his face.\nYou"\
                      " prepare yourself for a tough fight."
    return board


def get_user_choice(player: dict) -> str:
    """Get the a valid input for the user's next move.

    :precondition: player must be a dictionary containing the key ["name"] with a string as a value
    :precondition: the only valid inputs are integers in range [1, 5] - will prompt user for another input otherwise
    :precondition: all conditions to successfully execute the function selection_text_color(text) must be met, so that
    it can be mapped onto the choices selection
    :postcondition: get a valid input from the user to determine the player character's next step
    :return: the chosen input of the player if valid
    """
    choices = ["Move North", "Move East", "Move South", "Move West", "Quit"]
    color_choices = map(selection_text_color, choices)
    for number, choice in enumerate(color_choices, 1):
        print(number, "-", choice)
    valid_inputs = str([number for number, choice in enumerate(choices, 1)])
    input_chosen = False
    while not input_chosen:
        user_input = str(input(f"\nWhat will you do, {player['name']}? Enter a valid number. "))
        input_chosen = True if user_input in valid_inputs else False
        print("\nYou have quit the game. Better luck next time.") if user_input == "5" else None
        if input_chosen:
            return user_input
        else:
            print("\nMake a selection. ")


def player_location(player: dict) -> tuple:
    """Get the player's location.

    :param player: a dictionary
    :precondition: character is a dictionary that contains keys ["x_position"] and ["y_position"], whose values
    should be positive integers, respectively.
    :postcondition: returns coordinates of the player's location as a tuple
    :return: the location of the player

    >>> test_character = {"x_position": 0, "y_position": 0}
    >>> player_location(test_character)
    (0, 0)

    >>> test_character = {"x_position": 24, "y_position": 24}
    >>> player_location(test_character)
    (24, 24)
    """
    position = (player["x_position"], player["y_position"])
    return position


def move_player(player: dict) -> str:
    """Move the player around the game board.

    :param player: a dictionary
    :precondition: all conditions to successfully execute the function get_user_choice(player) must be met
    :precondition: all conditions to successfully execute the function player_location(player) must be met
    :precondition: all conditions to successfully execute the function validate_move(user_input, location) must be met
    :precondition: all conditions to successfully execute the function adjust_coords(user_input, player) must be met
    :postcondition: correctly moves the player around the board
    :return: the user input if the player entered "5" (ie. quitting the game, which does not move the player)
    """

    def adjust_coords(player_input: str, character: dict):
        """Adjust the player coordinates after the player moves.

        :param player_input: a string
        :param character: a dictionary
        :precondition: character is a dictionary that contains keys ["x_position"] and ["y_position"], whose values
        should be positive integers, respectively.
        :precondition: player_input must be a string representing a positive integer in range [1, 4]
        :postcondition: adjusts the coordinate values in the player dictionary correctly after movement
        """
        if player_input == "1":
            character["y_position"] -= 1
            print("\nYou moved North.")
        elif player_input == "2":
            character["x_position"] += 1
            print("\nYou moved East.")
        elif player_input == "3":
            character["y_position"] += 1
            print("\nYou moved South.")
        elif player_input == "4":
            character["x_position"] -= 1
            print("\nYou moved West.")
        position = player_location(player)
        print(f"\nYou are at position {position}")

    moved = False
    while not moved:
        user_input = get_user_choice(player)
        if user_input == "5":
            return user_input
        else:
            location = player_location(player)
            check_move_valid = validate_move(user_input, location)
            if check_move_valid:
                moved = True
                adjust_coords(user_input, player)
            else:
                print(f"\nYou can't go there! Make another input. Your position is {location}")


def validate_move(player_input: str, location: tuple) -> bool:
    """Check if player's move is valid.

    :param player_input: a string
    :param location: a tuple
    :precondition: character_location must be a tuple containing 2 elements, both positive integers
    :postcondition: assess if the movement input is actually valid relative to the user's position on the game board
    :return: a Boolean depending on if the move was valid

    >>> validate_move("1", (0, 0))
    False

    >>> validate_move("2", (24, 10))
    False

    >>> validate_move("3", (5, 5))
    True
    """
    if player_input == "1" and location in [(x, 0) for x in range(25)]:
        return False
    elif player_input == "2" and location in [(24, y) for y in range(25)]:
        return False
    elif player_input == "3" and location in [(x, 24) for x in range(25)]:
        return False
    elif player_input == "4" and location in [(0, y) for y in range(25)]:
        return False
    return True


def check_room(board: dict, player: dict) -> tuple:
    """Print the room description of the room that the player is in.

    :param board: a dictionary
    :param player: a dictionary
    :precondition: all conditions to successfully execute the function player_location(player) must be met
    :precondition: board must be a dictionary with keys that are tuples representing coordinates from (0, 0) to (24, 24)
    :precondition: board must be a dictionary with values that are strings
    :postcondition: print the description of the room that the player is currently in
    :return: the location of the player

    >>> test_board = make_board()
    >>> test_character = {"x_position": 0, "y_position": 0}
    >>> check_room(test_board, test_character)  # Only the room description will print
    <BLANKLINE>
    This is the stockade. You should get out of here, more guards might be coming...
    (0, 0)
    """
    location = player_location(player)
    print("\n" + board[location])
    return location


def check_combat(player: dict):
    """Check if combat will initiate.

    Combat will always start in (24,24) - the final boss location.

    :param player: a dictionary
    :precondition: all conditions to successfully execute the function player_location(player) must be met
    :precondition: player must be a dictionary containing the key ["in_combat"] with a Boolean as a value
    :postcondition: checks if the player character will encounter combat using a random number generator for odds, if
    the player is not at position (24, 24)
    :postcondition: makes sure the player encounters combat if they are at position (24, 24)
    :postcondition: adjusts the key ["in_combat"] in the player dictionary with a Boolean True if combat is initiated
    """
    if player_location(player) == BOSS_POSITION():
        player["in_combat"] = True
        print("\nThe time has come. You have to get out of here. Your freedom is at hand, and you are aware of how"
              " many bodies you have left in your wake. \n...This one, you think, is the last.")
    else:
        combat_rng = random.randint(1, 5)
        if combat_rng in range(1, 2):
            player["in_combat"] = True
            print("\nYou've been spotted! You have to defend yourself!")


def heal(player: dict):
    """Heal the player.

    Depending on the player's class, they will heal at different rates and have different amounts of HP.

    :param player: a dictionary
    :precondition: all conditions to successfully execute the function class_stats(player) must be met
    :precondition: player must be a dictionary containing the key ["hp"] with a positive integer > 0 as a value
    as a value
    :postcondition: adjusts the key ["hp"] in the player dictionary by the player class's heal value if combat is not
    initiated on that turn
    :postcondition: limits the maximum player HP based on the player's class

    >>> test_character = {"id": 1, "level": 1, "hp": 25}
    >>> print(test_character["hp"])
    25
    >>> heal(test_character)
    <BLANKLINE>
    You heal for 4 HP, and currently have 25 HP. Your max HP is 25 HP.
    >>> print(test_character["hp"])
    25

    >>> test_character = {"id": 1, "level": 2, "hp": 10}
    >>> print(test_character["hp"])
    10
    >>> heal(test_character)
    <BLANKLINE>
    You heal for 5 HP, and currently have 15 HP. Your max HP is 30 HP.
    >>> print(test_character["hp"])
    15
    """

    class_info = class_stats(player)
    if player["hp"] + class_info["heal"] > class_info["max_hp"]:
        player["hp"] = class_info["max_hp"]
    else:
        player["hp"] += class_info["heal"]
    print(f"\nYou heal for {class_info['heal']} HP, and currently have {player['hp']} HP. "
          f"Your max HP is {class_info['max_hp']} HP.")


def choose_fight() -> str:
    """Select if the player will fight or flee.

    :precondition: the only valid inputs are integers in range [1, 2] - will prompt user for another input otherwise
    :precondition: all conditions to successfully execute the function selection_text_color(text) must be met, so that
    it can be mapped onto the choices selection
    :postcondition: get a valid input from the user to determine the player character's next step
    :return: the chosen input of the player - a valid one, of course!
    """

    choices = ["Fight", "Flee"]
    color_choices = map(selection_text_color, choices)
    for number, choice in enumerate(color_choices, 1):
        print(number, "-", choice)
    valid_inputs = str([number for number, choice in enumerate(choices, 1)])
    input_chosen = False
    while not input_chosen:
        user_input = str(input("\nWill you fight or flee? Enter a valid number. "))
        input_chosen = True if user_input in valid_inputs else False
        if input_chosen:
            return user_input
        else:
            print("\nMake a selection.")


def make_mob(player: dict, boss: dict) -> dict:  # unique NPCs will spawn in special areas with various encounter rates
    """Generate an enemy NPC based on map areas.

    The final boss will always spawn when the player is at position (24, 24).

    :param player: a dictionary
    :param boss: a dictionary
    :precondition: all conditions to successfully execute the function player_location(player) must be met
    :precondition: all conditions to successfully execute the function stockade_mobs() must be met
    :precondition: all conditions to successfully execute the function library_mobs() must be met
    :precondition: all conditions to successfully execute the function shrine_mobs() must be met
    :precondition: all conditions to successfully execute the function final_mobs() must be met
    :precondition: all conditions to successfully execute the function normal_mobs() must be met
    :precondition: character is a dictionary that contains keys ["x_position"] and ["y_position"], whose values
    should be positive integers, respectively.
    :postcondition: correctly generates an enemy NPC
    :postcondition: if the player is at (24, 24) then spawn the final boss enemy NPC
    :return: the enemy NPC dictionary
    """

    def stockade_mobs() -> dict:
        """Generate enemy NPCs for the stockade area.

        :precondition: there must be a declared constant, ENEMY_L1()
        :precondition: there must be a declared constant, ENEMY_L2()
        :precondition: there must be a declared constant, ENEMY_STOCKADE()
        :postcondition: correctly generates an enemy based on random number generator
        :return: the randomly selected enemy NPC dictionary
        """
        mob_rng = random.randint(1, 10)
        if mob_rng in range(1, 6):
            enemy = ENEMY_STOCKADE()
        elif mob_rng in range(6, 9):
            enemy = ENEMY_L1()
        else:
            enemy = ENEMY_L2()
        return enemy

    def library_mobs() -> dict:
        """Generate enemy NPCs for the library area.

        :precondition: there must be a declared constant, ENEMY_L1()
        :precondition: there must be a declared constant, ENEMY_L2()
        :precondition: there must be a declared constant, ENEMY_LIBRARY()
        :postcondition: correctly generates an enemy based on random number generator
        :return: the randomly selected enemy NPC dictionary
        """

        mob_rng = random.randint(1, 10)
        if mob_rng in range(1, 6):
            enemy = ENEMY_L1()
        elif mob_rng in range(6, 9):
            enemy = ENEMY_L2()
        else:
            enemy = ENEMY_LIBRARY()
        return enemy

    def shrine_mobs() -> dict:
        """Generate enemy NPCs for the shrine area.

        :precondition: there must be a declared constant, ENEMY_L1()
        :precondition: there must be a declared constant, ENEMY_L2()
        :precondition: there must be a declared constant, ENEMY_SHRINE()
        :postcondition: correctly generates an enemy based on random number generator
        :return: the randomly selected enemy NPC dictionary
        """

        mob_rng = random.randint(1, 10)
        if mob_rng in range(1, 6):
            enemy = ENEMY_L1()
        elif mob_rng in range(6, 9):
            enemy = ENEMY_L2()
        else:
            enemy = ENEMY_SHRINE()
        return enemy

    def final_mobs() -> dict:
        """Generate enemy NPCs for the final area.

        :precondition: there must be a declared constant, ENEMY_L3()
        :postcondition: correctly generates an enemy
        :return: the enemy NPC dictionary
        """

        enemy = ENEMY_L3()
        return enemy

    def normal_mobs() -> dict:
        """Generate enemy NPCs for all other areas.

        :precondition: there must be a declared constant, ENEMY_L1()
        :precondition: there must be a declared constant, ENEMY_L2()
        :precondition: there must be a declared constant, ENEMY_L3()
        :postcondition: correctly generates an enemy based on random number generator
        :return: the randomly selected enemy NPC dictionary
        """

        mob_rng = random.randint(1, 10)
        if mob_rng in range(1, 6):
            enemy = ENEMY_L1()
        elif mob_rng in range(6, 9):
            enemy = ENEMY_L2()
        else:
            enemy = ENEMY_L3()
        return enemy

    if player_location(player) == BOSS_POSITION():
        mob = boss
    elif player["x_position"] in range(5) and player["y_position"] in range(5):
        mob = stockade_mobs()
    elif player["x_position"] in range(10) and player["y_position"] in range(10, 15):
        mob = library_mobs()
    elif player["x_position"] in range(16, 25) and player["y_position"] in range(0, 5):
        mob = shrine_mobs()
    elif player["x_position"] in range(20, 25) and player["y_position"] in range(20, 25):
        mob = final_mobs()
    else:
        mob = normal_mobs()
    return mob


def combat(player: dict, boss: dict):
    """Simulate game combat.

    :param player: a dictionary
    :param boss: a dictionary
    :precondition: all conditions to successfully execute the function make_mob(player, boss) must be met
    :precondition: all conditions to successfully execute the function choose_fight() must be met
    :precondition: all conditions to successfully execute the function initiative(player) must be met
    :precondition: all conditions to successfully execute the function combat_round(player, mob, initiative_winner)
    must be met
    :precondition: all conditions to successfully execute the function add_exp(player, mob) must be met
    :precondition: all conditions to successfully execute the function check_boss_alive(mob) must be met
    :precondition: all conditions to successfully execute the function flee_damage(player) must be met
    :precondition: player must be a dictionary containing the key ["name"] with a string as a value
    :precondition: player must be a dictionary containing the key ["in_combat"] with a Boolean as a value
    :precondition: player must be a dictionary containing the key ["is_alive"] with a Boolean as a value
    :precondition: player must be a dictionary containing the key ["hp"] with a positive integer as a value
    :postcondition: correctly simulates combat sequence
    :postcondition: adjust keys ["hp"], ["is_alive"] and ["in_combat"] for the player dictionary upon conclusion
    :postcondition: correctly marks boss as dead if boss is defeated
    """

    def combat_round(player_character: dict, mob_character: dict, initiative_win: str):
        """Simulate a round of combat.

        :param player_character: a dictionary
        :param mob_character: a dictionary
        :param initiative_win: a string
        :precondition: player_character must be a dictionary containing the key ["hp"] with a a positive integer > 0 as
        a value
        :precondition: player_character must be a dictionary containing the key ["in_combat"] with a Boolean as a value
        :precondition: player_character must be a dictionary containing the key ["is_alive"] with a Boolean as a value
        :precondition: mob_character must be a dictionary containing the key ["hp"] with a positive integer > 0 as a
        value
        :precondition: initiative_win must be "player", "mob" or "draw"
        :precondition: all conditions to successfully execute the function player_attack(player_character,
        mob_character) must be met
        :precondition: all conditions to successfully execute the function mob_attack(player_character, mob_character)
        must be met
        :postcondition: checks the damage taken by the player character and the enemy NPC
        :postcondition: adjusts the ["hp"] keys in the player_character and mob_character dictionaries respectively
        based on damage taken
        :postcondition: adjusts the ["in_combat"] key in the player_character dictionary if a condition is met removing
        the player from combat - ie. enemy NPC dies
        :postcondition: adjusts the ["is_alive"] key in the player_character dictionary to False if the player's hp
        drops to or below 0
        """

        if initiative_win == "player":
            player_attack(player_character, mob_character)
            if mob_character["hp"] <= 0:
                player_character["in_combat"] = False
            else:
                mob_attack(player_character, mob_character)
        if initiative_win == "mob":
            mob_attack(player_character, mob_character)
            if player_character["hp"] <= 0:
                player_character["in_combat"] = False
            elif player_character["in_combat"]:
                player_attack(player_character, mob_character)
        if initiative_win == "draw":
            print("\nBy some miracle, your attacks bounce off one another, leaving both parties unharmed!")

    mob = make_mob(player, boss)
    print(f"\nYou are confronted by a {mob['name']}. They say, '{mob['saying']}'.")
    while player["in_combat"] and player["is_alive"] and mob["hp"] >= 1:
        fight_input = choose_fight()
        if fight_input == "1":
            initiative_winner = initiative(player)
            combat_round(player, mob, initiative_winner)
            if mob["hp"] <= 0:
                add_exp(player, mob)
                check_boss_alive(mob)
            if player["hp"] <= 0:
                player["is_alive"] = False
        else:
            flee_damage(player)
            print("\nYou have successfully fled the fight...") if player["is_alive"] else None


def initiative(player: dict) -> str:
    """Determine initiative winner for combat.

    If the player is a Rogue class, they will always win initiative checks.
    :param player: a dictionary
    :precondition: there must be a declared constant, INITIATIVE_UPPERBOUND()
    :precondition: character must be a dictionary containing the key ["id"] with a positive integer as a value
    :postcondition: checks if the player character or the enemy NPC will strike first (or if they will tie) in a
    combat round, using a random number generator for odds
    :return: the winner of the initiative check, or "draw" if they are the same
    """

    player_initiative = random.randint(1, INITIATIVE_UPPERBOUND())
    mob_initiative = random.randint(1, INITIATIVE_UPPERBOUND())
    if player["id"] == 4 or player_initiative > mob_initiative:
        winner = "player"
        print("\nYou seize the initiative!")
    elif mob_initiative > player_initiative and player["id"] != 4:
        winner = "mob"
        print("\nYour opponent seizes the initiative!")
    else:
        winner = "draw"
    return winner


def player_attack(player: dict, mob: dict):
    """Simulate the player's attacking turn.

    :param player: a dictionary
    :param mob: a dictionary
    :precondition: all conditions to successfully execute the function class_stats(character) must be met
    :precondition: mob must be a dictionary containing the key ["hp"] with a positive integer as a value
    :precondition: mob must be a dictionary containing the key ["name"] with a string as a value
    :precondition: player must be a dictionary containing the key ["hp"] with a positive integer as a value
    :precondition: player must be a dictionary containing the key ["name"] with a string as a value
    """

    class_info = class_stats(player)
    damage = random.randint(1, class_info["max_damage"])
    if random.randint(1, 10) in range(class_info["accuracy"] + 1):
        if random.randint(1, 5) in range(class_info["crit_chance"] + 1):
            damage += random.randint(class_info["min_crit"], class_info["max_crit"])
            mob["hp"] -= damage
            print(f"\nA critical hit! {player['name']} attacks their opponent for {damage} HP of damage "
                  f"with their {class_info['attack_name']}! The {mob['name']} has {mob['hp']} HP "
                  f"remaining.")
        else:
            mob["hp"] -= damage
            print(f"\n{player['name']} attacks their opponent for {damage} HP of damage with their "
                  f"{class_info['attack_name']}! The {mob['name']} has {mob['hp']} HP remaining.")
    else:
        print(f"\n{player['name']} missed! The attack glances off harmlessly against the {mob['name']}...")


def mob_attack(player: dict, mob: dict):
    """Simulate the enemy's attacking turn.

    :param player: a dictionary
    :param mob: a dictionary
    :precondition: mob must be a dictionary containing the key ["is_boss"] with a Boolean as a value
    :precondition: mob must be a dictionary containing the key ["name"] with a string as a value
    :precondition: mob must be a dictionary containing the key ["max_damage"] with a positive integer as a value
    :precondition: mob must be a dictionary containing the key ["accuracy"] with a positive integer as a value
    :precondition: mob must be a dictionary containing the key ["attack_name"] with a string as a value
    :precondition: player must be a dictionary containing the key ["hp"] with a positive integer as a value
    :precondition: player must be a dictionary containing the key ["in_combat"] with a Boolean as a value
    :postcondition: calculates if the enemy NPC will flee in their turn
    :postcondition: adjusts the key ["hp"] of the player dictionary based on the damage that was generated,
    if the enemy NPC does not flee
    """

    if random.randint(1, 5) in range(1, 2) and not mob['is_boss']:
        print(f"\n{mob['name']} has fled the battle for fear of their life!\n")
        player["in_combat"] = False
    else:
        damage = random.randint(1, mob["max_damage"])
        if random.randint(1, 10) in range(mob["accuracy"] + 1):
            player["hp"] -= damage
            print(f"\n{mob['name']} attacks with {mob['attack_name']}, causing {player['name']} to "
                  f"take {damage} HP of damage. {player['name']} has {player['hp']} HP remaining.")
        else:
            print(f"\n{mob['name']} missed! {player['name']} dodges the attack effortlessly!")


def flee_damage(player: dict):
    """Simulate fleeing if player chooses not to fight.

    The player cannot flee from the final boss fight.

    :param player: a dictionary
    :precondition: player must be a dictionary containing the key ["hp"] with a positive integer > 0 as a value
    :precondition: there must be a declared constant, MAX_FLEE_DAMAGE()
    :precondition: player is a dictionary that contains keys ["x_position"] and ["y_position"], whose values
    should be positive integers, respectively.
    precondition: all conditions to successfully execute the function player_location(player) must be met
    :postcondition: checks if the player character will take damage upon fleeing using a random number generator for
    odds
    :postcondition: adjusts the key ["hp"] in the player dictionary accordingly if damage is taken, and the keys
    "x_position" and "y_position" are not the values 24 and 24
    :postcondition: if the keys ["x_position"] and ["y_position"] are the values 24 and 24, the print out that the
    player cannot flee from the encounter
    """

    if player_location(player) == BOSS_POSITION():
        print("\nYou can't flee from this fight!")
    else:
        flee_rng = random.randint(1, 5)
        damage = random.randint(1, MAX_FLEE_DAMAGE())
        if flee_rng in range(1, 2):
            player["hp"] -= damage
            player["in_combat"] = False
            print(f"\nYou have are attacked for {damage} HP! You have {player['hp']} HP left.")
            if player["hp"] <= 0:
                player["is_alive"] = False
        else:
            player["in_combat"] = False


def check_boss_alive(mob: dict):
    """Adjust the boss's "is_alive" value so that it is False, if the enemy is the boss.

    The game will end when the boss dies.

    :param mob: a dictionary
    :precondition: mob must have a key "is_boss" which has a Boolean value
    :precondition: mob must have a key "is_alive" which has a Boolean value
    :precondition: there must be a declared constant, GREEN()
    :precondition: there must be a declared constant, END()
    :postcondition: adjusts the "is_alive" value to False
    :postcondition: prints out a dialogue that denotes the end of the game (ie. when boss is dead)
    """

    if mob["is_boss"]:
        mob["is_alive"] = False
        print("You have won the battle - your enemy falls before you, cursing you with their last breath. You have"
              "managed to make it out alive, against all odds.")
        time.sleep(2)
        print("\nYou can barely feel your legs. You are lightheaded and your head is spinning, but you somehow"
              "managed to make it out of there. You have escaped. \nOver the horizon, the sun had just started to "
              "rise again, illuminating the pale lilac skies. \n\n...you cast your eyes upwards, and once more "
              "saw the stars...\n ")
        time.sleep(2)
        print(f"{GREEN()}THE END{END()}")


def add_exp(player: dict, mob: dict):
    """Add exp to player's exp points.

    The boss will not yield any exp points, as the game will end when they die.

    :param player: a dictionary
    :param mob: a dictionary
    :precondition: mob must be a dictionary containing the key ["is_boss"], which returns a Boolean
    :precondition: mob must be a dictionary containing the key ["exp"], which returns a positive integer
    :precondition: player must be a dictionary containing the key ["exp"], which returns a positive integer
    :precondition: player must be a dictionary containing the key ["name"], which returns a string
    :precondition: all conditions to successfully execute the function level_up(player) must be met
    :postcondition: correctly adjusts the key ["exp"] of the player dictionary if mob["is_boss"] returns a
     value of False
    :postcondition: correctly adjusts the key ["level"] of the player dictionary if the value of character["exp"]
    meets the leveling thresholds

    >>> test_character = {"name": "Susan", "id": 1, "level": 1, "exp": 0}
    >>> test_enemy = ENEMY_L1()
    >>> add_exp(test_character, test_enemy)
    <BLANKLINE>
    You have won the battle and honed your mastery.
    <BLANKLINE>
    You have gained 35 experience points.
    <BLANKLINE>
    Susan now has 35 experience points!
    <BLANKLINE>
    You are currently a level 1 Gunslinger Apprentice.
    >>> print(test_character["exp"])
    35
    """

    def level_up(character: dict):
        """Level up the player when they have sufficient exp.

        :param character: a dictionary
        :precondition: character must be a dictionary containing the key ["exp"], which returns a positive integer
        :precondition: character must be a dictionary containing the key ["level"], which returns a positive integer
        :precondition: there must be a declared constant, L2_EXP()
        :precondition: there must be a declared constant, L3_EXP()
        :precondition: all conditions to successfully execute the function class_stats(character) must be met
        :postcondition: correctly adjusts the key ["level"] of the character dictionary if the value of character["exp"]
        meets the leveling thresholds
        """

        if character["exp"] >= L2_EXP():
            character["level"] = 2
        if character["exp"] >= L3_EXP():
            character["level"] = 3
        if character["level"] == 3:
            print("\nYou've reached the maximum level.")
        class_info = class_stats(character)
        print(f"\nYou are currently a level {character['level']} {class_info['class_name']}.")

    if not mob["is_boss"]:
        print("\nYou have won the battle and honed your mastery.")
        print(f"\nYou have gained {mob['exp']} experience points.")
        player["exp"] += mob["exp"]
        print(f"\n{player['name']} now has {player['exp']} experience points!")
        level_up(player)


def print_board(player: dict, length: int, width: int):  # blue rooms on the map are special areas
    """Print out the game board map, with colors denoting room locations.

    :param player: a dictionary
    :param length: a positive integer
    :param width: a positive integer
    :precondition: length and width are >= 24 for all the special areas to print properly
    :precondition: character is a dictionary that contains keys ["x_position"] and ["y_position"], whose values
    should be positive integers, respectively.
    :postcondition: correctly prints out a colored game board
    """

    time.sleep(1.5)
    print(f"\n{YELLOW()}GAME MAP - Your current location is at 'x'. Make it to (24, 24) to escape.{END()}\n")
    time.sleep(2)
    for y in range(length):
        line = ""
        for x in range(width):
            if (x, y) == player_location(player):
                line += f"{GREEN()}[x]{END()}"
            elif (x in range(5) and y in range(5)) or (x in range(10) and y in range(10, 15)) or \
                    (x in range(16, 25) and y in range(0, 5)) or (x in range(20, 25) and y in range(20, 25)):
                line += f"{BLUE()}[ ]{END()}"
            else:
                line += "[ ]"
        print(line)
    print()


def intro_script():
    """Print out the intro script.

    :postcondition: Correctly prints out the introduction of the game.
    """

    print(f"{GREEN()}WELCOME TO SUSAN'S ORIGINAL TEXT BASED RPG GAME!{END()}\n")
    time.sleep(2)
    print("LONDON, 1890.")
    time.sleep(2)
    print("\nYou wake up, disoriented. It feels like you have been in a dream. Memories come back to you at an\n"
          "alarming rate — you don’t remember much, but you recall that you were attacked while travelling on the\n "
          "way back to Oxford. There is a feeling of pain spreading through your skull... you had been bound and\n"
          "knocked out by the assailants. The world slowly refocuses.")
    time.sleep(4)
    print("\nWho were they? You struggle to grasp at any piece of information that may help you. Then, an icy fear\n"
          "spreads through your veins. The Children of the Light. They were an end times cult that you had read about\n"
          "in The Telegraph — it was them, you were sure. But where were you now? What did they mean to do to you?\n"
          "Kill you? You had a terrible feeling about this.")
    time.sleep(4)
    print("\nThere are a few people around you in similar states of stupor. You check the pulse of some of them.\n"
          "They appear to be either unconscious — or, as you fearfully discover, dead. You need to get out of here.")
    time.sleep(4)
    print("\nLuckily, you manage to knock out the guard and steal his key, as well as a weapon he had on him. You\n"
          " have to escape the citadel before it’s too late...")
    time.sleep(4)


def game():
    """Initiate the game!

    :precondition: all functions needed for the game to run has their conditions met and are executed correctly
    :postcondition: correctly executes the game - you better run from those cultists!
    """

    board = make_board()
    boss = BOSS()
    character = make_character()
    while character["is_alive"] and boss["is_alive"]:
        print_board(character, BOARD_LENGTH(), BOARD_LENGTH())
        if move_player(character) == "5" or (check_room(board, character) == BOSS_POSITION() and not boss["is_alive"]):
            break
        else:
            check_combat(character)
            heal(character) if not character["in_combat"] else combat(character, boss)
            if not character["is_alive"]:
                print("You succumb to your injuries... blood drips form your wounds and everything goes black. "
                      "At least you died fighting, resisting until the last. GAME OVER.")


def main():
    """ Drive the program. """

    doctest.testmod(verbose=True)
    intro_script()
    game()


if __name__ == '__main__':
    main()
