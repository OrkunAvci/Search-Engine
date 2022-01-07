# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import process_reverse_index as pri
import file_manager as fm

reverseIndex = fm.get('_reverse_index_final')

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 678)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(50, 300, 93, 28))
        self.searchButton.setObjectName("searchButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(330, 40, 720, 571))
        self.listWidget.setObjectName("listWidget")
        self.searchBar = QtWidgets.QTextEdit(self.centralwidget)
        self.searchBar.setGeometry(QtCore.QRect(20, 250, 281, 41))
        self.searchBar.setObjectName("searchBar")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(170, 300, 93, 28))
        self.clearButton.setObjectName("clearButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 887, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.searchBar.setFont(QtGui.QFont('Times New', 13))
        self.listWidget.setFont(QtGui.QFont('Times New', 10))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 210, 211, 31))
        self.label.setObjectName("label")
        self.label.setFont(QtGui.QFont('Times New', 12))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TF-IDF Calculator"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.searchButton.clicked.connect(self.startSearch)
        self.clearButton.clicked.connect(self.clear)
        self.label.setText(_translate("MainWindow", "Input Word:"))


    def startSearch(self):
        self.clear()
        inputWord = self.searchBar.toPlainText()
        if inputWord == '':
            self.listWidget.addItem("Input field must not be empty!")
            return

        sortedList = pri.getTfIdfsOfWord(inputWord, reverseIndex)
        myFont = QtGui.QFont()
        myFont.setBold(True)




        if sortedList != None:
            for data in sortedList:
                item1 = QtWidgets.QListWidgetItem()
                item1.setText("LINK:")
                item1.setFont(myFont)
                self.listWidget.addItem(item1)
                self.listWidget.addItem(data["link"])
                item2 = QtWidgets.QListWidgetItem()
                item2.setText("TF-IDF VALUE:")
                item2.setFont(myFont)
                self.listWidget.addItem(item2)
                self.listWidget.addItem(str(data["TF-IDF"]))
                self.listWidget.addItem("-------------------------------")
        else:
            self.listWidget.addItem("Results couldn't be found based on your input value")

    def clear(self):
        self.listWidget.clear()





if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())

