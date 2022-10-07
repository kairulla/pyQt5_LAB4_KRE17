#!/usr/bin/env python3
# coding=utf-8

import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QItemSelectionModel
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem
from PyQt5.uic import loadUi
import math
import random


class Launcher(QDialog):
    array_global = []
    max_value = 0
    max_i = 0

    def __init__(self):
        super(Launcher, self).__init__()
        loadUi('g.ui', self)

        self.setWindowTitle('Лабораторная 4 _ Python3 + PyQt5')
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        # Задание иконки окна
        self.setWindowIcon(QtGui.QIcon('_MY_PICTURES//logo.png'))

        self.qPushButtonRandom.clicked.connect(self.qPushButtonRandomOnClick)
        self.qPushButtonSolver.clicked.connect(self.qPushButtonSolverOnClick)


    def qPushButtonRandomOnClick(self):
        n = 4
        m = 5
        max_number = 100

        array = []
        for i in range(0, n):
            sub_array = []
            for j in range(m):
                number = random.randint(0, max_number)
                sub_array.append(number)
            array.append(sub_array)

        for row, i in enumerate(array):
            for col, j in enumerate(i):
                self.qTableWidget.setItem(row, col, QTableWidgetItem(str(j)))


        i = 0
        max_value = array[1][i]
        max_i = i
        for i, j in enumerate(array[1]):
            # print("i=", i)
            if j > max_value:
                max_value = j
                max_i = i
        self.qLabelMaxItemValue.setText("Максимальный элемент = %s" % max_value)
        print("max_value=", max_value)
        print("max_i=", max_i)
        self.array_global = array.copy()
        self.max_value = max_value
        self.max_i = max_i




    def qPushButtonSolverOnClick(self):
        # array = self.array_global.copy()
        # max_value = self.max_value
        # max_i = self.max_i
        # if (max_value > array[2][0]):
        #     temp = array[2][0]
        #     array[2][0] = max_value
        #     array[1][max_i] = temp
        #
        #     for row, i in enumerate(array):
        #         for col, j in enumerate(i):
        #             self.qTableWidget.setItem(row, col, QTableWidgetItem(str(j)))
        try:
            b = []
            for i in range(4):
                sub_array = []
                for j in range(5):
                    try:
                        temp = int(self.qTableWidget.item(i, j).text())
                    except:
                        self.qTableWidget.setItem(i, j, QTableWidgetItem("???"))
                    sub_array.append(temp)
                b.append(sub_array)
            # a = self.qTableWidget.item(select.selectedRows(), select.selectedColums()).text()
            # a = self.qTableWidget.item(0, 0).text()

            array = b.copy()
            max_value = self.max_value
            max_i = self.max_i
            if (max_value > array[2][0]):
                temp = array[2][0]
                array[2][0] = max_value
                array[1][max_i] = temp

                for row, i in enumerate(array):
                    for col, j in enumerate(i):
                        self.qTableWidget.setItem(row, col, QTableWidgetItem(str(j)))

            print(b)


            n = 4
            m = 5
            max_number = 100

            array = b

            i = 0
            max_value = array[1][i]
            max_i = i
            for i, j in enumerate(array[1]):
                # print("i=", i)
                if j > max_value:
                    max_value = j
                    max_i = i
            self.qLabelMaxItemValue.setText("Максимальный элемент = %s" % max_value)
            print("max_value=", max_value)
            print("max_i=", max_i)

            if (max_value > array[2][0]):
                temp = array[2][0]
                array[2][0] = max_value
                array[1][max_i] = temp

                for row, i in enumerate(array):
                    for col, j in enumerate(i):
                        self.qTableWidget.setItem(row, col, QTableWidgetItem(str(j)))

        except:
            self.qLabelMaxItemValue.setText("Ошибка")

if __name__ == '__main__':
    # Основная часть программы
    app = QApplication(sys.argv)
    window = Launcher()  # базовый класс окна
    window.show()  # отобразить окно на экране
    sys.exit(app.exec_())  # запуск основного цикла приложения
