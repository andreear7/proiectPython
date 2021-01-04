import random

points_dict = {"B1": 4, "B2": 4, "B3": 4, "B4": 4, "B5": 4, "B6": 4, "B": 0, "A6": 4, "A5": 4, "A4": 4, "A3": 4,
               "A2": 4, "A1": 4, "A": 0}
buttons = ["B1", "B2", "B3", "B4", "B5", "B6", "B", "A6", "A5", "A4", "A3", "A2", "A1", "A"]

buttons_clicked_by_calc = []
player_0 = True
player_1 = False
value = 0
oponent = "calculator"
buttons_calculator = ["", ""]
initial_button = "A1"
current_labels = []
exception_2_buttons = []
result_calc = []


def get_buttons_clicked_by_calc():
    """
        returneaza butoanele "apasate" de calculator cand acesta muta
    """
    return buttons_clicked_by_calc


def set_opponent(oponentul):
    """
        seteaza oponentul
    """
    global oponent
    oponent = oponentul


def get_buttons_calculator():
    """
        returneaza ultimele 2 butoane "apasate" de calculator
    """
    return buttons_calculator


def get_value():
    """
        returneaza valuarea actuala a punctelor din "mana" jucatorilor
    """
    return value


def set_player(player):
    """
        seteaza playerul curent
    """
    global player_1, player_0
    if player == 0:
        player_0 = True
    else:
        player_1 = True


def get_result_calc():
    """
        returneaza rezultatul mutarii calculatorului
    """
    return result_calc


def get_player():
    """
        returneaza playerul curent
    """
    if player_1 is True:
        return 1  # B
    else:
        return 0  # A


def get_points(button):
    """
        returneaza valoarea curenta a punctelor unui buton
    """
    return points_dict[button]


def check_order(button1, button2, player):
    """
        verifica daca cele 2 butoane apasate de jucatorul sunt in ordinea corecta
        returneaza: 1 daca a apasat corect, 0 daca a apasat gresit
    """
    if (button1 == "A" and button2 == "B1") | (buttons.index(button1) == buttons.index(button2) - 1) | (
            button1 == "B6" and button2 == "A6" and player == 0) | (
            button1 == "A1" and button2 == "B1" and player == 1):
        return 1
    else:
        print("gresita ordinea")
        return 0


def check_player_start(player, button):
    """
        verifica daca playerul a inceput mutarea din partea lui: daca e player 1, butonul trebuie sa
        fie A1/../A6, daca e 0, trebuie sa fie B1/../B6
        returneaza: 1 daca a inceput corect, 0 daca a inceput gresit
    """
    if button == "A" or button == "B":
        return 0
    if player == 0:
        if "A" not in button:
            return 0
    if player == 1:
        if "B" not in button:
            return 0
    return 1


def check_player(player):
    """
        verifica playerul curent
        returneaza: 0 daca e setat corect, 1 daca nu
    """
    if player == 0:
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
    """
        verifica daca se indeplinesc conditiile pentru una din cele 2 exceptii
        returneaza: 1,0 daca e exceptia 1, 2,butonul_opus daca e exceptia 2 si 0,0 daca nu e nicio exceptie
    """
    if (player == 1 and button == "B") | (player == 0 and button == "A"):
        return 1, 0
    if player == 1 and points_dict[button] == 0 and "B" in button:
        oponent_button = "A" + button[1]
        return 2, oponent_button
    if player == 0 and points_dict[button] == 0 and "A" in button:
        oponent_button = "B" + button[1]
        return 2, oponent_button
    print("nicio exceptie")
    return 0, 0


def check_bank(button, player):
    """
        verifica daca jucatorul pune pietre in banca proprie, si nu in a adversarului
        returneaza: 1 daca a apasat corect, 0 daca a apasat gresit
    """
    if (player == 1 and button == "A") or (player == 0 and button == "B"):
        print("banca gresita")
        return 0
    else:
        return 1


