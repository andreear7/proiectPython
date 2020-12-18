from PyQt5 import QtCore, QtGui, QtWidgets
import sys
# import os

# de facut:
# adaugat paramentru oponent si apelat set_oponent
# functii pt fiecare buton ( daca am buttons complet apelez update_points cu ele si playerul)
# label pentru anuntat cine muta ( si de ce in cazul exceptiilor) daca value=0 / pt anuntat castigatorul
# (/ pt mutare gresita)
# functie pt apelat move_calculator cand oponent=calculator si e randul lui
# implementat efectiv mutarea pietrelor

oponent = "calculator"
buttons = [" "," "]
player=0

class MancalaGui(object):

    def setup_ui(self, mancala):
        mancala.setObjectName("Mancala")
        mancala.setWindowTitle("Mancala")
        mancala.resize(860, 500)
        self.centralwidget = QtWidgets.QWidget(mancala)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("border-image : url(m1.jpg) 0 0 0 0 stretch stretch;")

        # The button for start
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(250, 100, 350, 150))
        # self.pushButton.setObjectName("Start")
        self.startButton.setText("Incepe jocul")
        self.startButton.setStyleSheet(
            "font: bold;font-size:20px; background-color:rgba(255, 255, 255, 0.45); border-image:none")
        self.startButton.clicked.connect(self.start)

        # The button for rules
        self.rulesButton = QtWidgets.QPushButton(self.centralwidget)
        self.rulesButton.setGeometry(QtCore.QRect(250, 270, 350, 150))
        # self.pushButton2.setObjectName("Rules")
        self.rulesButton.setText("Regulament")
        self.rulesButton.setStyleSheet(
            "font: bold; font-size:20px;background-color:rgba(255, 255, 255, 0.45); border-image:none")
        self.rulesButton.clicked.connect(self.rules)

        mancala.setCentralWidget(self.centralwidget)

        # self.retranslateUi(Mancala)
        QtCore.QMetaObject.connectSlotsByName(mancala)
        mancala.show()

        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(20, 20, 45, 30))
        self.backButton.setStyleSheet(" border-image:url(back.png) 0 0 0 0")
        self.backButton.clicked.connect(self.back)
        self.backButton.setVisible(False)

        self.reg_label = QtWidgets.QLabel(self.centralwidget)
        self.reg_label.setStyleSheet(
            "font: bold; font-size:14px;background-color:rgba(255, 255, 255, 0.45); border-image:none")
        self.reg_label.setGeometry(QtCore.QRect(100, 50, 650, 400))
        self.reg_label.setAlignment(QtCore.Qt.AlignCenter)

        self.board_label = QtWidgets.QLabel(self.centralwidget)
        self.board_label.setStyleSheet("border-radius:50px;font: bold; font-size:14px; border-image: url(wm.jpg)")
        self.board_label.setGeometry(QtCore.QRect(65, 110, 743, 280))
        self.board_label.setAlignment(QtCore.Qt.AlignCenter)

        self.A1Button = QtWidgets.QPushButton(self.centralwidget)
        self.A1Button.setGeometry(185, 140, 80, 80)
        self.A1Button.setStyleSheet(
            "background-image:url(wm1.jpg);border-radius : 40; background-color:rgb(222,184,135)")
        self.A1Button.clicked.connect(self.A1)
        self.A1Button.setVisible(False)

        self.A2Button = QtWidgets.QPushButton(self.centralwidget)
        self.A2Button.setGeometry(270, 140, 80, 80)
        self.A2Button.setStyleSheet(
            "background-image:url(wm1.jpg);border-radius : 40; background-color:rgb(222,184,135)")
        self.A2Button.clicked.connect(self.A2)
        self.A2Button.setVisible(False)

        self.A3Button = QtWidgets.QPushButton(self.centralwidget)
        self.A3Button.setGeometry(355, 140, 80, 80)
        self.A3Button.setStyleSheet(
            "background-image:url(wm1.jpg);border-radius : 40; background-color:rgb(222,184,135)")
        self.A3Button.clicked.connect(self.A2)
        self.A3Button.setVisible(False)

        self.A4Button = QtWidgets.QPushButton(self.centralwidget)
        self.A4Button.setGeometry(440, 140, 80, 80)
        self.A4Button.setStyleSheet(
            "background-image:url(wm1.jpg);border-radius : 40; background-color:rgb(222,184,135)")
        self.A4Button.clicked.connect(self.A2)
        self.A4Button.setVisible(False)

        self.A5Button = QtWidgets.QPushButton(self.centralwidget)
        self.A5Button.setGeometry(525, 140, 80, 80)
        self.A5Button.setStyleSheet(
            "background-image:url(wm1.jpg);border-radius : 40; background-color:rgb(222,184,135)")
        self.A5Button.clicked.connect(self.A2)
        self.A5Button.setVisible(False)

        self.A6Button = QtWidgets.QPushButton(self.centralwidget)
        self.A6Button.setGeometry(610, 140, 80, 80)
        self.A6Button.setStyleSheet(
            "background-image:url(wm1.jpg);border-radius : 40; background-color:rgb(222,184,135)")
        self.A6Button.clicked.connect(self.A2)
        self.A6Button.setVisible(False)

        self.AButton = QtWidgets.QPushButton(self.centralwidget)
        self.AButton.setGeometry(80, 140, 100, 220)
        self.AButton.setStyleSheet(
            "background-image:url(wm1.jpg);border-radius : 40; background-color:rgb(222,184,135)")
        self.AButton.clicked.connect(self.A2)
        self.AButton.setVisible(False)

        self.BButton = QtWidgets.QPushButton(self.centralwidget)
        self.BButton.setGeometry(693, 140, 100, 220)
        self.BButton.setStyleSheet(
            "background-image:url(wm1.jpg);border-radius : 40; background-color:rgb(222,184,135)")
        self.BButton.clicked.connect(self.A2)
        self.BButton.setVisible(False)

        self.B1Button = QtWidgets.QPushButton(self.centralwidget)
        self.B1Button.setGeometry(185, 280, 80, 80)
        self.B1Button.setStyleSheet(
            "background-image:url(wm1.jpg);border-radius : 40; background-color:rgb(222,184,135)")
        self.B1Button.clicked.connect(self.A1)
        self.B1Button.setVisible(False)

        self.B2Button = QtWidgets.QPushButton(self.centralwidget)
        self.B2Button.setGeometry(270, 280, 80, 80)
        self.B2Button.setStyleSheet(
            "background-image:url(wm1.jpg);border-radius : 40; background-color:rgb(222,184,135)")
        self.B2Button.clicked.connect(self.A2)
        self.B2Button.setVisible(False)

        self.B3Button = QtWidgets.QPushButton(self.centralwidget)
        self.B3Button.setGeometry(355, 280, 80, 80)
        self.B3Button.setStyleSheet(
            "background-image:url(wm1.jpg);border-radius : 40; background-color:rgb(222,184,135)")
        self.B3Button.clicked.connect(self.A2)
        self.B3Button.setVisible(False)

        self.B4Button = QtWidgets.QPushButton(self.centralwidget)
        self.B4Button.setGeometry(440, 280, 80, 80)
        self.B4Button.setStyleSheet(
            "background-image:url(wm1.jpg);border-radius : 40; background-color:rgb(222,184,135)")
        self.B4Button.clicked.connect(self.A2)
        self.B4Button.setVisible(False)

        self.B5Button = QtWidgets.QPushButton(self.centralwidget)
        self.B5Button.setGeometry(525, 280, 80, 80)
        self.B5Button.setStyleSheet(
            "background-image:url(wm1.jpg);border-radius : 40; background-color:rgb(222,184,135)")
        self.B5Button.clicked.connect(self.A2)
        self.B5Button.setVisible(False)

        self.B6Button = QtWidgets.QPushButton(self.centralwidget)
        self.B6Button.setGeometry(610, 280, 80, 80)
        self.B6Button.setStyleSheet(
            "background-image:url(wm1.jpg);border-radius : 40; background-color:rgb(222,184,135)")
        self.B6Button.clicked.connect(self.A2)
        self.B6Button.setVisible(False)

        self.A11label = QtWidgets.QLabel(self.centralwidget)
        self.A11label.setGeometry(200, 155, 20, 20)
        self.A11label.setStyleSheet(
            "border-radius : 10; background-color:rgb(72, 201, 176)")
        self.A11label.setVisible(False)

        self.A12label = QtWidgets.QLabel(self.centralwidget)
        self.A12label.setGeometry(230, 155, 20, 20)
        self.A12label.setStyleSheet(
            "border-radius : 10; background-color:rgb(165, 105, 189 )")
        self.A12label.setVisible(False)

        self.A13label = QtWidgets.QLabel(self.centralwidget)
        self.A13label.setGeometry(230, 180, 20, 20)
        self.A13label.setStyleSheet(
            "border-radius : 10; background-color:rgb(231, 76, 60 )")
        self.A13label.setVisible(False)

        self.A14label = QtWidgets.QLabel(self.centralwidget)
        self.A14label.setGeometry(200, 180, 20, 20)
        self.A14label.setStyleSheet(
            "border-radius : 10; background-color:rgb(247, 220, 111 )")
        self.A14label.setVisible(False)

        self.A21label = QtWidgets.QLabel(self.centralwidget)
        self.A21label.setGeometry(285, 155, 20, 20)
        self.A21label.setStyleSheet(
            "border-radius : 10; background-color:rgb(153, 153, 255)")
        self.A21label.setVisible(False)

        self.A22label = QtWidgets.QLabel(self.centralwidget)
        self.A22label.setGeometry(315, 155, 20, 20)
        self.A22label.setStyleSheet(
            "border-radius : 10; background-color:rgb(51, 102, 153)")
        self.A22label.setVisible(False)

        self.A23label = QtWidgets.QLabel(self.centralwidget)
        self.A23label.setGeometry(315, 180, 20, 20)
        self.A23label.setStyleSheet(
            "border-radius : 10; background-color:rgb(204, 0, 153)")
        self.A23label.setVisible(False)

        self.A24label = QtWidgets.QLabel(self.centralwidget)
        self.A24label.setGeometry(285, 180, 20, 20)
        self.A24label.setStyleSheet(
            "border-radius : 10; background-color:rgb(102, 102, 153)")
        self.A24label.setVisible(False)

        self.A31label = QtWidgets.QLabel(self.centralwidget)
        self.A31label.setGeometry(370, 155, 20, 20)
        self.A31label.setStyleSheet(
            "border-radius : 10; background-color:rgb(153, 255, 255)")
        self.A31label.setVisible(False)

        self.A32label = QtWidgets.QLabel(self.centralwidget)
        self.A32label.setGeometry(400, 155, 20, 20)
        self.A32label.setStyleSheet(
            "border-radius : 10; background-color:rgb(0, 0, 255)")
        self.A32label.setVisible(False)

        self.A33label = QtWidgets.QLabel(self.centralwidget)
        self.A33label.setGeometry(400, 180, 20, 20)
        self.A33label.setStyleSheet(
            "border-radius : 10; background-color:rgb(255, 51, 153)")
        self.A33label.setVisible(False)

        self.A34label = QtWidgets.QLabel(self.centralwidget)
        self.A34label.setGeometry(370, 180, 20, 20)
        self.A34label.setStyleSheet(
            "border-radius : 10; background-color:rgb(204, 204, 255)")
        self.A34label.setVisible(False)

        self.A41label = QtWidgets.QLabel(self.centralwidget)
        self.A41label.setGeometry(455, 155, 20, 20)
        self.A41label.setStyleSheet(
            "border-radius : 10; background-color:rgb(255, 102, 204)")
        self.A41label.setVisible(False)

        self.A42label = QtWidgets.QLabel(self.centralwidget)
        self.A42label.setGeometry(485, 155, 20, 20)
        self.A42label.setStyleSheet(
            "border-radius : 10; background-color:rgb(0, 255, 204)")
        self.A42label.setVisible(False)

        self.A43label = QtWidgets.QLabel(self.centralwidget)
        self.A43label.setGeometry(485, 180, 20, 20)
        self.A43label.setStyleSheet(
            "border-radius : 10; background-color:rgb(0, 102, 0)")
        self.A43label.setVisible(False)

        self.A44label = QtWidgets.QLabel(self.centralwidget)
        self.A44label.setGeometry(455, 180, 20, 20)
        self.A44label.setStyleSheet(
            "border-radius : 10; background-color:rgb(255, 102, 0)")
        self.A44label.setVisible(False)

        self.A51label = QtWidgets.QLabel(self.centralwidget)
        self.A51label.setGeometry(540, 155, 20, 20)
        self.A51label.setStyleSheet(
            "border-radius : 10; background-color:rgb(255, 153, 255)")
        self.A51label.setVisible(False)

        self.A52label = QtWidgets.QLabel(self.centralwidget)
        self.A52label.setGeometry(570, 155, 20, 20)
        self.A52label.setStyleSheet(
            "border-radius : 10; background-color:rgb(255, 255, 255)")
        self.A52label.setVisible(False)

        self.A53label = QtWidgets.QLabel(self.centralwidget)
        self.A53label.setGeometry(570, 180, 20, 20)
        self.A53label.setStyleSheet(
            "border-radius : 10; background-color:rgb(204, 0, 102)")
        self.A53label.setVisible(False)

        self.A54label = QtWidgets.QLabel(self.centralwidget)
        self.A54label.setGeometry(540, 180, 20, 20)
        self.A54label.setStyleSheet(
            "border-radius : 10; background-color:rgb(255, 223, 128)")
        self.A54label.setVisible(False)

        self.A61label = QtWidgets.QLabel(self.centralwidget)
        self.A61label.setGeometry(625, 155, 20, 20)
        self.A61label.setStyleSheet(
            "border-radius : 10; background-color:rgb(57, 230, 0)")
        self.A61label.setVisible(False)

        self.A62label = QtWidgets.QLabel(self.centralwidget)
        self.A62label.setGeometry(655, 155, 20, 20)
        self.A62label.setStyleSheet(
            "border-radius : 10; background-color:rgb(179, 179, 255)")
        self.A62label.setVisible(False)

        self.A63label = QtWidgets.QLabel(self.centralwidget)
        self.A63label.setGeometry(655, 180, 20, 20)
        self.A63label.setStyleSheet(
            "border-radius : 10; background-color:rgb(64, 128, 191)")
        self.A63label.setVisible(False)

        self.A64label = QtWidgets.QLabel(self.centralwidget)
        self.A64label.setGeometry(625, 180, 20, 20)
        self.A64label.setStyleSheet(
            "border-radius : 10; background-color:rgb(187, 153, 255)")
        self.A64label.setVisible(False)

        self.B11label = QtWidgets.QLabel(self.centralwidget)
        self.B11label.setGeometry(200, 295, 20, 20)
        self.B11label.setStyleSheet(
            "border-radius : 10; background-color:rgb(72, 201, 176)")
        self.B11label.setVisible(False)

        self.B12label = QtWidgets.QLabel(self.centralwidget)
        self.B12label.setGeometry(230, 295, 20, 20)
        self.B12label.setStyleSheet(
            "border-radius : 10; background-color:rgb(165, 105, 189 )")
        self.B12label.setVisible(False)

        self.B13label = QtWidgets.QLabel(self.centralwidget)
        self.B13label.setGeometry(230, 320, 20, 20)
        self.B13label.setStyleSheet(
            "border-radius : 10; background-color:rgb(231, 76, 60 )")
        self.B13label.setVisible(False)

        self.B14label = QtWidgets.QLabel(self.centralwidget)
        self.B14label.setGeometry(200, 320, 20, 20)
        self.B14label.setStyleSheet(
            "border-radius : 10; background-color:rgb(247, 220, 111 )")
        self.B14label.setVisible(False)

        self.B21label = QtWidgets.QLabel(self.centralwidget)
        self.B21label.setGeometry(285, 295, 20, 20)
        self.B21label.setStyleSheet(
            "border-radius : 10; background-color:rgb(153, 153, 255)")
        self.B21label.setVisible(False)

        self.B22label = QtWidgets.QLabel(self.centralwidget)
        self.B22label.setGeometry(315, 295, 20, 20)
        self.B22label.setStyleSheet(
            "border-radius : 10; background-color:rgb(51, 102, 153)")
        self.B22label.setVisible(False)

        self.B23label = QtWidgets.QLabel(self.centralwidget)
        self.B23label.setGeometry(315, 320, 20, 20)
        self.B23label.setStyleSheet(
            "border-radius : 10; background-color:rgb(204, 0, 153)")
        self.B23label.setVisible(False)

        self.B24label = QtWidgets.QLabel(self.centralwidget)
        self.B24label.setGeometry(285, 320, 20, 20)
        self.B24label.setStyleSheet(
            "border-radius : 10; background-color:rgb(102, 102, 153)")
        self.B24label.setVisible(False)

        self.B31label = QtWidgets.QLabel(self.centralwidget)
        self.B31label.setGeometry(370, 295, 20, 20)
        self.B31label.setStyleSheet(
            "border-radius : 10; background-color:rgb(153, 255, 255)")
        self.B31label.setVisible(False)

        self.B32label = QtWidgets.QLabel(self.centralwidget)
        self.B32label.setGeometry(400, 295, 20, 20)
        self.B32label.setStyleSheet(
            "border-radius : 10; background-color:rgb(0, 0, 255)")
        self.B32label.setVisible(False)

        self.B33label = QtWidgets.QLabel(self.centralwidget)
        self.B33label.setGeometry(400, 320, 20, 20)
        self.B33label.setStyleSheet(
            "border-radius : 10; background-color:rgb(255, 51, 153)")
        self.B33label.setVisible(False)

        self.B34label = QtWidgets.QLabel(self.centralwidget)
        self.B34label.setGeometry(370, 320, 20, 20)
        self.B34label.setStyleSheet(
            "border-radius : 10; background-color:rgb(204, 204, 255)")
        self.B34label.setVisible(False)

        self.B41label = QtWidgets.QLabel(self.centralwidget)
        self.B41label.setGeometry(455, 295, 20, 20)
        self.B41label.setStyleSheet(
            "border-radius : 10; background-color:rgb(255, 102, 204)")
        self.B41label.setVisible(False)

        self.B42label = QtWidgets.QLabel(self.centralwidget)
        self.B42label.setGeometry(485, 295, 20, 20)
        self.B42label.setStyleSheet(
            "border-radius : 10; background-color:rgb(0, 255, 204)")
        self.B42label.setVisible(False)

        self.B43label = QtWidgets.QLabel(self.centralwidget)
        self.B43label.setGeometry(485, 320, 20, 20)
        self.B43label.setStyleSheet(
            "border-radius : 10; background-color:rgb(0, 102, 0)")
        self.B43label.setVisible(False)

        self.B44label = QtWidgets.QLabel(self.centralwidget)
        self.B44label.setGeometry(455, 320, 20, 20)
        self.B44label.setStyleSheet(
            "border-radius : 10; background-color:rgb(255, 102, 0)")
        self.B44label.setVisible(False)

        self.B51label = QtWidgets.QLabel(self.centralwidget)
        self.B51label.setGeometry(540, 295, 20, 20)
        self.B51label.setStyleSheet(
            "border-radius : 10; background-color:rgb(255, 153, 255)")
        self.B51label.setVisible(False)

        self.B52label = QtWidgets.QLabel(self.centralwidget)
        self.B52label.setGeometry(570, 295, 20, 20)
        self.B52label.setStyleSheet(
            "Border-radius : 10; background-color:rgb(255, 255, 255)")
        self.B52label.setVisible(False)

        self.B53label = QtWidgets.QLabel(self.centralwidget)
        self.B53label.setGeometry(570, 320, 20, 20)
        self.B53label.setStyleSheet(
            "border-radius : 10; background-color:rgb(204, 0, 102)")
        self.B53label.setVisible(False)

        self.B54label = QtWidgets.QLabel(self.centralwidget)
        self.B54label.setGeometry(540, 320, 20, 20)
        self.B54label.setStyleSheet(
            "border-radius : 10; background-color:rgb(255, 223, 128)")
        self.B54label.setVisible(False)

        self.B61label = QtWidgets.QLabel(self.centralwidget)
        self.B61label.setGeometry(625, 295, 20, 20)
        self.B61label.setStyleSheet(
            "Border-radius : 10; background-color:rgb(57, 230, 0)")
        self.B61label.setVisible(False)

        self.B62label = QtWidgets.QLabel(self.centralwidget)
        self.B62label.setGeometry(655, 295, 20, 20)
        self.B62label.setStyleSheet(
            "Border-radius : 10; background-color:rgb(179, 179, 255)")
        self.B62label.setVisible(False)

        self.B63label = QtWidgets.QLabel(self.centralwidget)
        self.B63label.setGeometry(655, 320, 20, 20)
        self.B63label.setStyleSheet(
            "border-radius : 10; background-color:rgb(64, 128, 191)")
        self.B63label.setVisible(False)

        self.B64label = QtWidgets.QLabel(self.centralwidget)
        self.B64label.setGeometry(625, 320, 20, 20)
        self.B64label.setStyleSheet(
            "border-radius : 10; background-color:rgb(187, 153, 255)")
        self.B64label.setVisible(False)

    def set_board_visible(self, value):
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
        self.A11label.setVisible(value)
        self.A12label.setVisible(value)
        self.A13label.setVisible(value)
        self.A14label.setVisible(value)
        self.A21label.setVisible(value)
        self.A22label.setVisible(value)
        self.A23label.setVisible(value)
        self.A24label.setVisible(value)
        self.A31label.setVisible(value)
        self.A32label.setVisible(value)
        self.A33label.setVisible(value)
        self.A34label.setVisible(value)
        self.A41label.setVisible(value)
        self.A42label.setVisible(value)
        self.A43label.setVisible(value)
        self.A44label.setVisible(value)
        self.A51label.setVisible(value)
        self.A52label.setVisible(value)
        self.A53label.setVisible(value)
        self.A54label.setVisible(value)
        self.A61label.setVisible(value)
        self.A62label.setVisible(value)
        self.A63label.setVisible(value)
        self.A64label.setVisible(value)
        self.B11label.setVisible(value)
        self.B12label.setVisible(value)
        self.B13label.setVisible(value)
        self.B14label.setVisible(value)
        self.B21label.setVisible(value)
        self.B22label.setVisible(value)
        self.B23label.setVisible(value)
        self.B24label.setVisible(value)
        self.B31label.setVisible(value)
        self.B32label.setVisible(value)
        self.B33label.setVisible(value)
        self.B34label.setVisible(value)
        self.B41label.setVisible(value)
        self.B42label.setVisible(value)
        self.B43label.setVisible(value)
        self.B44label.setVisible(value)
        self.B51label.setVisible(value)
        self.B52label.setVisible(value)
        self.B53label.setVisible(value)
        self.B54label.setVisible(value)
        self.B61label.setVisible(value)
        self.B62label.setVisible(value)
        self.B63label.setVisible(value)
        self.B64label.setVisible(value)


    def start(self):
        self.startButton.setVisible(False)
        self.rulesButton.setVisible(False)
        self.backButton.setVisible(True)
        self.centralwidget.setStyleSheet("border-image:none; background-color: rgb(234, 236, 238);")
        self.set_board_visible(True)

    def rules(self):
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
        self.reg_label.setVisible(False)
        self.backButton.setVisible(False)
        self.startButton.setVisible(True)
        self.rulesButton.setVisible(True)
        self.centralwidget.setStyleSheet("border-image : url(m1.jpg) 0 0 0 0 stretch stretch;")
        self.set_board_visible(False)

    def A1(self):
        pass

    def A2(self):
        pass


class MyWindow(QtWidgets.QMainWindow):
    def closeEvent(self, event):
        result = QtWidgets.QMessageBox.question(self,
                                                "Confirma iesirea",
                                                "Sigur doresti sa iesi din joc ?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if result == QtWidgets.QMessageBox.Yes:
            event.accept()
            self.close()
            # os.system("TASKKILL /F /IM table.exe")
        elif result == QtWidgets.QMessageBox.No:
            event.ignore()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Mancala = QtWidgets.QMainWindow()
    Mancala = MyWindow()
    ui = MancalaGui()
    ui.setup_ui(Mancala)
    sys.exit(app.exec_())
