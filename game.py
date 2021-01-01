import random
import mancala



points_dict = {"B1": 4, "B2": 4, "B3": 4, "B4": 4, "B5": 4, "B6": 4, "B": 0, "A6": 4, "A5": 4, "A4": 4, "A3": 4,
               "A2": 4, "A1": 4, "A": 0}
buttons = ["B1", "B2", "B3", "B4", "B5", "B6", "B", "A6", "A5", "A4", "A3", "A2", "A1", "A"]
labels = {"B1": ["b11", "b12", "b13", "b14"], "B2": ["b21", "b22", "b23", "b24"], "B3": ["b31", "b32", "b33", "b34"],
          "B4": ["b41", "b42", "b43", "b44"], "B5": ["b51", "b52", "b53", "b54"], "B6": ["b61", "b62", "b63", "b64"],
          "B": [], "A6": ["a61", "a62", "a63", "a64"], "A5": ["a51", "a52", "a53", "a54"],
          "A4": ["a41", "a42", "a43", "a44"], "A3": ["a31", "a32", "a33", "a34"],
          "A2": ["a21", "a22", "a23", "a24"], "A1": ["a11", "a12", "a13", "a14"], "A": []}
buttons_clicked_by_calc=[]
player_0 = True
player_1 = False
value = 0
opponent = "calculator"  # care va fi player_1
buttons_calculator = ["",""]
initial_button = "A1"
current_labels = []
exception_2_buttons=[]
result_calc=[]

def get_buttons_clicked_by_calc():
    return buttons_clicked_by_calc
def set_opponent(oponentul):
    global oponent
    oponent = oponentul
def get_buttons_calculator():
    return buttons_calculator
def get_value():
    return value
def set_player(player):
    global player_1,player_0
    if player == 0:
        player_0 = True
    else:
        player_1 = True
def get_result_calc():
    return result_calc

def get_player():
    if player_1 is True:
        return 1  # B
    else:
        return 0  # A

def get_labels(button):
    return labels[button]
def get_points(button):
    return points_dict[button]

def check_order(button1, button2,player):
    # print("check_order")
    print("order", buttons.index(button1), buttons.index(button2))
    if (button1 == "A" and button2 == "B1") | (buttons.index(button1) == buttons.index(button2) - 1) | (button1 == "B6" and button2 == "A6" and player==0) | (button1 == "A1" and button2 == "B1" and player==1):
        return 1
    else:
        print("gresita ordinea")
        return 0  # a apasat gresit


def check_player_start(player, button):
    if button == "A" or button == "B":
        return 0
    if player == 0:
        if "A" not in button:
            return 0
    if player == 1:
        if "B" not in button:
            return 0
    return 1


def check_player(player,button):
    print(player)
    if player==0:
        if player_0 is True:
            return 0
        else:
            return 1
    else:
        if player_1 is True:
            return 0
        else:
            return 1


def check_exceptions(player, button):
    # print("check_exceptions")
    print("puncte/buton", points_dict[button])
    if (player == 1 and button == "B") | (player == 0 and button == "A"):
        return (1, 0)  # e din nou randul lui
    if (player == 1 and points_dict[button] == 0 and "B" in button):
        oponent_button = "A" + button[1]
        return (2, oponent_button)  # regula 2- va lua toate pietrele din groapa opusa
    if (player == 0 and points_dict[button] == 0 and "A" in button):
        oponent_button = "B" + button[1]
        return (2, oponent_button)  # regula 2- va lua toate pietrele din groapa opusa
    print("nicio exceptie")
    return (0, 0)  # nicio exceptie


def check_bank(button, player):
    # print("check_bank")
    if (player == 1 and button == "A") or (player == 0 and button == "B"):
        print("gresita banca")
        return 0  # a apasat gresit
    else:
        return 1


def check_game_over():
    if ((points_dict["A1"] == 0 and points_dict["A2"] == 0 and points_dict["A3"] == 0 and points_dict["A4"] == 0 and
        points_dict["A5"] == 0 and points_dict["A6"] == 0) | (
            points_dict["B1"] == 0 and points_dict["B2"] == 0 and points_dict["B3"] == 0 and points_dict["B4"] == 0 and
            points_dict["B5"] == 0 and points_dict["B6"] == 0)) and value==0:
        return 1
    else:
        return 0


def move_calculator():
    print("move_calculator")
    global buttons_calculator,result_calc,buttons_clicked_by_calc
    if value == 0:  # trebuie sa aleg un buton de pe care incep
        buttons_clicked_by_calc.clear()
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
        buttons_calculator[0]=button1
        buttons_calculator[1] = button2
        buttons_clicked_by_calc.append(button1)
        buttons_clicked_by_calc.append(button2)
        result_calc=update_points(button1, button2, 1)

    while value != 0:
        print("b2cald",buttons_calculator[1])
        button1 = buttons_calculator[1]
        buttons_calculator[0]=buttons_calculator[1]
        if buttons_calculator[1] == "B":
            button2 = "A6"
        elif buttons_calculator[1] == "A1":
            button2 = "B1"
        elif buttons_calculator[1]=="B6":
            button2="B"
        elif "A" in buttons_calculator[1]:
            print("inainte",buttons_calculator[1])
            button2 = "A" + str(int(buttons_calculator[1][1]) -1)
            print("but2calc",button2)
        elif "B" in buttons_calculator[1]:
            print("inainte",buttons_calculator[1])
            button2 = "B" + str(int(buttons_calculator[1][1]) +1)
            print("but2calc",button2)
        buttons_calculator[1]=button2
        buttons_clicked_by_calc.append(button2)
        # mancala.update_buttons_and_move_calc(button1,button2)
        result_calc=update_points(button1, button2, 1)
        # mancala.move_calc(button1,button2)
    # buttons_clicked_by_calc.clear()



