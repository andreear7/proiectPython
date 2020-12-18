import random

#de facut:
#testat functiile

points_dict = {"B1": 4, "B2": 4, "B3": 4, "B4": 4, "B5": 4, "B6": 4, "B": 0, "A6": 4, "A5": 4, "A4": 4, "A3": 4,
               "A2": 4, "A1": 4, "A": 0}
buttons = ["B1", "B2", "B3", "B4", "B5", "B6", "B", "A6", "A5", "A4", "A3", "A2", "A1", "A"]
player_1 = True
player_0 = False
value = 4
oponent = "calculator"  # care va fi player_1
button_2_calculator = 0


def set_oponent(oponentul):
    global oponent
    oponent = oponentul


def get_player():
    if player_1 is True:
        return 1  # B
    else:
        return 0  # A


def check_order(button1, button2):
    if not (button1 == "A" and button2 == "B1") | (buttons.index(button1) != buttons.index(button2) - 1):
        return 0  # a apasat gresit
    else:
        return 1


def check_player(player):
    if "player_" + player is True:
        return 0
    else:
        return 1


def check_exceptions(player, button):
    if (player == 1 and button == "B") | (player == 0 and button == "A"):
        return (1, 0)  # e din nou randul lui
    if (player == 1 & points_dict[button] == 0):
        oponent_button = "A" + button[1]
        return (2, oponent_button)  # regula 2- va lua toate pietrele din groapa opusa
    elif (player == 0 & points_dict[button] == 0):
        oponent_button = "B" + button[1]
        return (2, oponent_button)  # regula 2- va lua toate pietrele din groapa opusa
    return (0, 0)  # nicio exceptie


def check_bank(button, player):
    if (player == 1 and button == "A") or (player == 0 and button == "B"):
        return 0  # a apasat gresit
    else:
        return 1


def check_game_over():
    if (points_dict["A1"] == 0 and points_dict["A2"] == 0 and points_dict["A3"] == 0 and points_dict["A4"] == 0 and
        points_dict["A5"] == 0 and points_dict["A6"] == 0) | (
            points_dict["B1"] == 0 and points_dict["B2"] == 0 and points_dict["B3"] == 0 and points_dict["B4"] == 0 and
            points_dict["B5"] == 0 and points_dict["B6"] == 0):
        return 1
    else:
        return 0


def move_calculator():
    global button_2_calculator
    if value == 0:  # trebuie sa aleg un buton de pe care incep
        button = random.randint(1, 6)
        button1 = "B" + str(button)
        while points_dict[button1] == 0:
            button = random.randint(1, 6)
            button1 = "B" + str(button)
        if button != 6:
            button += 1
            button2 = "B" + str(button)
        else:
            button2 = "B"
        button_2_calculator = button2
        update_points(button1, button2, 1)
    while value != 0:
        button1 = button_2_calculator
        if button_2_calculator == "B":
            button2 = "A6"
        elif button_2_calculator == "A1":
            button2 = "B1"
        else:
            button2 = "B" + str(int(button_2_calculator[1]) + 1)
        update_points(button1, button2, 1)


def update_points(button1, button2, player):
    global value, points_dict, player_0, player_1
    if value == 0:
        if check_player(player) == 0:
            # a apasat gresit - nu e randul lui
            return (0, 0)
        else:
            # abia a inceput mutarile
            value = points_dict[button1]
    ok = 0
    bank = 0
    if button1 == "A" or button1 == "B":
        bank = 1
        ok = ok + check_bank(button1, player)
    if button2 == "A" or button2 == "B":
        bank = 1
        ok = ok + check_bank(button2, player)
    if ok == 2:
        # nu a mutat bine, dar e randul lui
        return (0, 1)
    ok = ok + check_order(button1, button2)
    if (bank == 1 and ok == 2) or (bank == 0 and ok == 1):
        # cand valoarea e 0, trebuie afisat ce se intampla
        value = value - 1
        if value == 0:
            if check_game_over() == 1:  # jocul s-a terminat, returnez si castigatorul
                return (3, get_winner())
            exception = check_exceptions(player, button2)
            if exception[0] == 0:
                points_dict[button1] = points_dict[button1] - 1
                points_dict[button2] = points_dict[button2] + 1
                if player == 1:
                    player_1 = False
                    player_0 = True
                else:
                    player_1 = True
                    player_0 = False
                return (1, 0)  # a mutat bine, i se termina randul
            elif exception[0] == 1:
                return (1, 1)  # a mutat bine si exceptia e 1 => i se reia randul
            elif exception[0] == 2:
                if player == 1:
                    player_1 = False
                    player_0 = True
                    points_dict["B"] = points_dict["B"] + points_dict[exception[1]]
                else:
                    player_1 = True
                    player_0 = False
                    points_dict["A"] = points_dict["A"] + points_dict[exception[1]]
                points_dict[button1] = points_dict[button1] - 1
                points_dict[exception[1]] = 0
                return (1, 2)  # a mutat bine, e exceptia 2 => i se termina randul
        else:  # nimic special
            points_dict[button1] = points_dict[button1] - 1
            points_dict[button2] = points_dict[button2] + 1
            return (1, 3)  # a mutat bine, continua


def get_final_points():
    global points_dict
    points_dict["B"] = points_dict["B1"] + points_dict["B2"] + points_dict["B3"] + points_dict["B4"] + points_dict[
        "B5"] + points_dict["B6"]
    points_dict["A"] = points_dict["A1"] + points_dict["A2"] + points_dict["A3"] + points_dict["A4"] + points_dict[
        "A5"] + points_dict["A6"]


def get_winner():
    get_final_points()
    if points_dict["A"] > points_dict["B"]:
        return 1  # A
    else:
        return 0  # B
