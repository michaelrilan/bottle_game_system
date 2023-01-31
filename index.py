from bottle_game_design import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import (QApplication,QWidget)
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
import sys
import os
class newWindow1(Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super(newWindow1, self).__init__()
        self.setupUi(self)
        self.frame_correct.hide()
        self.frame_4.hide()
        self.frame_choose.hide()
        self.txtedit_question.hide()
        self.btn_cancel.hide()
        self.btn_next_question.hide()
        self.lbl_mode.setText("MODE:")
        
        self.setFixedSize(631, 451)


        self.mlist_easy = [
            ["How many planets in solar system?","nine"],
            ["Who is the 17th President in Philippines?","Ferdinand Bongbong Marcos Jr"],
            ["How many stars in the flag of Philippines?","three"],
            ["What is the virus infect the world wide on 2018?","Covid 19"],
            ["What is the national bird of the Philippines?","Eagle"],
            ["What is the capital of the Philippines?","Manila"],
            ["What is the oldest city in the Philippines?","Cebu City"],
            ["How many country in the world?","195"],
            ["Who is the king of the jungle?","Lion"],
            ["What is the smallest city in Philippines?","San Juan"],
            ["What is a group of crows called?","Murder"],
            ["How many dots appear on a pair of dice?","42"],
            ["Which is the only body part that is fully grown from birth?","Eyeball"],
            ["What is acrophobia a fear of?","Intense fear of heights"],
            ["How many minutes are in a full week?","10,080"],
            ["Sino ang pambansang bayani ng Pilipinas?","Jose Rizal"],
            ["Sino ang ama ng rebolusyon?","Andres Bonifacio"],
            ["Ano ang makikita sa bansang Pilipinas na pinag-aagawan?","langis"],
            ["Sino ang unang taong sumakop sa Pilipinas?","Ferdinand Magellan"],
            ["Lengawahe ng bansang Pilipinas?","Filipino"]
             ]
        self.easy_choices = [
            ["eight","seven","nine"],
            ["Rodrigo Roa Duterte","Ferdinand Bongbong Marcos Jr","Diosdado Macapagal"],
            ["two","four","three"],
            ["Covid 19","Malaria","Dengue"],
            ["Maya","Eagle","Hawk"],
            ["Cebu","Tarlac","Manila"],
            ["Manila","Cebu City","Davao City"],
            ["196","193","195"],
            ["Lion","Tiger","Elephant"],
            ["Sta Cruz","Tondo","San Juan"],
            ["Flock","School","Murder"],
            ["43","41","42"],
            ["Heart","Eyeball","Brain"],
            ["Intense fear of heights","Intense fear of clowns","Intense fear of water"],
            ["10,704","10,465","10,080"],
            ["Andres Bonifacio","Emilio Jacinto","Jose Rizal"],
            ["Andres Bonifacio","Apolinario Mabini","Emilio Aguinaldo"],
            ["ginto","langis","pilak"],
            ["Antonio Pigafetta","Ferdinand Magellan","King Philip II"],
            ["Tagalog","Pilipino","Filipino"]
             ]



        

        self.mlist_average = [
            ["Anong taon binaril ang Pambasang bayani ng Pilipinas?","Disyembre 30, 1896"],
            ["Anong pinaka malaking hayop sa buong mundo?","African Elephant"],
            ["Ano pinakamabilis na hayop sa buong mundo?","Cheetah"],
            ["Ano ang pinaka maliit na hayop sa buong mundo?","Dwarf marmoset"],
            ["Sino ang kilala bilang pilay o 'dakilang lumpo' na bayani?","Apolonario Mabini"],
            ["Nagkaroon ng parangal dahil sa aking galing sa boxing?","Manny Pacquiao"],
            ["Sino ang nagbigay ng unang korona sa miss universe?","Gloria Diaz"],
            ["Sino ang king of rapper ng Pilipinas?","Francis Magallona"],
            ["Kilala bilang bastos na rapper at tinagoriang badsheep?","Andrew E"],
            ["Sino ang magician sa larangan ng bilyaran?","Efren Bata Reyes"],
            ["How many bones are in the human body?","206"],
            ["What is the most good conductor?","Gold"],
            ["What does DNA stand for?","Deoxyribonucleic acid"],
            ["What is the hardest natural substance on Earth?","Diamond"],
            ["Which is the main gas that makes up the Earth's atmosphere?","Nitrogen"],
            ["Which famous British physicist wrote A Brief History of Time?","Stephen Hawking"],
            ["What is Carbon Dioxide?","natural greenhouse gas"],
            ["What is the most good conductor?","Gold"],
            ["Science is made by God?","Yes"],
            ["What is the biggest planet in our solar system?","Jupiter"]
             ]
        self.average_choices=[
            ["Disyembre 30, 1895","Disyembre 30, 1896","Disyembre 30, 1898"],
            ["African Elephant","American Elephant","Philippine Elephant"],
            ["Horse","Rabbit","Cheetah"],
            ["Hummingbird","Ants","Dwarf marmoset"],
            ["Apolonario Mabini","Andres Bonifacio","Emilio Aguinaldo"],
            ["Donny Nietes","Manny Pacquiao","Nonito Donaire"],
            ["Gloria Diaz","Pia Wurtzbach","Samcy Supsup"],
            ["Shanti Dope","Gloc 9","Francis Magallona"],
            ["Flow G","Andrew E","Loonie"],
            ["Eric Buhain","Efren Bata Reyes","Lydia De Vega"],
            ["205","206","207"],
            ["Gold","Silver","Copper"],
            ["Deoxyribonuclic acid","Dioxyribonucleic acid","Deoxyribonucleic acid"],
            ["Titanium","Diamond","Tungsten"],
            ["Carbon Monoxide","Helium","Nitrogen"],
            ["Albert Einstein","Stephen Hawking","Isaac Newton"],
            ["natural greenhouse gas","natural greenhouse solid","natural greenhouse liquid"],
            ["Silver","Copper","Gold"],
            ["Yes","No","Maybe"],
            ["Uranus","Jupiter","Saturn"],
             ]
        



        self.mlist_hard = [
            ["What is the smallest planet in our solar system?","Mercury"],
            ["What was the name of the first man-made satellite launched by the Soviet Union in 1957?","Sputnik"],
            ["What is the study of mushrooms called?","Mycology"],
            ["What is a material that will not carry an electrical charge called?","Insulator"],
            ["Which Apollo moon mission was the first to carry a lunar rover?","Apollo 15"],
            ["What is the only number that has the same number of letters as its meaning?","Four"],
            ["What is the only even prime number?","Two"],
            ["What is the smallest perfect number?","Six"],
            ["What is the most popular lucky number?","Seven"],
            ["How many lives are cats said to have?","Nine"],
            ["How many cupcakes are in a bakers dozen?","Thirteen"],
            ["What flat image can also be displayed in 3D?","Hologram"],
            ["How many equal sides do Icosahedrons have?","Twenty"],
            ["What is the prefix meaning 10?","Deka"],
            ["How many sides does a dodecahedron have?","Twelve sides"],
            ["What is the mathematical name for a pound sign?","Octothorpe"],
            ["What civilization first used dot patterns to represent numbers?","Chinese"],
            ["How old was Isaac Newton when he developed integral calculus?","23 years old"],
            ["Who developed the cartesian axes?","René Descartes"],
            ["Where was the first recorded instance of math games played?","Africa(South of the Sahara)"]
             ]
        self.hard_choices = [
            ["Mercury","Earth","Venus"],
            ["Armstrong","Space X","Sputnik"],
            ["Mycology","Biology","Botany"],
            ["Insulator","Conductor","Vector"],
            ["Apollo 15","Apollo 16","Apollo 17"],
            ["Four","Five","Six"],
            ["One","Two","Three"],
            ["Five","Six","Seven"],
            ["Seven","Eight","Nine"],
            ["Seven","Eight","Nine"],
            ["Thirteen","Fourteen","Fifteen"],
            ["GUI(Graphical User Interface)","TUI(Tangible User Interface)","Hologram"],
            ["Eighteen","Nineteen","Twenty"],
            ["Dodeca","Undec-","Deka"],
            ["Twelve sides","Thirteen sides","Fourteen sides"],
            ["Octhothorpe","Octothorpe","Octtothorpe"],
            ["Chinese","Japanese","Thai"],
            ["21 years old","22 years old","23 years old"],
            ["Sigmund Freud","René Descartes","Saint Thomas Aquinas"],
            ["Africa(North of the Sahara)","Africa(East of the Sahara)","Africa(South of the Sahara)"], 
        ]
        
        self.mode = ""
        self.qstn_number = 0
        self.score = 0
        self.answered_mode = []
        self.selected_ans = ""

        #passing functions in every/widgets
        self.btn_easy.clicked.connect(self.btn_easy_func)
        self.btn_average.clicked.connect(self.btn_average_func)
        self.btn_hard.clicked.connect(self.btn_hard_func)


        self.btn_exit.clicked.connect(self.exit_game)
        self.chs_1.toggled.connect(self.chs_1_selected)
        self.chs_2.toggled.connect(self.chs_2_selected)
        self.chs_3.toggled.connect(self.chs_3_selected)
        self.btn_cancel.clicked.connect(self.cancel_mod)
        self.btn_next.clicked.connect(self.btn_next_func)
        self.btn_next_question.clicked.connect(self.btn_next_question_func)

    def btn_next_question_func(self):
        self.btn_next_question.hide()
        self.btn_next.hide()
        self.frame_4.hide()
        self.frame_correct.hide()
        self.chs_1.setDisabled(False)
        self.chs_2.setDisabled(False)
        self.chs_3.setDisabled(False)
        self.btn_next.setDisabled(False)
        self.chs_1.setAutoExclusive(False)
        self.chs_2.setAutoExclusive(False)
        self.chs_3.setAutoExclusive(False)
        self.chs_1.setChecked(False)
        self.chs_2.setChecked(False)
        self.chs_3.setChecked(False)

        if(self.mode == "EASY"):
            #if all the questions are displayed
            
            if(self.qstn_number == 20):
                self.answered_mode.append("EASY")
                
                if(len(self.answered_mode) != 3):
                    
                    ret = QMessageBox.question(self, 'Easy Mode Done!', "Do you want to continue onto the next mode?",
                                   QMessageBox.Yes | QMessageBox.No)
                    
                    if ret == QMessageBox.Yes:
                       
                        self.btn_easy.hide()
                        if("AVERAGE" not in self.answered_mode):
                            self.btn_average.show()
                        else:
                            self.btn_average.hide()
                        if("HARD" not in self.answered_mode):
                            self.btn_hard.show()
                        else:
                            self.btn_hard.hide()
                        self.mode = ""
                        self.selected_ans = ""
                        self.qstn_number = 0
                        self.frame_correct.hide()
                        self.frame_4.hide()
                        self.frame_choose.hide()
                        self.txtedit_question.hide()
                        self.btn_cancel.hide()
                        self.btn_next_question.hide()
                        self.lbl_mode.setText("MODE:")
                    elif ret == QMessageBox.No:
                        QMessageBox.about(self, "Thank You for Playing", "Overall Score: " + str(self.score))
                        exit()
                elif(len(self.answered_mode) == 3):
                     QMessageBox.about(self, "Conratulations", "Overall Score: " + str(self.score))
                     exit()
            else:
                self.selected_ans = ""
                self.qstn_number += 1
                self.lbl_question_number.setText("QUESTION NUMBER: " + str(self.qstn_number))
                self.txtedit_question.setText(self.mlist_easy[self.qstn_number-1][0])
                self.chs_1.setText(self.easy_choices[self.qstn_number-1][0])
                self.chs_2.setText(self.easy_choices[self.qstn_number-1][1])
                self.chs_3.setText(self.easy_choices[self.qstn_number-1][2])
        elif(self.mode == "AVERAGE"):
            #if all the questions are displayed
            
            if(self.qstn_number == 20):
                self.answered_mode.append("AVERAGE")
                if(len(self.answered_mode) != 3):
                    
                    ret = QMessageBox.question(self, 'Average Mode Done!', "Do you want to continue onto the next mode?",
                                   QMessageBox.Yes | QMessageBox.No)
                    
                    if ret == QMessageBox.Yes:
                        
                        self.btn_average.hide()
                        if("EASY" not in self.answered_mode):
                            self.btn_easy.show()
                        else:
                            self.btn_easy.hide()
                        if("HARD" not in self.answered_mode):
                            self.btn_hard.show()
                        else:
                            self.btn_hard.hide()
                        self.mode = ""
                        self.selected_ans = ""
                        self.qstn_number = 0
                        self.frame_correct.hide()
                        self.frame_4.hide()
                        self.frame_choose.hide()
                        self.txtedit_question.hide()
                        self.btn_cancel.hide()
                        self.btn_next_question.hide()
                        self.lbl_mode.setText("MODE:")
                    elif ret == QMessageBox.No:
                        QMessageBox.about(self, "Thank You for Playing", "Overall Score: " + str(self.score))
                        exit()
                elif(len(self.answered_mode) == 3):
                     QMessageBox.about(self, "Conratulations", "Overall Score: " + str(self.score))
                     exit()
            
            else:
                self.selected_ans = ""
                self.qstn_number += 1
                self.lbl_question_number.setText("QUESTION NUMBER: " + str(self.qstn_number))
                self.txtedit_question.setText(self.mlist_average[self.qstn_number-1][0])
                self.chs_1.setText(self.average_choices[self.qstn_number-1][0])
                self.chs_2.setText(self.average_choices[self.qstn_number-1][1])
                self.chs_3.setText(self.average_choices[self.qstn_number-1][2])
        
        elif(self.mode == "HARD"):
            #if all the questions are displayed
            if(self.qstn_number == 20):
                self.answered_mode.append("HARD")
                if(len(self.answered_mode) != 3):
                    
                    ret = QMessageBox.question(self, 'Hard Mode Done!', "Do you want to continue onto the next mode?",
                                   QMessageBox.Yes | QMessageBox.No)
                    if ret == QMessageBox.Yes:
                        
                        self.btn_hard.hide()
                        if("EASY" not in self.answered_mode):
                            self.btn_easy.show()
                        else:
                            self.btn_easy.hide()
                        if("AVERAGE" not in self.answered_mode):
                            self.btn_average.show()
                        else:
                            self.btn_average.hide()
                        self.mode = ""
                        self.selected_ans = ""
                        self.qstn_number = 0
                        self.frame_correct.hide()
                        self.frame_4.hide()
                        self.frame_choose.hide()
                        self.txtedit_question.hide()
                        self.btn_cancel.hide()
                        self.btn_next_question.hide()
                        self.lbl_mode.setText("MODE:")
                    elif ret == QMessageBox.No:
                        QMessageBox.about(self, "Thank You for Playing", "Overall Score: " + str(self.score))
                        exit()
                elif(len(self.answered_mode) == 3):
                     QMessageBox.about(self, "Conratulations", "Overall Score: " + str(self.score))
                     exit()
                            
            
            else:
                self.selected_ans = ""
                self.qstn_number += 1
                self.lbl_question_number.setText("QUESTION NUMBER: " + str(self.qstn_number))
                self.txtedit_question.setText(self.mlist_hard[self.qstn_number-1][0])
                self.chs_1.setText(self.hard_choices[self.qstn_number-1][0])
                self.chs_2.setText(self.hard_choices[self.qstn_number-1][1])
                self.chs_3.setText(self.hard_choices[self.qstn_number-1][2])


    def btn_next_func(self):
        self.btn_next_question.show()
        self.chs_1.setDisabled(True)
        self.chs_2.setDisabled(True)
        self.chs_3.setDisabled(True)
        self.btn_next.setDisabled(True)
        if(self.mode == "EASY"):
            get_correct_ans = self.mlist_easy[self.qstn_number-1][1]
            print(str(get_correct_ans) + "asdf")
            if(get_correct_ans == self.selected_ans):
                self.frame_correct.show()
                self.frame_4.hide()
                self.lbl_answer1.setText("Answer:" + get_correct_ans)
                self.score = self.score+1
                self.lbl_score.setText("SCORE: " + str(self.score))
            else:
                self.frame_correct.hide()
                self.frame_4.show()
                self.lbl_answer2.setText("Answer:" + get_correct_ans)
        elif(self.mode == "AVERAGE"):
            
            get_correct_ans = self.mlist_average[self.qstn_number-1][1]
            print(str(get_correct_ans) + "asdf")
            if(get_correct_ans == self.selected_ans):
                self.frame_correct.show()
                self.frame_4.hide()
                self.lbl_answer1.setText("Answer:" + get_correct_ans)
                self.score = self.score+2
                self.lbl_score.setText("SCORE: " + str(self.score))
            else:
                self.frame_correct.hide()
                self.frame_4.show()
                self.lbl_answer2.setText("Answer:" + get_correct_ans)
                

        elif(self.mode == "HARD"):
            
            get_correct_ans = self.mlist_hard[self.qstn_number-1][1]
            if(get_correct_ans == self.selected_ans):
                self.frame_correct.show()
                self.frame_4.hide()
                self.lbl_answer1.setText("Answer:" + get_correct_ans)
                self.score = self.score+3
                self.lbl_score.setText("SCORE: " + str(self.score))
            else:
                self.frame_correct.hide()
                self.frame_4.show()
                self.lbl_answer2.setText("Answer:" + get_correct_ans)
                
                
        

    def exit_game(self):
        ret = QMessageBox.question(self, 'Exit Game?', "Are you sure you want to Exit the Game?",
                                   QMessageBox.Yes | QMessageBox.No)

        if ret == QMessageBox.Yes:
            exit()



    def btn_easy_func(self):
        if(self.mode == ""):
            self.btn_average.hide()
            self.btn_next_question.hide()
            self.btn_hard.hide()
            self.frame_choose.show()
            self.txtedit_question.show()
            self.btn_cancel.show()
            self.mode = "EASY"
            self.btn_next.hide()
            self.lbl_mode.setText("MODE: " + self.mode)
            self.lbl_score.setText("SCORE: " + str(self.score))
            self.qstn_number = 0
            self.qstn_number += 1
            self.lbl_question_number.setText("QUESTION NUMBER: " + str(self.qstn_number))
            self.txtedit_question.setText(self.mlist_easy[0][0])
            self.chs_1.setText(self.easy_choices[0][0])
            self.chs_2.setText(self.easy_choices[0][1])
            self.chs_3.setText(self.easy_choices[0][2])

    def btn_average_func(self):
        if(self.mode == ""):
            self.btn_next_question.hide()
            self.btn_easy.hide()
            self.btn_hard.hide()
            self.frame_choose.show()
            self.txtedit_question.show()
            self.btn_cancel.show()
            self.mode = "AVERAGE"
            self.btn_next.hide()
            self.lbl_mode.setText("MODE: " + self.mode)
            self.lbl_score.setText("SCORE: " + str(self.score))
            self.qstn_number = 0
            self.qstn_number += 1
            self.lbl_question_number.setText("QUESTION NUMBER: " + str(self.qstn_number))
            self.txtedit_question.setText(self.mlist_average[0][0])
            self.chs_1.setText(self.average_choices[0][0])
            self.chs_2.setText(self.average_choices[0][1])
            self.chs_3.setText(self.average_choices[0][2])

    def btn_hard_func(self):
        if(self.mode == ""):
            self.btn_next_question.hide()
            self.btn_easy.hide()
            self.btn_average.hide()
            self.frame_choose.show()
            self.txtedit_question.show()
            self.btn_cancel.show()
            self.mode = "HARD"
            self.btn_next.hide()
            self.lbl_mode.setText("MODE: " + self.mode)
            self.lbl_score.setText("SCORE: " + str(self.score))
            self.qstn_number = 0
            self.qstn_number += 1
            self.lbl_question_number.setText("QUESTION NUMBER: " + str(self.qstn_number))
            self.txtedit_question.setText(self.mlist_hard[0][0])
            self.chs_1.setText(self.hard_choices[0][0])
            self.chs_2.setText(self.hard_choices[0][1])
            self.chs_3.setText(self.hard_choices[0][2])


    def chs_1_selected(self, selected):
        if selected:
            self.chs_2.setChecked(False)
            self.chs_3.setChecked(False)
            self.selected_ans = self.chs_1.text()
            print(self.selected_ans)
            self.btn_next.show()

    def chs_2_selected(self, selected):
        if selected:
            self.chs_1.setChecked(False)
            self.chs_3.setChecked(False)
            self.selected_ans = self.chs_2.text()
            print(self.selected_ans)
            self.btn_next.show()

    def chs_3_selected(self, selected):
        if selected:
            self.chs_1.setChecked(False)
            self.chs_2.setChecked(False)
            self.selected_ans = self.chs_3.text()
            print(self.selected_ans)
            self.btn_next.show()
    
    def cancel_mod(self):
        ret = QMessageBox.question(self, 'Restart the game?', "The Game will reset if you restart",
                                   QMessageBox.Yes | QMessageBox.No)

        if ret == QMessageBox.Yes:
            self.mode = ""
            self.qstn_number = 0
            self.score = 0
            self.chs_1.setDisabled(False)
            self.chs_2.setDisabled(False)
            self.chs_3.setDisabled(False)
            self.btn_next.setDisabled(False)
            self.chs_1.setAutoExclusive(False)
            self.chs_2.setAutoExclusive(False)
            self.chs_3.setAutoExclusive(False)
            self.chs_1.setChecked(False)
            self.chs_2.setChecked(False)
            self.chs_3.setChecked(False)
            self.answered_mode = []
            self.selected_ans = ""
            self.frame_correct.hide()
            self.frame_4.hide()
            self.frame_choose.hide()
            self.txtedit_question.hide()
            self.btn_cancel.hide()
            self.btn_next_question.hide()
            self.lbl_mode.setText("MODE:")
            self.btn_average.show()
            self.btn_hard.show()
            self.btn_easy.show()
            self.lbl_question_number.setText("QUESTION NUMBER: ")
            self.lbl_score.setText("SCORE: " + str(self.score))
if __name__ == "__main__":
    apps = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    w1 = newWindow1()
    w1.show()
    apps.exec_()