def check_game_over():
    """
        verifica daca jocul s-a terminat: daca unul din jucatori are 0 puncte in toate gropile
        si playerul curent nu mai are pietre in mana
        returneaza: 1 daca jocul s-a terminat, 0 in caz contrar
    """
    if ((points_dict["A1"] == 0 and points_dict["A2"] == 0 and points_dict["A3"] == 0 and points_dict["A4"] == 0 and
         points_dict["A5"] == 0 and points_dict["A6"] == 0) | (
                points_dict["B1"] == 0 and points_dict["B2"] == 0 and points_dict["B3"] == 0 and points_dict[
            "B4"] == 0 and
                points_dict["B5"] == 0 and points_dict["B6"] == 0)) and value == 0:
        return 1
    else:
        return 0


def move_calculator():
    """
        functie pentru mutarea calculatorului
    """
    print("move_calculator")
    global buttons_calculator, result_calc, buttons_clicked_by_calc
    if value == 0:
        # alege random butonul de inceput
        buttons_clicked_by_calc.clear()
        button = random.randint(1, 6)
        button1 = "B" + str(button)
        # cat timp butonul are 0 puncte nu se poate incepe de pe el deci se alege altul
        while points_dict[button1] == 0:
            button = random.randint(1, 6)
            button1 = "B" + str(button)
        # se alege al 2-lea buton care va fi "apasat", conform regulilor jocului
        if button != 6:
            button += 1
            button2 = "B" + str(button)
        else:
            button2 = "B"
        # se actualizeaza variabilele care tin evidenta butoanelor "apasate" de calculator
        buttons_calculator[0] = button1
        buttons_calculator[1] = button2
        buttons_clicked_by_calc.append(button1)
        buttons_clicked_by_calc.append(button2)
        # se apeleaza functia care face update la puncte in functie de mutari
        result_calc = update_points(button1, button2, 1)

    while value != 0:
        # cat timp calculatorul mai "are in mana" pietre, continua sa mute conform regulilor
        button1 = buttons_calculator[1]
        buttons_calculator[0] = buttons_calculator[1]
        if buttons_calculator[1] == "B":
            button2 = "A6"
        elif buttons_calculator[1] == "A1":
            button2 = "B1"
        elif buttons_calculator[1] == "B6":
            button2 = "B"
        elif "A" in buttons_calculator[1]:
            button2 = "A" + str(int(buttons_calculator[1][1]) - 1)
        elif "B" in buttons_calculator[1]:
            button2 = "B" + str(int(buttons_calculator[1][1]) + 1)
        buttons_calculator[1] = button2
        buttons_clicked_by_calc.append(button2)
        result_calc = update_points(button1, button2, 1)


def update_labels(inceput, button1, button2):
    """
       face update la puncte: daca e inceput de mutare, seteaza pe 0 butonul si mereu adauga 1 la
       butonul al 2-lea
    """
    global initial_button, current_labels
    if inceput == 1:
        points_dict[button1] = 0
    points_dict[button2] = points_dict[button2] + 1


def get_exc2_buttons():
    """
        returneaza butoanele care trebuie updatate dupa exceptia 2
    """
    return exception_2_buttons


def ver_start(button, player):
    """
        verifica daca e inceput corect de mutare
        returneaza: 1 daca e inceput de mutare corect, 0 daca nu e inceput de mutare/ e gresit
    """
    if check_player(player) == 0:
        if check_player_start(player, button):
            if value == 0 and points_dict[button] != 0:
                return 1
    return 0


