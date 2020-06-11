# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lesson07.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(610, 506)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 591, 80))
        self.widget.setObjectName("widget")
        self.lbl_path_db = QtWidgets.QLabel(self.widget)
        self.lbl_path_db.setGeometry(QtCore.QRect(10, 10, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.lbl_path_db.setFont(font)
        self.lbl_path_db.setObjectName("lbl_path_db")
        self.lbl_full_path_db = QtWidgets.QLabel(self.widget)
        self.lbl_full_path_db.setEnabled(False)
        self.lbl_full_path_db.setGeometry(QtCore.QRect(10, 30, 571, 16))
        self.lbl_full_path_db.setObjectName("lbl_full_path_db")
        self.btn_db_open = QtWidgets.QPushButton(self.widget)
        self.btn_db_open.setGeometry(QtCore.QRect(10, 50, 121, 23))
        self.btn_db_open.setAutoDefault(True)
        self.btn_db_open.setFlat(False)
        self.btn_db_open.setObjectName("btn_db_open")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(10, 440, 181, 23))
        self.btn_add.setObjectName("btn_add")
        self.btn_del = QtWidgets.QPushButton(self.centralwidget)
        self.btn_del.setGeometry(QtCore.QRect(210, 440, 181, 23))
        self.btn_del.setObjectName("btn_del")
        self.tablelist = QtWidgets.QComboBox(self.centralwidget)
        self.tablelist.setGeometry(QtCore.QRect(110, 100, 171, 22))
        self.tablelist.setObjectName("tablelist")
        self.lbl_table_list = QtWidgets.QLabel(self.centralwidget)
        self.lbl_table_list.setGeometry(QtCore.QRect(20, 100, 91, 21))
        self.lbl_table_list.setObjectName("lbl_table_list")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 130, 591, 301))
        self.tableView.setObjectName("tableView")
        self.save_changes = QtWidgets.QPushButton(self.centralwidget)
        self.save_changes.setGeometry(QtCore.QRect(420, 440, 181, 23))
        self.save_changes.setObjectName("save_changes")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 610, 21))
        self.menubar.setObjectName("menubar")
        self.mnu_file = QtWidgets.QMenu(self.menubar)
        self.mnu_file.setObjectName("mnu_file")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.mnu_exit = QtWidgets.QAction(MainWindow)
        self.mnu_exit.setObjectName("mnu_exit")
        self.mnu_file.addAction(self.mnu_exit)
        self.menubar.addAction(self.mnu_file.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Учет товаров"))
        self.lbl_path_db.setText(_translate("MainWindow", "Путь к базе данных"))
        self.lbl_full_path_db.setText(_translate("MainWindow", "TextLabel"))
        self.btn_db_open.setText(_translate("MainWindow", "Открыть БД"))
        self.btn_add.setText(_translate("MainWindow", "Добавить запись"))
        self.btn_del.setText(_translate("MainWindow", "Удалить запись"))
        self.lbl_table_list.setText(_translate("MainWindow", "Список таблиц"))
        self.save_changes.setText(_translate("MainWindow", "Сохранить изменения"))
        self.mnu_file.setTitle(_translate("MainWindow", "Файл"))
        self.mnu_exit.setText(_translate("MainWindow", "Выход"))