def update_labels(inceput, button1, button2):
    global initial_button, current_labels
    print("inceput=",inceput)
    if inceput == 1:
        points_dict[button1] = 0
        # current_labels = labels[button1]
        # labels[button1] = []
    points_dict[button2] = points_dict[button2] + 1
    # print("cur-lab",current_labels)
    # labels[button2].append(current_labels[0])
    # current_labels.pop(0)

def get_exc2_buttons():
    return exception_2_buttons
def ver_start(button,player):
    if check_player(player,button)==0:
        if check_player_start(player,button):
            if value==0 and points_dict[button]!=0:
                return 1
    return 0

def update_points(button1, button2, player):
    # print("update_points")
    print(button1, button2, player)
    global value, points_dict, player_0, player_1, initial_button, current_labels,exception_2_buttons
    if check_player(player,button1) == 1:
        # a apasat gresit - nu e randul lui
        # print("returnez 00")
        return (0, 0)
    print("value", value)
    inceput = 0
    if value == 0:
        # abia a inceput mutarile
        inceput = 1
        if check_player_start(player, button1) == 0:
            return (0, 0)
        value = points_dict[button1]
        print("value dupa update", value)
        if value == 0:
            return (2, 0)
        else:
            initial_button = button1
    ok = 0
    bank = 0
    if button1 == "A" or button1 == "B":
        bank = 1

        ok = ok + check_bank(button1, player)
    if button2 == "A" or button2 == "B":
        bank = 1
        print("verific banci ", check_bank(button2,player))
        ok = ok + check_bank(button2, player)
    if ok == 2:
        # nu a mutat bine, dar ramane randul lui
        # print("returnez 01")
        return (0, 1)
    ok = ok + check_order(button1, button2,player)
    # print("ok da ",ok)
    print("TOATE PUNCTELE",points_dict)
    if (bank == 1 and ok == 2) or (bank == 0 and ok == 1):
        print("mutare ok")
        # cand valoarea e 0, trebuie afisat ce se intampla
        value = value - 1
        if value == 0:
            exception = check_exceptions(player, button2)
            if exception[0] == 0:
                update_labels(inceput, button1, button2)
                if player == 1:
                    player_1 = False
                    player_0 = True
                else:
                    player_1 = True
                    player_0 = False
                    # print("returnez 10")
                if check_game_over() == 1 and ((bank == 1 and ok == 2) or (
                        bank == 0 and ok == 1)):  # jocul s-a terminat, returnez si castigatorul
                    return (3, get_winner())
                return (1, 0)  # a mutat bine, i se termina randul
            elif exception[0] == 1:
                # print("returnez 11")
                update_labels(inceput, button1, button2)
                if check_game_over() == 1 and ((bank == 1 and ok == 2) or (
                        bank == 0 and ok == 1)):  # jocul s-a terminat, returnez si castigatorul
                    return (3, get_winner())
                return (1, 1)  # a mutat bine si exceptia e 1 => i se reia randul
            elif exception[0] == 2:
                print("exceptia2")
                exception_2_buttons=[button1,exception[1]]
                if player == 1:
                    player_1 = False
                    player_0 = True
                    points_dict["B"] = points_dict["B"] + points_dict[exception[1]]+1
                    # labels["B"] = labels["B"].append(labels[exception[1]])
                    # labels["B"].append(current_labels[0])
                else:
                    player_1 = True
                    player_0 = False
                    points_dict["A"] = points_dict["A"] + points_dict[exception[1]]+1
                    # labels["A"] = labels["A"].append(labels[exception[1]])
                    # labels["A"].append(current_labels[0])
                # points_dict[button1] = points_dict[button1] - 1
                # current_labels.pop(0)
                if initial_button==button1:
                    points_dict[button1] = points_dict[button1] - 1
                points_dict[exception[1]] = 0
                # labels[exception[1]] = []
                # print("returnez 12")
                if check_game_over() == 1 and ((bank == 1 and ok == 2) or (
                        bank == 0 and ok == 1)):  # jocul s-a terminat, returnez si castigatorul
                    return (3, get_winner())
                return (1, 2)  # a mutat bine, e exceptia 2 => i se termina randul
        else:  # nimic special
            update_labels(inceput, button1, button2)
            # print("returnez 13")
            if check_game_over() == 1 and (
                    (bank == 1 and ok == 2) or (bank == 0 and ok == 1)):  # jocul s-a terminat, returnez si castigatorul
                return (3, get_winner())
            return (1, 3)  # a mutat bine, continua
        if check_game_over() == 1 and ((bank == 1 and ok == 2) or (bank == 0 and ok == 1)) : # jocul s-a terminat, returnez si castigatorul
            return (3, get_winner())
    else:
        return (4, 2)


def get_final_points():
    global points_dict
    points_dict["B"] = points_dict["B1"] + points_dict["B2"] + points_dict["B3"] + points_dict["B4"] + points_dict[
        "B5"] + points_dict["B6"] + points_dict["B"]
    points_dict["A"] = points_dict["A1"] + points_dict["A2"] + points_dict["A3"] + points_dict["A4"] + points_dict[
        "A5"] + points_dict["A6"] + points_dict["A"]
    print("puncte!!!!!!!!!! ",points_dict)
    return points_dict["A"], points_dict["B"]


def get_winner():
    get_final_points()
    if points_dict["A"] > points_dict["B"]:
        return 1  # B
    else:
        return 0  # A
