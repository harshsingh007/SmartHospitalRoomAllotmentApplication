# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hospital.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(854, 583)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(50, 90, 321, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))



        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(570, 90, 141, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        ###########################################################################################
        self.pushButton.clicked.connect(self.buttonClicked)
        self.pushButton.clicked.connect(self.download)
        #########################################################################################



        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 190, 111, 31))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 190, 111, 31))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(300, 190, 111, 31))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(560, 190, 111, 31))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(430, 190, 111, 31))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.lineEdit_7 = QtGui.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(690, 190, 111, 31))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.lineEdit_8 = QtGui.QLineEdit(Dialog)
        self.lineEdit_8.setGeometry(QtCore.QRect(170, 280, 111, 31))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.lineEdit_9 = QtGui.QLineEdit(Dialog)
        self.lineEdit_9.setGeometry(QtCore.QRect(430, 280, 111, 31))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.lineEdit_10 = QtGui.QLineEdit(Dialog)
        self.lineEdit_10.setGeometry(QtCore.QRect(560, 280, 111, 31))
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.lineEdit_11 = QtGui.QLineEdit(Dialog)
        self.lineEdit_11.setGeometry(QtCore.QRect(40, 280, 111, 31))
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.lineEdit_12 = QtGui.QLineEdit(Dialog)
        self.lineEdit_12.setGeometry(QtCore.QRect(690, 280, 111, 31))
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.lineEdit_13 = QtGui.QLineEdit(Dialog)
        self.lineEdit_13.setGeometry(QtCore.QRect(300, 280, 111, 31))
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.lineEdit_14 = QtGui.QLineEdit(Dialog)
        self.lineEdit_14.setGeometry(QtCore.QRect(300, 370, 111, 31))
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.lineEdit_15 = QtGui.QLineEdit(Dialog)
        self.lineEdit_15.setGeometry(QtCore.QRect(170, 370, 111, 31))
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.lineEdit_16 = QtGui.QLineEdit(Dialog)
        self.lineEdit_16.setGeometry(QtCore.QRect(40, 370, 111, 31))
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.lineEdit_17 = QtGui.QLineEdit(Dialog)
        self.lineEdit_17.setGeometry(QtCore.QRect(560, 370, 111, 31))
        self.lineEdit_17.setObjectName(_fromUtf8("lineEdit_17"))
        self.lineEdit_18 = QtGui.QLineEdit(Dialog)
        self.lineEdit_18.setGeometry(QtCore.QRect(430, 370, 111, 31))
        self.lineEdit_18.setObjectName(_fromUtf8("lineEdit_18"))
        self.lineEdit_19 = QtGui.QLineEdit(Dialog)
        self.lineEdit_19.setGeometry(QtCore.QRect(690, 370, 111, 31))
        self.lineEdit_19.setObjectName(_fromUtf8("lineEdit_19"))
        self.lineEdit_20 = QtGui.QLineEdit(Dialog)
        self.lineEdit_20.setGeometry(QtCore.QRect(110, 460, 321, 31))
        self.lineEdit_20.setObjectName(_fromUtf8("lineEdit_20"))


        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 460, 161, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        ###########################################################################################
        self.pushButton_2.clicked.connect(self.buttonClicked_1)
        self.pushButton_2.clicked.connect(self.download)
        #########################################################################################


        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 70, 131, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(290, 160, 231, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(210, 440, 141, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(220, 530, 481, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        ################################################################################
    def buttonClicked(self):

      #  id = self.item_id.text()




        id=self.lineEdit.text()

        f = open("hospital_dataset.csv", "r")
        f.readline()
        dis = id

        for i in f.readlines():
        #     print(i)

            k = i.split(",")
            if (k[0] == dis):
                print(k)
                break

        maxtemp = int(k[1])
        maxhum = int(k[2])
        maxair = int(k[3])
        print(maxtemp, maxhum, maxair)

    # f.close()
        f1 = open("room_description.csv", "r")
        f1.readline()
        l1 = list()
        for i in f1.readlines():
        #     print(i)
            k = i.split(",")
        #     print(k)
            t = int(k[1])
            h = int(k[2])
            a = int(k[3])
            s = int(k[4])

            if (t <= maxtemp and h <= maxhum and a <= maxair and s!=1):
                l1.append(k[0])
                # print(k[0])
        print(l1)
        try:
            self.lineEdit_2.setText(l1[0])
            self.lineEdit_3.setText(l1[1])
            self.lineEdit_4.setText(l1[2])
            self.lineEdit_5.setText(l1[3])
            self.lineEdit_6.setText(l1[4])
            self.lineEdit_7.setText(l1[5])
            self.lineEdit_8.setText(l1[6])
            self.lineEdit_9.setText(l1[7])
            self.lineEdit_10.setText(l1[8])
            self.lineEdit_11.setText(l1[9])
            self.lineEdit_12.setText(l1[10])
            self.lineEdit_13.setText(l1[11])
            self.lineEdit_14.setText(l1[12])
            self.lineEdit_15.setText(l1[13])
            self.lineEdit_16.setText(l1[14])
            self.lineEdit_17.setText(l1[15])
            self.lineEdit_18.setText(l1[16])
            self.lineEdit_19.setText(l1[17])
        except:
            pass




############################################################################################
      ################################################################################

    def buttonClicked_1(self):
        #  id = self.item_id.text()

        roomid = self.lineEdit_20.text()
        f1 = open("room_description.csv", "r")
        f1.readline()
        l1 = list()

        for i in f1.readlines():
            k = i.split(",")
            if (k[0] != roomid):
                l1.append(i)
            if (k[0] == roomid):
                a = k[0] + "," + k[1] + "," + k[2] + "," + k[3] + "," + "1" + "\n"
                l1.append(a)

        f1.close()
        f1 = open("room_description.csv", "w")
        for i in l1:
            f1.write(i)
        f1.close()












    ############################################################################################
      ############################################################################################

    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001

            self.progressBar.setValue(self.completed)

    #############################################################################################

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "Search Avialable Rooms", None))
        self.pushButton_2.setText(_translate("Dialog", "Allocate", None))
        self.label.setText(_translate("Dialog", "Enter the Disease", None))
        self.label_2.setText(_translate("Dialog", "Please select rooms from these Avialable Rooms", None))
        self.label_3.setText(_translate("Dialog", "Enter the Room Number", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

