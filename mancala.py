from PyQt5 import QtCore, QtWidgets
import time
import sys
from PyQt5.QtWidgets import QApplication
import game

opponent = "calculator"
buttons = [" ", " "]
player = 0
start = 0
game_over = 0


class MancalaGui(object):

    def setup_game_ui(self, mancala):
        """
            seteaza elementele legate de interfata
        """
        mancala.setWindowTitle("Mancala")
        mancala.resize(860, 500)
        self.centralwidget = QtWidgets.QWidget(mancala)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("border-image : url(m1.jpg) 0 0 0 0 stretch stretch;")

        # butonul de start/ revino la joc
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(250, 100, 350, 150))
        self.startButton.setText("Incepe jocul")
        self.startButton.setStyleSheet(
            "font: bold;font-size:20px; background-color:rgba(255, 255, 255, 0.45); border-image:none")
        self.startButton.clicked.connect(self.start)

        # butonul pentru regulament
        self.rulesButton = QtWidgets.QPushButton(self.centralwidget)
        self.rulesButton.setGeometry(QtCore.QRect(250, 270, 350, 150))
        self.rulesButton.setText("Regulament")
        self.rulesButton.setStyleSheet(
            "font: bold; font-size:20px;background-color:rgba(255, 255, 255, 0.45); border-image:none")
        self.rulesButton.clicked.connect(self.rules)

        mancala.setCentralWidget(self.centralwidget)
        mancala.show()

        # butonul de inapoi
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(20, 20, 45, 30))
        self.backButton.setStyleSheet(" border-image:url(back.png) 0 0 0 0")
        self.backButton.clicked.connect(self.back)
        self.backButton.setVisible(False)

        # labelul pe care va fi regulamentul
        self.reg_label = QtWidgets.QLabel(self.centralwidget)
        self.reg_label.setStyleSheet(
            "font: bold; font-size:14px;background-color:rgba(255, 255, 255, 0.45); border-image:none")
        self.reg_label.setGeometry(QtCore.QRect(100, 50, 650, 400))
        self.reg_label.setAlignment(QtCore.Qt.AlignCenter)

        # labelul pentru informatiile legate de joc
        self.text_label = QtWidgets.QLabel(self.centralwidget)
        self.text_label.setStyleSheet(
            "font: bold; font-size:14px;background-color: rgb(234, 236, 238); border-image:none")
        self.text_label.setGeometry(QtCore.QRect(70, 50, 750, 20))
        self.text_label.setAlignment(QtCore.Qt.AlignCenter)
        self.text_label.setText("")
        self.text_label.setVisible(False)

        # tabla
        self.board_label = QtWidgets.QLabel(self.centralwidget)
        self.board_label.setStyleSheet("border-radius:50px;font: bold; font-size:14px; border-image: url(wm.jpg)")
        self.board_label.setGeometry(QtCore.QRect(65, 110, 743, 280))
        self.board_label.setAlignment(QtCore.Qt.AlignCenter)

        # butoanele de pe tabla - gropile si bancile din joc
        self.A1Button = QtWidgets.QPushButton(self.centralwidget)
        self.A1Button.setGeometry(185, 140, 80, 80)
        self.A1Button.setStyleSheet(
            "background-image:url(wm1.jpg);border-radius : 40; background-color:rgb(222,184,135);"
            "font-size:16px; font:bold")
        self.A1Button.setText("4\n🟣  🟣 \n🟣  🟣")
        self.A1Button.clicked.connect(self.a1)
        self.A1Button.setVisible(False)

        self.A2Button = QtWidgets.QPushButton(self.centralwidget)
        self.A2Button.setGeometry(270, 140, 80, 80)
        self.A2Button.setStyleSheet(
            "background-image:url(wm1.jpg);border-radius : 40; background-color:rgb(222,184,135);"
            "font-size:16px; font:bold")
        self.A2Button.setText("4\n🟣  🟣 \n🟣  🟣")
        self.A2Button.clicked.connect(self.a2)
        self.A2Button.setVisible(False)

        self.A3Button = QtWidgets.QPushButton(self.centralwidget)
        self.A3Button.setGeometry(355, 140, 80, 80)
        self.A3Button.setStyleSheet(
            "background-image:url(wm1.jpg);border-radius : 40; background-color:rgb(222,184,135);"
            "font-size:16px; font:bold")
        self.A3Button.setText("4\n🟣  🟣 \n🟣  🟣")
        self.A3Button.clicked.connect(self.a3)
        self.A3Button.setVisible(False)

        self.A4Button = QtWidgets.QPushButton(self.centralwidget)
        self.A4Button.setGeometry(440, 140, 80, 80)
        self.A4Button.setStyleSheet(
            "background-image:url(wm1.jpg);border-radius : 40; background-color:rgb(222,184,135);"
            "font-size:16px; font:bold")
        self.A4Button.setText("4\n🟣  🟣 \n🟣  🟣")
        self.A4Button.clicked.connect(self.a4)
        self.A4Button.setVisible(False)

        self.A5Button = QtWidgets.QPushButton(self.centralwidget)
        self.A5Button.setGeometry(525, 140, 80, 80)
        self.A5Button.setStyleSheet(
            "background-image:url(wm1.jpg);border-radius : 40; background-color:rgb(222,184,135);"
            "font-size:16px; font:bold")
        self.A5Button.setText("4\n🟣  🟣 \n🟣  🟣")
        self.A5Button.clicked.connect(self.a5)
        self.A5Button.setVisible(False)

        self.A6Button = QtWidgets.QPushButton(self.centralwidget)
        self.A6Button.setGeometry(610, 140, 80, 80)
        self.A6Button.setStyleSheet(
            "background-image:url(wm1.jpg);border-radius : 40; background-color:rgb(222,184,135);"
            "font-size:16px; font:bold")
        self.A6Button.setText("4\n🟣  🟣 \n🟣  🟣")
        self.A6Button.clicked.connect(self.a6)
        self.A6Button.setVisible(False)

        self.AButton = QtWidgets.QPushButton(self.centralwidget)
        self.AButton.setGeometry(80, 140, 100, 220)
        self.AButton.setStyleSheet(
            "background-image:url(wm1.jpg);border-radius : 40; background-color:rgb(222,184,135);"
            "font-size:16px; font:bold")
        self.AButton.setText("0")
        self.AButton.clicked.connect(self.a)
        self.AButton.setVisible(False)

        self.BButton = QtWidgets.QPushButton(self.centralwidget)
        self.BButton.setGeometry(693, 140, 100, 220)
        self.BButton.setStyleSheet(
            "background-image:url(wm1.jpg);border-radius : 40; background-color:rgb(222,184,135);"
            "font-size:16px; font:bold")
        self.BButton.setText("0")
        self.BButton.clicked.connect(self.b)
        self.BButton.setVisible(False)

        self.B1Button = QtWidgets.QPushButton(self.centralwidget)
        self.B1Button.setGeometry(185, 280, 80, 80)
        self.B1Button.setStyleSheet(
            "background-image:url(wm1.jpg);border-radius : 40; background-color:rgb(222,184,135);"
            "font-size:16px; font:bold")
        self.B1Button.setText("4\n🟣  🟣 \n🟣  🟣")
        self.B1Button.clicked.connect(self.b1)
        self.B1Button.setVisible(False)

        self.B2Button = QtWidgets.QPushButton(self.centralwidget)
        self.B2Button.setGeometry(270, 280, 80, 80)
        self.B2Button.setStyleSheet(
            "background-image:url(wm1.jpg);border-radius : 40; background-color:rgb(222,184,135);"
            "font-size:16px; font:bold")
        self.B2Button.setText("4\n🟣  🟣 \n🟣  🟣")
        self.B2Button.clicked.connect(self.b2)
        self.B2Button.setVisible(False)

        self.B3Button = QtWidgets.QPushButton(self.centralwidget)
        self.B3Button.setGeometry(355, 280, 80, 80)
        self.B3Button.setStyleSheet(
            "background-image:url(wm1.jpg);border-radius : 40; background-color:rgb(222,184,135);"
            "font-size:16px; font:bold")
        self.B3Button.setText("4\n🟣  🟣 \n🟣  🟣")
        self.B3Button.clicked.connect(self.b3)
        self.B3Button.setVisible(False)

        self.B4Button = QtWidgets.QPushButton(self.centralwidget)
        self.B4Button.setGeometry(440, 280, 80, 80)
        self.B4Button.setStyleSheet(
            "background-image:url(wm1.jpg);border-radius : 40; background-color:rgb(222,184,135);"
            "font-size:16px; font:bold")
        self.B4Button.setText("4\n🟣  🟣 \n🟣  🟣")
        self.B4Button.clicked.connect(self.b4)
        self.B4Button.setVisible(False)

        self.B5Button = QtWidgets.QPushButton(self.centralwidget)
        self.B5Button.setGeometry(525, 280, 80, 80)
        self.B5Button.setStyleSheet(
            "background-image:url(wm1.jpg);border-radius : 40; background-color:rgb(222,184,135);"
            "font-size:16px; font:bold")
        self.B5Button.setText("4\n🟣  🟣 \n🟣  🟣")
        self.B5Button.clicked.connect(self.b5)
        self.B5Button.setVisible(False)

        self.B6Button = QtWidgets.QPushButton(self.centralwidget)
        self.B6Button.setGeometry(610, 280, 80, 80)
        self.B6Button.setStyleSheet(
            "background-image:url(wm1.jpg);border-radius : 40; background-color:rgb(222,184,135);"
            "font-size:16px; font:bold")
        self.B6Button.setText("4\n🟣  🟣 \n🟣  🟣")
        self.B6Button.clicked.connect(self.b6)
        self.B6Button.setVisible(False)

    def set_board_visible(self, value):
        """
            face vizibila/invizibila tabla
        """
        self.board_label.setVisible(value)
        self.A1Button.setVisible(value)
        self.A2Button.setVisible(value)
        self.A3Button.setVisible(value)
        self.A4Button.setVisible(value)
        self.A5Button.setVisible(value)
        self.A6Button.setVisible(value)
        self.AButton.setVisible(value)
        self.BButton.setVisible(value)
        self.B1Button.setVisible(value)
        self.B2Button.setVisible(value)
        self.B3Button.setVisible(value)
        self.B4Button.setVisible(value)
        self.B5Button.setVisible(value)
        self.B6Button.setVisible(value)
        self.text_label.setVisible(value)

    def start(self):
        """
            face cele 2 butoane de la inceput invizibile si tabla vizibila
        """
        self.startButton.setVisible(False)
        self.rulesButton.setVisible(False)
        self.backButton.setVisible(True)
        self.centralwidget.setStyleSheet("border-image:none; background-color: rgb(234, 236, 238);")
        self.set_board_visible(True)
        global start
        # daca jocul incepe acum, afiseaza un mesaj corespunzator si seteaza variabila start pe 1
        if start == 0:
            self.text_label.setStyleSheet("font: bold; font-size:16px; color:green")
            self.text_label.setText("Jocul a inceput! Primul este A!")
            start = 1

    def rules(self):
        """
            functie pentru afisarea regulamentului: seteaza textul labelului de regulament si il face vizibil,
            face invizibile celelalte elemente si adauga butonul de back pentru a reveni la meniu
        """
        self.startButton.setVisible(False)
        self.rulesButton.setVisible(False)
        self.backButton.setVisible(True)
        self.reg_label.setVisible(True)
        self.reg_label.setText("REGULAMENT:\n\nScopul jocului: castiga cel cu cele mai multe pietricele in banca la "
                               "sfarsitul jocului.\n Reguli de joc: Tabla de joc se aseaza intre jucatori.\n Groapa "
                               "mai "
                               "larga din dreapta unui jucator este banca (mancala) sa.\n Pietricelele sunt asezate in "
                               "cele 12 gropi, cate 4 in fiecare groapa. Nu se pun pietricele in banci.\n Cand ii vine "
                               "randul unui jucator acesta ia pietricelele din oricare groapa de pe partea sa si\n "
                               "pune "
                               "una cate una, in celelalte gropi, in sens invers acelor de ceasornic,\n inclusiv in "
                               "banca sa. Nu se pun pietricele in banca adversarului.\n Groapa in care a ajuns ultima "
                               "pietricica determina cele doua reguli de joc: \n1. Daca ultima pietricica a cazut in "
                               "banca jucatorului care a mutat, acesta mai are dreptul la\n inca o mutare. 2. Daca "
                               "ultima pietricica a cazut intr-una din gropile jucatorului care a mutat\n si aceasta "
                               "era goala atunci captureaza in banca sa toate pietricelele adversarului (daca sunt)\n "
                               "din groapa opusa + pietricica pe care a pus-o in groapa.\n Sfarsitul jocului: Jocul se "
                               "termina atunci cand un jucator nu mai are nici o pietricica\n in gropile de pe partea "
                               "sa de joc. Restul pietricelelor se pun in banca celuilalt jucator.\n Fiecare jucator "
                               "isi numara pietricelele din banca.\n Jucatorul care are cele mai multe pietricele in "
                               "banca sa a castigat!")

    def back(self):
        """
            functie pentru butonul de back: schimba textul butonului de start daca jocul a inceput,
            schimba vizibilitatea elementelor astfel incat sa apara doar meniul
        """
        if start == 1:
            self.startButton.setText("Inapoi la joc")
        self.reg_label.setVisible(False)
        self.backButton.setVisible(False)
        self.startButton.setVisible(True)
        self.rulesButton.setVisible(True)
        self.centralwidget.setStyleSheet("border-image : url(m1.jpg) 0 0 0 0 stretch stretch;")
        self.set_board_visible(False)

    def set_zero(self):
        """
            apelata cand jocul s-a terminat, seteaza textul tuturor butoanelor considerate gropi la 0
        """
        self.A1Button.setText("0")
        self.A2Button.setText("0")
        self.A3Button.setText("0")
        self.A4Button.setText("0")
        self.A5Button.setText("0")
        self.A6Button.setText("0")
        self.B1Button.setText("0")
        self.B2Button.setText("0")
        self.B3Button.setText("0")
        self.B4Button.setText("0")
        self.B5Button.setText("0")
        self.B6Button.setText("0")

    def convert_str_to_button(self, string):
        """
            converteste numele butoanelor la butoane
        """
        if string == "A":
            return self.AButton
        if string == "A1":
            return self.A1Button
        if string == "A2":
            return self.A2Button
        if string == "A3":
            return self.A3Button
        if string == "A4":
            return self.A4Button
        if string == "A5":
            return self.A5Button
        if string == "A6":
            return self.A6Button
        if string == "B":
            return self.BButton
        if string == "B1":
            return self.B1Button
        if string == "B2":
            return self.B2Button
        if string == "B3":
            return self.B3Button
        if string == "B4":
            return self.B4Button
        if string == "B5":
            return self.B5Button
        if string == "B6":
            return self.B6Button

    def block_buttons(self):
        """
            functie apelata la terminarea jocului: blocheaza toate butoanele
        """
        self.A1Button.setDisabled(True)
        self.A2Button.setDisabled(True)
        self.A3Button.setDisabled(True)
        self.A4Button.setDisabled(True)
        self.A5Button.setDisabled(True)
        self.A6Button.setDisabled(True)
        self.AButton.setDisabled(True)
        self.BButton.setDisabled(True)
        self.B1Button.setDisabled(True)
        self.B2Button.setDisabled(True)
        self.B3Button.setDisabled(True)
        self.B4Button.setDisabled(True)
        self.B5Button.setDisabled(True)
        self.B6Button.setDisabled(True)

    def convert_points_to_text(self, points):
        """
            converteste punctele la un text mai atractiv vizual
        """
        if points == 0:
            text = "0"
        elif points == 1:
            text = "1\n 🟣"
        elif points == 2:
            text = "2\n🟣   🟣"
        elif points == 3:
            text = "3\n🟣   🟣\n   🟣"
        elif points == 4:
            text = "4\n🟣   🟣\n🟣   🟣"
        elif points == 5:
            text = "5\n🟣   🟣\n🟣🟣🟣"
        elif points == 6:
            text = "6\n🟣🟣🟣\n🟣🟣🟣"
        elif points == 7:
            text = "7\n🟣 \n🟣🟣🟣\n🟣🟣🟣"
        elif points == 8:
            text = "8\n🟣   🟣\n🟣🟣🟣\n🟣🟣🟣"
        elif points == 9:
            text = "9\n🟣🟣🟣\n🟣🟣🟣\n🟣🟣🟣"
        else:
            text = str(points)
        return text

    def play(self):
        """
            functia comunica cu "game.py" pentru a actualiza in interfata punctele jucatorilor si pentru
            a-i informa starea jocului si rezultatul mutarilor
            returneaza: numarul de puncte pentru butonul apasat daca mutarea e corecta, -1 in caz contrar
                        -2 daca jocul s-a terminat
        """
        self.text_label.setStyleSheet("font: bold; font-size:14px; color:black")
        self.text_label.setText("")
        ok = 1
        global buttons, player, start, game_over
        # apeleaza functia update_points din game.py pentru a afla care e rezultatul mutarii
        # rezultatul are 2 componente
        if opponent == "om" or (opponent == "calculator" and player == 0):
            result = game.update_points(buttons[0], buttons[1], player)
        elif opponent == "calculator" and player == 1:
            result = game.get_result_calc()
        print("result e ", result[0], result[1])
        # 0,0 semnifica faptul ca utilizatorul a apasat gresit( pe partea celuilalt) sau
        # oponentul a incercat sa-si mute piesele lui cand nu era randul sau
        if result[0] == 0 and result[1] == 0:
            self.text_label.setStyleSheet("font: bold; font-size:16px; color:red")
            self.text_label.setText("Nu este randul tau!")
            buttons[0] = " "
            buttons[1] = " "
            ok = 0
            QApplication.processEvents()
        # 0,1 sau 4,2 semnifica o mutare gresita din punct de vedere a regulilor jocului
        if (result[0] == 0 and result[1] == 1) or (result[0] == 4 and result[1] == 2):
            self.text_label.setStyleSheet("font: bold; font-size:16px; color:red")
            self.text_label.setText("Nu ai mutat conform regulilor! Te rog sa refaci ultima mutare!")
            buttons[1] = " "
            QApplication.processEvents()
            ok = 0
        # 2,0 semnifica incercarea de inceput de la o groapa fara puncte
        if result[0] == 2 and result[1] == 0:
            self.text_label.setStyleSheet("font: bold; font-size:16px; color:red")
            self.text_label.setText("Groapa nu are niciun punct! Te rog sa refaci ultima mutare!")
            buttons[0] = " "
            buttons[1] = " "
            ok = 0
            QApplication.processEvents()
        # daca utilizatorul a mutat corect, ok a ramas 1
        if ok == 1:
            button2 = buttons[1]
        # rezultatul cu 1 pe prima pozitie semnifica mutari corecte
        # 1,0 semnifica faptul ca randul playerului curent s-a terminar, asa ca se va actualiza playerul
        # si se va afisa acest lucru in text_label
        if result[0] == 1 and result[1] == 0:
            if player == 1:
                player = 0
                nume = "A"
            else:
                player = 1
                nume = "B"
            self.text_label.setStyleSheet("font: bold; font-size:16px; color:black")
            self.text_label.setText("Este randul lui " + nume)
            # se va actualiza si in partea de joc playerul
            game.set_player(player)
            QApplication.processEvents()
            # daca utilizatorul joaca cu calculatorul, se actualizeaza intai punctele ultimului buton
            # apasat, iar mai apoi se apeleaza functia pentru mutarea calculatorului
            if opponent == "calculator" and nume == "B":
                if game.get_points(buttons[1]) <= 6 or (buttons[1] == "A" or buttons[1] == "B"):
                    self.convert_str_to_button(buttons[1]).setText(
                        self.convert_points_to_text(game.get_points(buttons[1])))
                else:
                    self.convert_str_to_button(buttons[1]).setText(str(game.get_points(buttons[1])))
                QApplication.processEvents()
                game.move_calculator()
                # se face update la textul butoanelor "apasate" de calculator
                self.update_buttons_calc()
            buttons[0] = " "
            buttons[1] = " "
        # 1,1 semnifica exceptia 1- ultima piatra a ajuns in groapa playerului curent
        # se actualizeaza textul afisat in functie de oponent, iar daca oponentul e calculatorul
        # se apeleaza functia pentru mutarea lui si se actualizeaza punctele
        if result[0] == 1 and result[1] == 1:
            self.text_label.setStyleSheet("font: bold; font-size:16px; color:black")
            if opponent == "calculator" and player == 1:
                self.text_label.setText("Ultima piatra a ajuns in banca calculatorului, va muta din nou!")
                buttons[0] = " "
                if game.get_points(buttons[1]) <= 6 or (buttons[1] == "A" or buttons[1] == "B"):
                    self.convert_str_to_button(buttons[1]).setText(
                        self.convert_points_to_text(game.get_points(buttons[1])))
                else:
                    self.convert_str_to_button(buttons[1]).setText(str(game.get_points(buttons[1])))
                buttons[1] = " "
                QApplication.processEvents()
                game.move_calculator()
                self.update_buttons_calc()
            else:
                self.text_label.setText("Ultima piatra a ajuns in banca ta, poti muta din nou!")
                buttons[0] = " "
                buttons[1] = " "
        QApplication.processEvents()
        # 1,2 semnifica exceptia 2
        # se schimba playerul curent in ambele fisiere si se actualizeaza punctele conform dictionarului
        # de puncte din game.py
        if result[0] == 1 and result[1] == 2:
            self.text_label.setStyleSheet("font: bold; font-size:16px; color:black")
            if player == 1:
                player = 0
                nume = "A"
                points_b = game.get_points("B")
                self.BButton.setText(self.convert_points_to_text(points_b))
            else:
                player = 1
                nume = "B"
                points_a = game.get_points("A")
                self.AButton.setText(self.convert_points_to_text(points_a))
            if opponent == "calculator" and nume == "A":
                self.text_label.setText(
                    "Calculatorul aduna toate pietrele din groapa opusa+ultima piatra. Urmeaza randul tau!")
                time.sleep(1)
                buttons[0] = " "
                buttons[1] = " "
                # butonul opus ultimului buton apasat are 0 puncte
                ex2b = game.get_exc2_buttons()
                self.convert_str_to_button(ex2b[1]).setText("0")
                game.set_player(player)
                QApplication.processEvents()
            else:
                self.text_label.setText(
                    "Aduni toate pietrele din groapa opusa+ultima piatra. Urmeaza randul lui " + nume)
                time.sleep(1)
                buttons[0] = " "
                if game.get_points(buttons[1]) <= 6 or (buttons[1] == "A" or buttons[1] == "B"):
                    self.convert_str_to_button(buttons[1]).setText(
                        self.convert_points_to_text(game.get_points(buttons[1])))
                else:
                    self.convert_str_to_button(buttons[1]).setText(str(game.get_points(buttons[1])))
                buttons[1] = " "
                ex2b = game.get_exc2_buttons()
                self.convert_str_to_button(ex2b[1]).setText("0")
                game.set_player(player)
                QApplication.processEvents()
                # daca oponentul este calculatorul, se apeleaza functia game.move_calculator() pentru
                # mutarea acestuia si apoi se actualizeaza punctele din butoanele "apasate" de el
                if opponent == "calculator" and nume == "B":
                    game.move_calculator()
                    self.update_buttons_calc()
        # 1,3 semnifica o mutare corecta fara exceptii si in curs de derulare
        # se actualizeaza numarul de pietre care mai trebuie plasate in gropi/banca si se afiseaza
        if result[0] == 1 and result[1] == 3:
            self.text_label.setStyleSheet("font: bold; font-size:16px; color:black")
            value = game.get_value()
            if value != 1:
                self.text_label.setText("Mai ai in mana " + str(value) + " pietre!")
            else:
                self.text_label.setText("Mai ai in mana o piatra!")
            buttons[0] = buttons[1]
            buttons[1] = " "
        # jocul s-a terminat, deci se vor bloca butoanele, se vor updata punctele din banci, gropile
        # vor avea toate 0 puncte si se va afisa castigatorul
        if result[0] == 3:
            game_over = 1
            if result[1] != 2:
                if result[1] == 0:
                    nume = "A"
                else:
                    nume = "B"
                self.text_label.setStyleSheet("font: bold; font-size:20px; color:green")
                self.text_label.setText("Jocul s-a terminat! Castigatorul este " + nume + "!")
            else:
                self.text_label.setStyleSheet("font: bold; font-size:20px; color:green")
                self.text_label.setText("Jocul s-a terminat! Este remiza!")
            self.block_buttons()
            a = game.get_points("A")
            b = game.get_points("B")
            print(a, b, "puncte")
            self.AButton.setText(str(a))
            self.BButton.setText(str(b))
            self.set_zero()
            QApplication.processEvents()
            return -2
        # daca mutarea a fost corecta se vor returna punctele butonului apasat
        if ok == 1:
            return game.get_points(button2)
        else:
            # altfel, -1
            return -1

    def set_text_label_err(self, text):
        """
            seteaza textul din labelul informativ cand e vorba de o eroare
        """
        self.text_label.setStyleSheet("font: bold; font-size:16px; color:red")
        self.text_label.setText(text)
        buttons[0] = " "

    def update_buttons_calc(self):
        """
            face update la punctele de pe butoanele "apasate" de calculator
        """
        global buttons, player, start, game_over
        time.sleep(1)
        # obtine butoanele, iar pentru fiecare buton seteaza textul corespunzator punctelor
        # cu o mica pauza intre mutari
        buttons_to_update = game.get_buttons_clicked_by_calc()
        for button in buttons_to_update:
            time.sleep(1)
            QApplication.processEvents()
            if game.get_points(button) <= 6 or (button == "A" or button == "B"):
                self.convert_str_to_button(button).setText(self.convert_points_to_text(game.get_points(button)))
            else:
                self.convert_str_to_button(button).setText(str(game.get_points(button)))
        time.sleep(1)
        buttons = game.get_buttons_calculator()
        # se apeleaza functia de play pentru a se continua jocul
        self.play()

    # urmatoarele functii sunt foarte asemanatoare, se apeleaza in cazul apasarii
    # butoanelor de pe tabla de joc

    def a1(self):
        """
            functie apelata in cazul apasarii butonului A1,
            actualizeaza variabila "buttons" care tine evidenta mutarilor
            si mai apoi actualizeaza si punctele de pe buton
        """
        # daca e randul calculatorului nu se intampla nimic
        if opponent == "calculator" and ("B" in self.text_label.text() or "calculatorului" in self.text_label.text()):
            return
        global buttons
        # daca e primul buton apasat se verifica daca este un inceput de mutare si daca este corect
        if buttons[0] == " ":
            buttons[0] = "A1"
            self.text_label.setText(" ")
            if game.ver_start("A1", player):
                self.A1Button.setText("0")
            else:
                if game.check_player(player) == 1 or game.check_player_start(player, "A1") == 0:
                    self.set_text_label_err("Ai inceput de pe o groapa care nu este a ta!")
                elif game.get_points("A1") == 0:
                    self.set_text_label_err("Groapa nu are niciun punct! Incepe din nou!")
        # daca este al 2-lea buton apasat se actualizeaza variabila buttons, se apeleaza functia play
        # pentru a updata punctajul si pentru a afla punctele corespunzatoare butonului A1 si se
        # actualizeaza punctele de pe buton
        elif buttons[1] == " ":
            buttons[1] = "A1"
        if buttons[0] != " " and buttons[1] != " ":
            points = self.play()
            # daca sunt pana in 6 puncte in textul de pe buton vor aparea si bulinele, altfel nu, din
            # motive vizuale
            if points == -2:
                pass
            if points >= 0 and points <= 6:
                self.A1Button.setText(self.convert_points_to_text(points))
            elif points >= 7:
                self.A1Button.setText(str(points))

    def a2(self):
        """
            functie apelata in cazul apasarii butonului A2
        """
        if opponent == "calculator" and ("B" in self.text_label.text() or "calculatorului" in self.text_label.text()):
            return
        global buttons
        if buttons[0] == " ":
            buttons[0] = "A2"
            self.text_label.setText(" ")
            if game.ver_start("A2", player):
                self.A2Button.setText("0")
            else:
                if game.check_player(player) == 1 or game.check_player_start(player, "A2") == 0:
                    self.set_text_label_err("Ai inceput de pe o groapa care nu este a ta!")
                elif game.get_points("A2") == 0:
                    self.set_text_label_err("Groapa nu are niciun punct! Incepe din nou!")
        elif buttons[1] == " ":
            buttons[1] = "A2"
        if buttons[0] != " " and buttons[1] != " ":
            points = self.play()
            if points == -2:
                pass
            if points >= 0 and points <= 6:
                self.A2Button.setText(self.convert_points_to_text(points))
            elif points >= 7:
                self.A2Button.setText(str(points))

    def a3(self):
        """
            functie apelata in cazul apasarii butonului A3
         """
        if opponent == "calculator" and ("B" in self.text_label.text() or "calculatorului" in self.text_label.text()):
            return
        global buttons
        if buttons[0] == " ":
            buttons[0] = "A3"
            self.text_label.setText(" ")
            if game.ver_start("A3", player):
                self.A3Button.setText("0")
            else:
                if game.check_player(player) == 1 or game.check_player_start(player, "A3") == 0:
                    self.set_text_label_err("Ai inceput de pe o groapa care nu este a ta!")
                elif game.get_points("A3") == 0:
                    self.set_text_label_err("Groapa nu are niciun punct! Incepe din nou!")
        elif buttons[1] == " ":
            buttons[1] = "A3"
        if buttons[0] != " " and buttons[1] != " ":
            points = self.play()
            if points == -2:
                pass
            if points >= 0 and points <= 6:
                self.A3Button.setText(self.convert_points_to_text(points))
            elif points >= 7:
                self.A3Button.setText(str(points))

    def a4(self):
        """
            functie apelata in cazul apasarii butonului A4
        """
        if opponent == "calculator" and ("B" in self.text_label.text() or "calculatorului" in self.text_label.text()):
            return
        global buttons
        if buttons[0] == " ":
            buttons[0] = "A4"
            self.text_label.setText(" ")
            self.text_label.setText(" ")
            if game.ver_start("A4", player):
                self.A4Button.setText("0")
            else:
                if game.check_player(player) == 1 or game.check_player_start(player, "A4") == 0:
                    self.set_text_label_err("Ai inceput de pe o groapa care nu este a ta!")
                elif game.get_points("A4") == 0:
                    self.set_text_label_err("Groapa nu are niciun punct! Incepe din nou!")
        elif buttons[1] == " ":
            buttons[1] = "A4"
        if buttons[0] != " " and buttons[1] != " ":
            points = self.play()
            if points == -2:
                pass
            if points >= 0 and points <= 6:
                self.A4Button.setText(self.convert_points_to_text(points))
            elif points >= 7:
                self.A4Button.setText(str(points))

    def a5(self):
        """
            functie apelata in cazul apasarii butonului A5
        """
        if opponent == "calculator" and ("B" in self.text_label.text() or "calculatorului" in self.text_label.text()):
            return
        global buttons
        if buttons[0] == " ":
            buttons[0] = "A5"
            self.text_label.setText(" ")
            if game.ver_start("A5", player):
                self.A5Button.setText("0")
            else:
                if game.check_player(player) == 1 or game.check_player_start(player, "A5") == 0:
                    self.set_text_label_err("Ai inceput de pe o groapa care nu este a ta!")
                elif game.get_points("A5") == 0:
                    self.set_text_label_err("Groapa nu are niciun punct! Incepe din nou!")
        elif buttons[1] == " ":
            buttons[1] = "A5"
        if buttons[0] != " " and buttons[1] != " ":
            points = self.play()
            if points == -2:
                pass
            if points >= 0 and points <= 6:
                self.A5Button.setText(self.convert_points_to_text(points))
            elif points >= 7:
                self.A5Button.setText(str(points))

    def a6(self):
        """
            functie apelata in cazul apasarii butonului A6
        """
        if opponent == "calculator" and ("B" in self.text_label.text() or "calculatorului" in self.text_label.text()):
            return
        global buttons
        if buttons[0] == " ":
            buttons[0] = "A6"
            self.text_label.setText(" ")
            if game.ver_start("A6", player):
                self.A6Button.setText("0")
            else:
                if game.check_player(player) == 1 or game.check_player_start(player, "A6") == 0:
                    self.set_text_label_err("Ai inceput de pe o groapa care nu este a ta!")
                elif game.get_points("A6") == 0:
                    self.set_text_label_err("Groapa nu are niciun punct! Incepe din nou!")
        elif buttons[1] == " ":
            buttons[1] = "A6"
        if buttons[0] != " " and buttons[1] != " ":
            points = self.play()
            if points == -2:
                pass
            if points >= 0 and points <= 6:
                self.A6Button.setText(self.convert_points_to_text(points))
            elif points >= 7:
                self.A6Button.setText(str(points))

    def a(self):
        """
            functie apelata in cazul apasarii butonului A
        """
        if opponent == "calculator" and ("B" in self.text_label.text() or "calculatorului" in self.text_label.text()):
            return
        global buttons
        if buttons[0] == " ":
            self.text_label.setStyleSheet("font: bold; font-size:16px; color:red")
            self.text_label.setText("Nu poti incepe cu bancile!")
        elif buttons[1] == " ":
            buttons[1] = "A"
        if buttons[0] != " " and buttons[1] != " ":
            points = self.play()
            if points == -2:
                pass
            if points >= 0 and points <= 9:
                self.AButton.setText(self.convert_points_to_text(points))
            elif points >= 10:
                self.AButton.setText(str(points))

    def b(self):
        """
            functie apelata in cazul apasarii butonului B
        """
        if opponent == "calculator" and ("B" in self.text_label.text() or "calculatorului" in self.text_label.text()):
            return
        global buttons
        if buttons[0] == " ":
            self.text_label.setStyleSheet("font: bold; font-size:16px; color:red")
            self.text_label.setText("Nu poti incepe cu bancile!")
        elif buttons[1] == " ":
            buttons[1] = "B"
        if buttons[0] != " " and buttons[1] != " ":
            points = self.play()
            if points == -2:
                pass
            if points >= 0 and points <= 9:
                self.BButton.setText(self.convert_points_to_text(points))
            elif points >= 10:
                self.BButton.setText(str(points))

    def b1(self):
        """
            functie apelata in cazul apasarii butonului B1
        """
        if opponent == "calculator" and ("B" in self.text_label.text() or "calculatorului" in self.text_label.text()):
            return
        global buttons
        if buttons[0] == " ":
            buttons[0] = "B1"
            self.text_label.setText(" ")
            if game.ver_start("B1", player):
                self.B1Button.setText("0")
            else:
                if game.check_player(player) == 1 or game.check_player_start(player, "B1") == 0:
                    self.set_text_label_err("Ai inceput de pe o groapa care nu este a ta!")
                elif game.get_points("B1") == 0:
                    self.set_text_label_err("Groapa nu are niciun punct! Incepe din nou!")
        elif buttons[1] == " ":
            buttons[1] = "B1"
        if buttons[0] != " " and buttons[1] != " ":
            points = self.play()
            if points == -2:
                pass
            if points >= 0 and points <= 6:
                self.B1Button.setText(self.convert_points_to_text(points))
            elif points >= 7:
                self.B1Button.setText(str(points))

    def b2(self):
        """
            functie apelata in cazul apasarii butonului B2
        """
        if opponent == "calculator" and ("B" in self.text_label.text() or "calculatorului" in self.text_label.text()):
            return
        global buttons
        if buttons[0] == " ":
            buttons[0] = "B2"
            self.text_label.setText(" ")
            if game.ver_start("B2", player):
                self.B2Button.setText("0")
            else:
                if game.check_player(player) == 1 or game.check_player_start(player, "B2") == 0:
                    self.set_text_label_err("Ai inceput de pe o groapa care nu este a ta!")
                elif game.get_points("B2") == 0:
                    self.set_text_label_err("Groapa nu are niciun punct! Incepe din nou!")
        elif buttons[1] == " ":
            buttons[1] = "B2"
        if buttons[0] != " " and buttons[1] != " ":
            points = self.play()
            if points == -2:
                pass
            if points >= 0 and points <= 6:
                self.B2Button.setText(self.convert_points_to_text(points))
            elif points >= 7:
                self.B2Button.setText(str(points))

    def b3(self):
        """
            functie apelata in cazul apasarii butonului B3
        """
        if opponent == "calculator" and ("B" in self.text_label.text() or "calculatorului" in self.text_label.text()):
            return
        global buttons
        if buttons[0] == " ":
            buttons[0] = "B3"
            self.text_label.setText(" ")
            if game.ver_start("B3", player):
                self.B3Button.setText("0")
            else:
                if game.check_player(player) == 1 or game.check_player_start(player, "B3") == 0:
                    self.set_text_label_err("Ai inceput de pe o groapa care nu este a ta!")
                elif game.get_points("B3") == 0:
                    self.set_text_label_err("Groapa nu are niciun punct! Incepe din nou!")
        elif buttons[1] == " ":
            buttons[1] = "B3"
        if buttons[0] != " " and buttons[1] != " ":
            points = self.play()
            if points == -2:
                pass
            if points >= 0 and points <= 6:
                self.B3Button.setText(self.convert_points_to_text(points))
            elif points >= 7:
                self.B3Button.setText(str(points))

    def b4(self):
        """
            functie apelata in cazul apasarii butonului B4
        """
        if opponent == "calculator" and ("B" in self.text_label.text() or "calculatorului" in self.text_label.text()):
            return
        global buttons
        if buttons[0] == " ":
            buttons[0] = "B4"
            self.text_label.setText(" ")
            if game.ver_start("B4", player):
                self.B4Button.setText("0")
            else:
                if game.check_player(player) == 1 or game.check_player_start(player, "B4") == 0:
                    self.set_text_label_err("Ai inceput de pe o groapa care nu este a ta!")
                elif game.get_points("B4") == 0:
                    self.set_text_label_err("Groapa nu are niciun punct! Incepe din nou!")
        elif buttons[1] == " ":
            buttons[1] = "B4"
        if buttons[0] != " " and buttons[1] != " ":
            points = self.play()
            if points == -2:
                pass
            if points >= 0 and points <= 6:
                self.B4Button.setText(self.convert_points_to_text(points))
            elif points >= 7:
                self.B4Button.setText(str(points))

    def b5(self):
        """
            functie apelata in cazul apasarii butonului B5
        """
        if opponent == "calculator" and ("B" in self.text_label.text() or "calculatorului" in self.text_label.text()):
            return
        global buttons
        if buttons[0] == " ":
            buttons[0] = "B5"
            self.text_label.setText(" ")
            if game.ver_start("B5", player):
                self.B5Button.setText("0")
            else:
                if game.check_player(player) == 1 or game.check_player_start(player, "B5") == 0:
                    self.set_text_label_err("Ai inceput de pe o groapa care nu este a ta!")
                elif game.get_points("B5") == 0:
                    self.set_text_label_err("Groapa nu are niciun punct! Incepe din nou!")
        elif buttons[1] == " ":
            buttons[1] = "B5"
        if buttons[0] != " " and buttons[1] != " ":
            points = self.play()
            if points == -2:
                pass
            if points >= 0 and points <= 6:
                self.B5Button.setText(self.convert_points_to_text(points))
            elif points >= 7:
                self.B5Button.setText(str(points))

    def b6(self):
        """
            functie apelata in cazul apasarii butonului B6
        """
        if opponent == "calculator" and ("B" in self.text_label.text() or "calculatorului" in self.text_label.text()):
            return
        global buttons
        if buttons[0] == " ":
            buttons[0] = "B6"
            self.text_label.setText(" ")
            if game.ver_start("B6", player):
                self.B6Button.setText("0")
            else:
                if game.check_player(player) == 1 or game.check_player_start(player, "B6") == 0:
                    self.set_text_label_err("Ai inceput de pe o groapa care nu este a ta!")
                elif game.get_points("B6") == 0:
                    self.set_text_label_err("Groapa nu are niciun punct! Incepe din nou!")
        elif buttons[1] == " ":
            buttons[1] = "B6"
        if buttons[0] != " " and buttons[1] != " ":
            points = self.play()
            if points == -2:
                pass
            if points >= 0 and points <= 6:
                self.B6Button.setText(self.convert_points_to_text(points))
            elif points >= 7:
                self.B6Button.setText(str(points))


class MyWindow(QtWidgets.QMainWindow):
    def closeEvent(self, event):
        """
            functie pentru confirmarea iesirii: daca utilizatorul apasa pe "x", va avea optiunea sa
            iasa din joc sau sa ramana in el
        """
        result = QtWidgets.QMessageBox.question(self,
                                                "Confirma iesirea",
                                                "Sigur doresti sa iesi din joc ?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if result == QtWidgets.QMessageBox.Yes:
            event.accept()
            self.close()
        elif result == QtWidgets.QMessageBox.No:
            event.ignore()


def exception_hook(exctype, value, traceback):
    """
        functie pentru a vedea de unde vin erorile
    """
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError('Trebuie sa alegi tipul de oponent!')
    opponent = sys.argv[1]
    game.set_opponent(opponent)
    app = QtWidgets.QApplication(sys.argv)
    Mancala = MyWindow()
    ui = MancalaGui()
    ui.setup_game_ui(Mancala)
    sys._excepthook = sys.excepthook
    sys.excepthook = exception_hook
    sys.exit(app.exec_())
