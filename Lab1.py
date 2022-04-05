from PyQt5.QtWidgets import QApplication
from PyQt5 import uic
from pulp import *

Form, Window = uic.loadUiType("F:\Системный Анализ\\form.ui")


def button_answer():
    first_type_a = int(form.lineEdit.text())
    second_type_a = int(form.lineEdit_2.text())
    third_type_a = int(form.lineEdit_3.text())

    first_type_b = int(form.lineEdit_4.text())
    second_type_b = int(form.lineEdit_5.text())
    third_type_b = int(form.lineEdit_6.text())

    first_type_stock = int(form.lineEdit_7.text())
    second_type_stock = int(form.lineEdit_8.text())
    third_type_stock = int(form.lineEdit_9.text())

    pr_b = int(form.lineEdit_11.text())
    pr_a = int(form.lineEdit_10.text())

    model = LpProblem("Volkogonov", LpMaximize)

    A = LpVariable('A', lowBound=0, cat='Integer')
    B = LpVariable('B', lowBound=0, cat='Integer')

    model += pr_a * A + pr_b * B

    model += first_type_a * A + first_type_b * B <= first_type_stock
    model += second_type_a * A + second_type_b * B <= second_type_stock
    model += third_type_a * A + third_type_b * B <= third_type_stock
    model += A <= B

    model.solve()

    form.textBrowser.append(f"Необходимо произвести : {A.varValue} товаров типа А")
    form.textBrowser.append(f"Необходимо произвести : {B.varValue} товаров типа B")


app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
form.pushButton.clicked.connect(button_answer)
app.exec()