def update_points(button1, button2, player):
    """
        functia principala a jocului care updateaza punctele in functie de butoanele apasate
        returneaza: 0,0 daca nu e randul jucatorului care a apasat/ nu a inceput bine
                    2,0 daca groapa de pe care vrea sa inceapa e goala
                    0,1 daca jucatorul nu a mutat conform regulilor
                    1,0 daca e sfarsit de mutare corecta
                    1,1 daca e exceptia 1
                    1,2 daca e exceptia 2
                    1,3 daca e mutare corecta in curs
                    3,castigatorul daca jocul s-a terminat
                    4,2 in orice alt caz
    """
    print(button1, button2, player)
    global value, points_dict, player_0, player_1, initial_button, current_labels, exception_2_buttons
    if check_player(player) == 1:
        return 0, 0
    print("puncte in mana: ", value)
    inceput = 0
    if value == 0:
        # abia a inceput mutarile
        inceput = 1
        if check_player_start(player, button1) == 0:
            return 0, 0
        # punctele din mana vor fi punctele de pe primul buton apasat
        value = points_dict[button1]
        print("puncte in mana dupa update:", value)
        if value == 0:
            return 2, 0
        else:
            initial_button = button1
    ok = 0
    bank = 0
    if button1 == "A" or button1 == "B":
        bank = 1
        ok = ok + check_bank(button1, player)
    if button2 == "A" or button2 == "B":
        bank = 1
        ok = ok + check_bank(button2, player)
    if ok == 2:
        return 0, 1
    ok = ok + check_order(button1, button2, player)
    print("dictionarul actual al punctelor:", points_dict)
    if (bank == 1 and ok == 2) or (bank == 0 and ok == 1):
        print("mutare ok")
        # mutarea e corecta
        value = value - 1
        if value == 0:
            # daca mutarea s-a terminat, verific daca este vreo exceptie
            exception = check_exceptions(player, button2)
            if exception[0] == 0:
                # nu e nicio exceptie, deci se schimba jucatorul curent si se updateaza punctele normal
                update_labels(inceput, button1, button2)
                if player == 1:
                    player_1 = False
                    player_0 = True
                else:
                    player_1 = True
                    player_0 = False
                # verific daca dupa acest update al punctelor jocul s-a terminat
                if check_game_over() == 1 and ((bank == 1 and ok == 2) or (
                        bank == 0 and ok == 1)):
                    return 3, get_winner()
                return 1, 0
            elif exception[0] == 1:
                # este exceptia 1, ramane randul jucatorului curent si updatez punctele normal
                update_labels(inceput, button1, button2)
                # verific daca dupa acest update al punctelor jocul s-a terminat
                if check_game_over() == 1 and ((bank == 1 and ok == 2) or (
                        bank == 0 and ok == 1)):
                    return 3, get_winner()
                return 1, 1
            elif exception[0] == 2:
                # este exceptia 2, schimb playerul curent si updatez punctele conform exceptiei:
                # in banca playerului curent adaug 1+ punctele din groapa opusa, groapa opusa va avea 0
                # puncte si al 2-lea buton de asemenea
                exception_2_buttons = [button1, exception[1]]
                if player == 1:
                    player_1 = False
                    player_0 = True
                    points_dict["B"] = points_dict["B"] + points_dict[exception[1]] + 1
                else:
                    player_1 = True
                    player_0 = False
                    points_dict["A"] = points_dict["A"] + points_dict[exception[1]] + 1
                if initial_button == button1:
                    points_dict[button1] = points_dict[button1] - 1
                points_dict[exception[1]] = 0
                # verific daca dupa acest update al punctelor jocul s-a terminat
                if check_game_over() == 1 and ((bank == 1 and ok == 2) or (
                        bank == 0 and ok == 1)):
                    return 3, get_winner()
                return 1, 2
        else:
            # este o mutare in curs, fac update la puncte normal
            update_labels(inceput, button1, button2)
            return 1, 3
    else:
        return 4, 2


def get_final_points():
    """
        aduna toate punctele din gropi in banci, in functie de jucator
        returneaza punctele corespunzatoare jucatorilor dupa adunarea acestora
    """
    global points_dict
    points_dict["B"] = points_dict["B1"] + points_dict["B2"] + points_dict["B3"] + points_dict["B4"] + points_dict[
        "B5"] + points_dict["B6"] + points_dict["B"]
    points_dict["A"] = points_dict["A1"] + points_dict["A2"] + points_dict["A3"] + points_dict["A4"] + points_dict[
        "A5"] + points_dict["A6"] + points_dict["A"]
    print("punctele finale: ", points_dict)
    return points_dict["A"], points_dict["B"]


def get_winner():
    """
        returneaza castigatorul: 0 daca e A, 1 daca e B, 2 daca e remiza
    """
    get_final_points()
    if points_dict["A"] == points_dict["B"]:
        return 2
    if points_dict["A"] > points_dict["B"]:
        return 0
    else:
        return 1
